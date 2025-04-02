# Installation du package (à exécuter une seule fois)
# pip install aif360

import numpy as np
import pandas as pd
from aif360.datasets import BinaryLabelDataset, StandardDataset
from aif360.metrics import BinaryLabelDatasetMetric
from aif360.algorithms.preprocessing import Reweighing
from aif360.algorithms.preprocessing import DisparateImpactRemover
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Fonction pour charger et préparer les données
def load_data(filepath, protected_attribute, target_column, privileged_values=None, favorable_values=None):
    """
    Charge le dataset et le prépare pour l'analyse de biais
    
    Parameters:
    -----------
    filepath: str
        Chemin vers le fichier de données
    protected_attribute: str ou list
        Nom(s) de(s) colonne(s) contenant le(s) attribut(s) protégé(s)
    target_column: str
        Nom de la colonne cible
    privileged_values: dict
        Dictionnaire avec les attributs protégés comme clés et les valeurs privilégiées comme valeurs
    favorable_values: list ou int
        Valeur(s) considérée(s) comme favorable(s) dans la colonne cible
    """
    # Charger les données
    df = pd.read_csv(filepath)
    
    # Conversion des attributs protégés en liste si ce n'est pas déjà le cas
    if isinstance(protected_attribute, str):
        protected_attribute = [protected_attribute]
    
    # Afficher des informations sur les colonnes
    print("\n=== Informations sur les colonnes clés ===")
    for attr in protected_attribute:
        print(f"Attribut protégé '{attr}' - valeurs uniques: {df[attr].unique()}")
    print(f"Colonne cible '{target_column}' - valeurs uniques: {df[target_column].unique()}")
    
    # Si privileged_values n'est pas fourni, demander à l'utilisateur
    if privileged_values is None:
        privileged_values = {}
        print("\n=== Configuration des valeurs privilégiées ===")
        for attr in protected_attribute:
            unique_vals = df[attr].unique()
            print(f"Valeurs uniques pour '{attr}': {unique_vals}")
            if len(unique_vals) == 2:
                # Si binaire, suggérer la valeur la plus élevée comme privilégiée
                suggested = max(unique_vals)
                privileged_values[attr] = suggested
                print(f"Pour '{attr}', valeur privilégiée considérée: {suggested}")
            else:
                # Pour les cas non binaires, nous devons définir explicitement
                print(f"Pour '{attr}', spécifiez la valeur privilégiée dans le code")
                privileged_values[attr] = unique_vals[0]  # Par défaut, première valeur
    
    # Si favorable_values n'est pas fourni, demander à l'utilisateur
    if favorable_values is None:
        unique_vals = df[target_column].unique()
        print("\n=== Configuration des valeurs favorables ===")
        print(f"Valeurs uniques pour '{target_column}': {unique_vals}")
        if len(unique_vals) == 2:
            # Si binaire, suggérer la valeur la plus élevée comme favorable
            favorable_values = [max(unique_vals)]
            print(f"Pour '{target_column}', valeur favorable considérée: {favorable_values[0]}")
        else:
            # Pour les cas non binaires, nous devons définir explicitement
            print(f"Pour '{target_column}', spécifiez la valeur favorable dans le code")
            favorable_values = [unique_vals[-1]]  # Par défaut, dernière valeur
    
    # Obtenir toutes les colonnes sauf target
    features = df.columns.tolist()
    features.remove(target_column)
    
    # Créer un dataset AIF360 approprié en fonction du type de données
    if len(favorable_values) == 1 and all(len(df[attr].unique()) == 2 for attr in protected_attribute):
        # Cas simple: binaire -> utiliser BinaryLabelDataset
        aif_dataset = BinaryLabelDataset(
            df=df,
            label_names=[target_column],
            protected_attribute_names=protected_attribute,
            favorable_label=favorable_values[0],
            unfavorable_label=list(set(df[target_column].unique()) - set(favorable_values))[0]
        )
    else:
        # Cas complexe: multi-valeurs -> utiliser StandardDataset
        aif_dataset = StandardDataset(
            df=df,
            label_name=target_column,
            favorable_classes=favorable_values,
            protected_attribute_names=protected_attribute,
            privileged_classes=[privileged_values[attr] for attr in protected_attribute]
        )
    
    return aif_dataset, features, protected_attribute, privileged_values, favorable_values

# Fonction pour créer les groupes privilégiés/non privilégiés à partir des attributs protégés
def create_groups(protected_attributes, privileged_values):
    """
    Crée les dictionnaires pour les groupes privilégiés et non privilégiés
    
    Parameters:
    -----------
    protected_attributes: list
        Liste des attributs protégés
    privileged_values: dict
        Dictionnaire associant chaque attribut protégé à sa valeur privilégiée
    
    Returns:
    --------
    privileged_groups: list de dict
        Liste de dictionnaires pour les groupes privilégiés
    unprivileged_groups: list de dict
        Liste de dictionnaires pour les groupes non privilégiés
    """
    # Pour le cas simple d'un seul attribut protégé
    if len(protected_attributes) == 1:
        attr = protected_attributes[0]
        priv_value = privileged_values[attr]
        
        # Créer les groupes en fonction du type de valeur privilégiée
        if isinstance(priv_value, (list, np.ndarray)):
            privileged_groups = [{attr: v} for v in priv_value]
            # Pour les valeurs non privilégiées, il faudrait connaître toutes les valeurs possibles
            # Par simplicité, on suppose ici qu'il s'agit de valeurs binaires
            unprivileged_groups = [{attr: v} for v in [0, 1] if v not in priv_value]
        else:
            privileged_groups = [{attr: priv_value}]
            # Pour une valeur binaire, l'autre valeur est 1-valeur pour 0/1, mais peut être 
            # différente pour d'autres types
            if priv_value in [0, 1]:
                unprivileged_groups = [{attr: 1 - priv_value}]
            else:
                # Il faudrait spécifier explicitement la valeur non privilégiée
                print(f"Pour '{attr}', spécifiez la valeur non privilégiée dans le code")
                unprivileged_groups = [{attr: None}]  # À remplacer
    else:
        # Pour plusieurs attributs protégés, la logique devient plus complexe
        # et nécessiterait de prendre en compte toutes les combinaisons possibles
        # Pour l'exemple, nous prenons juste le premier attribut
        attr = protected_attributes[0]
        priv_value = privileged_values[attr]
        privileged_groups = [{attr: priv_value}]
        
        if priv_value in [0, 1]:
            unprivileged_groups = [{attr: 1 - priv_value}]
        else:
            # Il faudrait spécifier explicitement la valeur non privilégiée
            print(f"Pour '{attr}', spécifiez la valeur non privilégiée dans le code")
            unprivileged_groups = [{attr: None}]  # À remplacer
    
    return privileged_groups, unprivileged_groups

# Fonction pour détecter les biais
def detect_bias(dataset, privileged_groups, unprivileged_groups):
    """
    Détecte les biais dans le dataset et retourne un verdict sur la présence de biais
    """
    metrics = BinaryLabelDatasetMetric(
        dataset, 
        unprivileged_groups=unprivileged_groups,
        privileged_groups=privileged_groups
    )
    
    # Mesures de biais
    print("\n=== Métriques de biais ===")
    di = metrics.disparate_impact()
    spd = metrics.statistical_parity_difference()
    
    try:
        eod = metrics.equal_opportunity_difference()
        aod = metrics.average_odds_difference()
        print(f"Equal Opportunity Difference: {eod:.4f}")
        print(f"Average Odds Difference: {aod:.4f}")
    except:
        eod = None
        aod = None
        print("Note: Equal Opportunity et Average Odds ne peuvent pas être calculés (probablement en raison de données multi-classes)")
    
    print(f"Disparate Impact: {di:.4f}")
    print(f"Statistical Parity Difference: {spd:.4f}")
    
    # Détermination si le dataset est biaisé
    biased = False
    bias_reasons = []
    
    # Vérification du Disparate Impact (80% rule)
    if di < 0.8 or di > 1.25:
        biased = True
        if di < 0.8:
            bias_reasons.append(f"Disparate Impact de {di:.4f} < 0.8 (sous-représentation du groupe non privilégié)")
        else:
            bias_reasons.append(f"Disparate Impact de {di:.4f} > 1.25 (sur-représentation du groupe non privilégié)")
    
    # Vérification du Statistical Parity Difference
    if abs(spd) > 0.05:
        biased = True
        bias_reasons.append(f"Statistical Parity Difference de {abs(spd):.4f} > 0.05")
    
    # Vérification des autres métriques si disponibles
    if eod is not None and abs(eod) > 0.05:
        biased = True
        bias_reasons.append(f"Equal Opportunity Difference de {abs(eod):.4f} > 0.05")
    
    if aod is not None and abs(aod) > 0.05:
        biased = True
        bias_reasons.append(f"Average Odds Difference de {abs(aod):.4f} > 0.05")
    
    return metrics, biased, bias_reasons

# Fonction pour mitiger les biais avec Reweighing
def mitigate_bias_reweighing(dataset, privileged_groups, unprivileged_groups):
    """
    Atténue les biais en utilisant l'algorithme Reweighing
    """
    print("\n=== Mitigation avec Reweighing ===")
    reweighing = Reweighing(unprivileged_groups=unprivileged_groups,
                           privileged_groups=privileged_groups)
    dataset_transformed = reweighing.fit_transform(dataset)
    
    # Évaluation après mitigation
    metrics_transformed = BinaryLabelDatasetMetric(
        dataset_transformed, 
        unprivileged_groups=unprivileged_groups,
        privileged_groups=privileged_groups
    )
    
    print("Après mitigation:")
    print(f"Disparate Impact: {metrics_transformed.disparate_impact():.4f}")
    print(f"Statistical Parity Difference: {metrics_transformed.statistical_parity_difference():.4f}")
    
    return dataset_transformed

# Fonction pour mitiger les biais avec Disparate Impact Remover
def mitigate_bias_dir(dataset, privileged_groups, unprivileged_groups, repair_level=1.0):
    """
    Atténue les biais en utilisant l'algorithme Disparate Impact Remover
    """
    print("\n=== Mitigation avec Disparate Impact Remover ===")
    dir = DisparateImpactRemover(repair_level=repair_level)
    dataset_transformed = dir.fit_transform(dataset)
    
    # Évaluation après mitigation
    metrics_transformed = BinaryLabelDatasetMetric(
        dataset_transformed, 
        unprivileged_groups=unprivileged_groups,
        privileged_groups=privileged_groups
    )
    
    print("Après mitigation:")
    print(f"Disparate Impact: {metrics_transformed.disparate_impact():.4f}")
    print(f"Statistical Parity Difference: {metrics_transformed.statistical_parity_difference():.4f}")
    
    return dataset_transformed

# Fonction pour évaluer l'impact sur un modèle de ML
def evaluate_model(original_dataset, transformed_dataset, features, privileged_groups, unprivileged_groups):
    """
    Évalue les performances d'un modèle avant et après mitigation
    """
    print("\n=== Évaluation de l'impact sur les performances d'un modèle ===")
    
    try:
        # Préparation des données originales
        X_orig = original_dataset.features
        y_orig = original_dataset.labels.ravel()
        X_train_orig, X_test_orig, y_train_orig, y_test_orig = train_test_split(X_orig, y_orig, test_size=0.3, random_state=42)
        
        # Préparation des données transformées
        X_trans = transformed_dataset.features
        y_trans = transformed_dataset.labels.ravel()
        X_train_trans, X_test_trans, y_train_trans, y_test_trans = train_test_split(X_trans, y_trans, test_size=0.3, random_state=42)
        
        # Vérifier s'il s'agit d'un problème binaire ou multiclasse
        unique_classes = np.unique(y_orig)
        if len(unique_classes) == 2:
            model_type = "binaire"
            model_orig = RandomForestClassifier(n_estimators=100, random_state=42)
            model_trans = RandomForestClassifier(n_estimators=100, random_state=42)
        else:
            model_type = "multiclasse"
            model_orig = RandomForestClassifier(n_estimators=100, random_state=42)
            model_trans = RandomForestClassifier(n_estimators=100, random_state=42)
        
        print(f"Type de problème détecté: {model_type} avec {len(unique_classes)} classes")
        
        # Entraînement et évaluation du modèle original
        model_orig.fit(X_train_orig, y_train_orig)
        y_pred_orig = model_orig.predict(X_test_orig)
        
        # Entraînement et évaluation du modèle transformé
        model_trans.fit(X_train_trans, y_train_trans)
        y_pred_trans = model_trans.predict(X_test_trans)
        
        # Affichage des résultats
        acc_orig = accuracy_score(y_test_orig, y_pred_orig)
        acc_trans = accuracy_score(y_test_trans, y_pred_trans)
        
        print("Modèle original:")
        print(f"Précision: {acc_orig:.4f}")
        print("Matrice de confusion:")
        print(confusion_matrix(y_test_orig, y_pred_orig))
        
        print("\nModèle après mitigation:")
        print(f"Précision: {acc_trans:.4f}")
        print("Matrice de confusion:")
        print(confusion_matrix(y_test_trans, y_pred_trans))
        
        # Vérification si le modèle mitigé maintient une bonne performance
        performance_drop = acc_orig - acc_trans
        if performance_drop > 0.05:
            print(f"\nAttention: La mitigation a réduit la précision du modèle de {performance_drop:.4f} points")
        else:
            print(f"\nLa mitigation a eu un impact limité sur la précision ({performance_drop:.4f} points)")
        
        return acc_orig, acc_trans
        
    except Exception as e:
        print(f"Erreur lors de l'évaluation du modèle: {e}")
        print("L'évaluation du modèle n'a pas pu être effectuée, possiblement en raison de la complexité des données.")
        return None, None

# Vérification finale des biais après mitigation
def check_final_bias(dataset_transformed, privileged_groups, unprivileged_groups):
    """
    Vérifie si les biais ont été effectivement mitigés
    """
    metrics_transformed, still_biased, bias_reasons = detect_bias(dataset_transformed, privileged_groups, unprivileged_groups)
    
    print("\n=== Conclusion après mitigation ===")
    if still_biased:
        print("Le dataset reste biaisé après mitigation pour les raisons suivantes:")
        for reason in bias_reasons:
            print(f"- {reason}")
        print("\nRecommandation: Envisagez d'autres techniques de mitigation ou une combinaison de méthodes.")
    else:
        print("La mitigation a réussi! Le dataset ne présente plus de biais significatifs.")
    
    return still_biased

# Programme principal
def main():
    # Paramètres à configurer
    filepath = "votre_dataset.csv"  # Remplacez par le chemin vers votre fichier
    
    # Colonnes à utiliser - À CONFIGURER selon votre dataset
    protected_attribute = "gender"  # Peut être une liste ["gender", "race", ...] pour plusieurs attributs
    target_column = "target"
    
    # Valeurs privilégiées et favorables - À CONFIGURER ou laisser None pour détection automatique
    # Exemples:
    # - Pour attributs binaires (0/1), généralement: privileged_values = {"gender": 1, "race": 1}
    # - Pour attributs catégoriels: privileged_values = {"gender": "male", "race": "white"}
    # - Pour attributs numériques: privileged_values = {"age": [lambda x: x >= 25 and x <= 60]}
    privileged_values = None  # Laissez None pour détection automatique ou spécifiez
    
    # Valeurs favorables - Généralement la classe positive pour les problèmes binaires
    # Pour problèmes multi-classes, spécifiez les classes considérées comme favorables
    # Exemples:
    # - Binaire: favorable_values = [1]
    # - Multi-classe: favorable_values = ["approved", "accepted"]
    favorable_values = None  # Laissez None pour détection automatique ou spécifiez
    
    # Chargement des données
    try:
        dataset, features, protected_attribute_list, privileged_values, favorable_values = load_data(
            filepath, protected_attribute, target_column, privileged_values, favorable_values
        )
        print(f"Dataset chargé avec succès: {dataset.shape}")
        print(f"Attribut(s) protégé(s): {protected_attribute_list}")
        
        # Création des groupes
        privileged_groups, unprivileged_groups = create_groups(protected_attribute_list, privileged_values)
        
        print("\n=== Groupes définis ===")
        print(f"Groupe(s) privilégié(s): {privileged_groups}")
        print(f"Groupe(s) non privilégié(s): {unprivileged_groups}")
        
    except Exception as e:
        print(f"Erreur lors du chargement des données: {e}")
        return
    
    # Détection des biais
    metrics, is_biased, bias_reasons = detect_bias(dataset, privileged_groups, unprivileged_groups)
    
    # Verdict sur la présence de biais
    print("\n=== VERDICT SUR LA PRÉSENCE DE BIAIS ===")
    if is_biased:
        print("VERDICT: Le dataset est BIAISÉ pour les raisons suivantes:")
        for reason in bias_reasons:
            print(f"- {reason}")
        
        # Mitigation des biais si biaisé
        print("\nApplication des techniques de mitigation...")
        
        try:
            # Mitigation des biais avec Reweighing
            dataset_reweighed = mitigate_bias_reweighing(dataset, privileged_groups, unprivileged_groups)
            
            # Vérification des biais après Reweighing
            still_biased_reweighing = check_final_bias(dataset_reweighed, privileged_groups, unprivileged_groups)
            
            # Si toujours biaisé, essayer une autre méthode
            if still_biased_reweighing:
                print("\nEssai d'une méthode alternative...")
                # Mitigation des biais avec Disparate Impact Remover
                dataset_dir = mitigate_bias_dir(dataset, privileged_groups, unprivileged_groups, repair_level=0.8)
                still_biased_dir = check_final_bias(dataset_dir, privileged_groups, unprivileged_groups)
                
                # Choisir le meilleur dataset mitigé pour l'évaluation du modèle
                if still_biased_dir:
                    print("\nLes deux méthodes n'ont pas complètement éliminé les biais.")
                    best_dataset = dataset_reweighed  # Par défaut, utiliser Reweighing
                else:
                    best_dataset = dataset_dir
            else:
                best_dataset = dataset_reweighed
            
            # Évaluation de l'impact sur un modèle
            print("\nÉvaluation de l'impact de la mitigation sur les performances du modèle...")
            acc_orig, acc_mitigated = evaluate_model(dataset, best_dataset, features, privileged_groups, unprivileged_groups)
            
            # Conclusion finale
            print("\n=== CONCLUSION FINALE ===")
            print(f"État initial: Dataset BIAISÉ avec {len(bias_reasons)} problème(s) identifié(s)")
            if acc_orig is not None and acc_mitigated is not None:
                print(f"Précision du modèle original: {acc_orig:.4f}")
                print(f"Précision du modèle après mitigation: {acc_mitigated:.4f}")
                print(f"Impact sur la précision: {(acc_mitigated - acc_orig):.4f} points")
            
        except Exception as e:
            print(f"Erreur lors de la mitigation: {e}")
            print("La mitigation n'a pas pu être effectuée correctement, possiblement en raison de la complexité des données.")
            print("Suggestion: Essayez de simplifier votre problème (par exemple, en rendant binaires certains attributs)")
            
    else:
        print("VERDICT: Le dataset n'est PAS BIAISÉ selon les critères d'équité analysés.")
        print("Aucune mitigation n'est nécessaire.")

if __name__ == "__main__":
    main()