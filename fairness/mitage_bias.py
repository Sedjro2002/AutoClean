import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from fairlearn.metrics import MetricFrame, count, selection_rate
from fairlearn.reductions import ExponentiatedGradient, DemographicParity
from fairlearn.metrics import demographic_parity_difference
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, accuracy_score
import seaborn as sns

class FairnessAnalyzer:
    def __init__(self, data, sensitive_features, target, features=None):
        self.data = data
        self.sensitive_features = sensitive_features
        self.target = target
        self.features = features
        
    def prepare_data(self):
        X = self.data[self.features] if self.features else self.data.drop(self.target, axis=1)
        y = self.data[self.target]
        
        scaler = StandardScaler()
        X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
        
        sensitive = self.data[self.sensitive_features]
        
        X_train, X_test, y_train, y_test, sensitive_train, sensitive_test = train_test_split(
            X_scaled, y, sensitive, test_size=0.2, random_state=42
        )
        
        return X_train, X_test, y_train, y_test, sensitive_train, sensitive_test
    
    def analyze_bias(self, predictor, X_test, y_test, sensitive_test):
        """
        Analyser les biais dans les prédictions du modèle
        
        Parameters:
        predictor: Un modèle ou une fonction de prédiction
        """
        # Faire des prédictions en tenant compte du type de predictor
        if hasattr(predictor, 'predict'):
            y_pred = predictor.predict(X_test)
        else:
            # Si c'est une fonction de prédiction directe
            y_pred = predictor(X_test)
        
        metrics = {
            'count': count,
            'selection_rate': selection_rate,
            'accuracy': accuracy_score
        }
        
        results = {}
        for sensitive_feature in self.sensitive_features:
            metric_frame = MetricFrame(
                metrics=metrics,
                y_true=y_test,
                y_pred=y_pred,
                sensitive_features=sensitive_test[sensitive_feature]
            )
            
            results[sensitive_feature] = {
                'overall': metric_frame.overall,
                'by_group': metric_frame.by_group,
                'demographic_parity': demographic_parity_difference(
                    y_test, y_pred, sensitive_features=sensitive_test[sensitive_feature]
                )
            }
            
        return results
    
    def mitigate_bias(self, X_train, y_train, sensitive_train, X_test, y_test, sensitive_test):
        """
        Appliquer la mitigation des biais en utilisant ExponentiatedGradient
        """
        results = {}
        mitigators = {}
        
        for sensitive_feature in self.sensitive_features:
            # Créer et entraîner le modèle original
            original_predictor = RandomForestClassifier(n_estimators=100, random_state=42)
            original_predictor.fit(X_train, y_train)
            
            # Créer et entraîner le mitigateur
            constraint = DemographicParity()
            mitigator = ExponentiatedGradient(
                estimator=RandomForestClassifier(n_estimators=100, random_state=42),
                constraints=constraint,
                eps=0.01
            )
            
            mitigator.fit(
                X_train,
                y_train,
                sensitive_features=sensitive_train[sensitive_feature]
            )
            
            # Stocker les résultats
            results[sensitive_feature] = {
                'original': self.analyze_bias(
                    original_predictor, X_test, y_test, sensitive_test
                )[sensitive_feature],
                'mitigated': self.analyze_bias(
                    mitigator.predict, X_test, y_test, sensitive_test
                )[sensitive_feature]
            }
            
            mitigators[sensitive_feature] = mitigator
            
        return results, mitigators
    
    




class FairnessImpactAnalyzer:
    def __init__(self, model, data, sensitive_features, target, features):
        self.model = model
        self.data = data
        self.sensitive_features = sensitive_features
        self.target = target
        self.features = features

    def analyze_predictions_by_group(self):
        """
        Analyser les prédictions pour chaque groupe sensible
        """
        # Faire les prédictions
        X = self.data[self.features]
        predictions = self.model.predict(X)
        
        results = {}
        for sensitive_feature in self.sensitive_features:
            # Grouper les prédictions par valeur de feature sensible
            grouped_results = pd.DataFrame({
                'true_values': self.data[self.target],
                'predictions': predictions,
                'group': self.data[sensitive_feature]
            }).groupby('group')
            
            # Calculer les métriques par groupe
            group_metrics = {}
            for group_name, group_data in grouped_results:
                tn, fp, fn, tp = confusion_matrix(
                    group_data['true_values'],
                    group_data['predictions']
                ).ravel()
                
                group_metrics[group_name] = {
                    'total_samples': len(group_data),
                    'positive_rate': (tp + fp) / len(group_data),
                    'true_positive_rate': tp / (tp + fn) if (tp + fn) > 0 else 0,
                    'false_positive_rate': fp / (fp + tn) if (fp + tn) > 0 else 0
                }
            
            results[sensitive_feature] = group_metrics
            
        return results

    def analyze_feature_importance(self):
        """
        Analyser l'importance indirecte des features sensibles
        """
        # Créer des variables dummy pour les features sensibles
        sensitive_dummies = pd.get_dummies(self.data[self.sensitive_features])
        
        # Calculer les corrélations avec les features utilisées
        correlations = pd.DataFrame()
        for feature in self.features:
            for sensitive_col in sensitive_dummies.columns:
                correlation = np.corrcoef(
                    self.data[feature],
                    sensitive_dummies[sensitive_col]
                )[0,1]
                correlations.loc[feature, sensitive_col] = correlation
        
        return correlations

    def plot_group_disparities(self, results):
        """
        Visualiser les disparités entre groupes
        """
        for sensitive_feature, metrics in results.items():
            # Créer un DataFrame pour la visualisation
            plot_data = pd.DataFrame(metrics).T
            
            # Créer plusieurs subplots
            fig, axes = plt.subplots(2, 2, figsize=(15, 10))
            fig.suptitle(f'Disparités pour {sensitive_feature}')
            
            # Plot 1: Taux de positifs
            plot_data['positive_rate'].plot(
                kind='bar',
                ax=axes[0,0],
                title='Taux de prédictions positives'
            )
            
            # Plot 2: True Positive Rate
            plot_data['true_positive_rate'].plot(
                kind='bar',
                ax=axes[0,1],
                title='Taux de vrais positifs'
            )
            
            # Plot 3: False Positive Rate
            plot_data['false_positive_rate'].plot(
                kind='bar',
                ax=axes[1,0],
                title='Taux de faux positifs'
            )
            
            # Plot 4: Distribution des échantillons
            plot_data['total_samples'].plot(
                kind='bar',
                ax=axes[1,1],
                title='Distribution des échantillons'
            )
            
            plt.tight_layout()
            return fig

    def analyze_conditional_outcomes(self):
        """
        Analyser les résultats conditionnels aux features sensibles
        """
        results = {}
        for sensitive_feature in self.sensitive_features:
            # Calculer les taux de succès conditionnels
            conditional_rates = {}
            for feature in self.features:
                # Créer des bins pour les features numériques
                bins = pd.qcut(self.data[feature], q=5)
                
                # Calculer les taux par groupe et bin
                rates = self.data.groupby([bins, sensitive_feature])[self.target].mean()
                conditional_rates[feature] = rates.unstack()
            
            results[sensitive_feature] = conditional_rates
            
        return results

def example_usage():
    # Créer des données synthétiques
    np.random.seed(42)
    n_samples = 1000
    
    # Simuler un biais dans les données
    data = pd.DataFrame({
        'income': np.random.normal(50000, 20000, n_samples),
        'credit_score': np.random.normal(700, 100, n_samples),
        'gender': np.random.choice(['M', 'F'], n_samples),
        'age_group': np.random.choice(['18-25', '26-35', '36-50', '50+'], n_samples),
    })
    
    # Introduire un biais: les revenus sont systématiquement plus bas pour certains groupes
    data.loc[data['gender'] == 'F', 'income'] *= 0.8
    
    # Créer une variable cible biaisée
    data['approved'] = (
        (data['income'] > 45000) & 
        (data['credit_score'] > 650)
    ).astype(int)
    
    # Configurer et utiliser l'analyseur
    analyzer = FairnessImpactAnalyzer(
        model=RandomForestClassifier().fit(
            data[['income', 'credit_score']], 
            data['approved']
        ),
        data=data,
        sensitive_features=['gender', 'age_group'],
        target='approved',
        features=['income', 'credit_score']
    )
    
    # Analyser l'impact
    group_results = analyzer.analyze_predictions_by_group()
    feature_importance = analyzer.analyze_feature_importance()
    conditional_outcomes = analyzer.analyze_conditional_outcomes()
    
    return group_results, feature_importance, conditional_outcomes    
    
    


def main():
    # Créer un dataset synthétique
    np.random.seed(42)
    n_samples = 1000
    
    #data = pd.DataFrame({
    #    'age': np.random.normal(35, 10, n_samples),
    #    'income': np.random.normal(50000, 20000, n_samples),
    #    'gender': np.random.choice(['M', 'F'], n_samples),
    #    'ethnicity': np.random.choice(['A', 'B', 'C'], n_samples),
    #    'approved': np.random.choice([0, 1], n_samples)
    #})
    
    data = pd.read_csv('german_credit_data.csv')
    
    # Configurer l'analyseur
    analyzer = FairnessAnalyzer(
        data=data,
        sensitive_features=['Sex'],
        target='Risk',
        #features=['age', 'income']
    )
    
    # Préparer les données
    X_train, X_test, y_train, y_test, sensitive_train, sensitive_test = analyzer.prepare_data()
    
    # Analyser et mitiger les biais
    results, mitigators = analyzer.mitigate_bias(
        X_train, y_train, sensitive_train,
        X_test, y_test, sensitive_test
    )
    
    # Afficher les résultats
    for feature, result in results.items():
        print(f"\nRésultats pour {feature}:")
        print("\nAvant mitigation:")
        print(f"Disparité démographique: {result['original']['demographic_parity']:.4f}")
        print("Métriques par groupe:")
        print(result['original']['by_group'])
        
        print("\nAprès mitigation:")
        print(f"Disparité démographique: {result['mitigated']['demographic_parity']:.4f}")
        print("Métriques par groupe:")
        print(result['mitigated']['by_group'])

if __name__ == "__main__":
    main()