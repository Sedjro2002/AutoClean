# MATERIEL ET METHODES

Cette section présente en détail l'environnement technique, les outils et les méthodes utilisés pour développer FairAutoClean, un outil de prétraitement automatique et éthique des données.

## MATERIEL

### Analyse des besoins fonctionnels et techniques

#### Analyse des besoins fonctionnels

Le développement de FairAutoClean répond à plusieurs besoins fonctionnels essentiels :

1. **Prétraitement automatique et efficient des données**
    Il a pour objectif de nettoyer les données en supprimant les doublons, en gérant les valeurs manquantes, en détectant et en traitant les valeurs aberrantes, en détectant et en convertissant les colonnes de date, en encodant les colonnes catégoriques et en normalisant les colonnes numériques.
   - **Suppression des doublons** : Identification et élimination des enregistrements redondants pour garantir l'unicité des données
   - **Gestion des valeurs manquantes** : Implémentation de plusieurs stratégies :
     - Imputation par régression pour les données numériques
     - Imputation KNN pour préserver les relations entre variables
     - Suppression intelligente des lignes avec trop de valeurs manquantes
   - **Gestion des valeurs aberrantes** :
     - Détection par la méthode IQR (Inter-Quartile Range)
     - Traitement par winsorisation pour limiter l'impact des valeurs extrêmes
   - **Détection et conversion des colonnes de date** :
     - Identification automatique des formats de date
     - Standardisation des formats temporels
   - **Encodage des colonnes catégoriques** :
     - Label Encoding pour les variables ordinales
     - One-Hot Encoding pour les variables nominales
   - **Normalisation des colonnes numériques** :
     - Standardisation (moyenne=0, écart-type=1)
     - Min-Max Scaling
     - Robust Scaling pour les données avec outliers

2. **Réduction de dimension des données**
   - **PCA (Principal Component Analysis)** :
     - Réduction de la dimensionnalité tout en préservant la variance
     - Configuration du nombre de composantes ou du pourcentage de variance à conserver
   - **Autoencoders** :
     - Réduction non-linéaire de la dimensionnalité
     - Architecture adaptative selon la complexité des données

3. **Détection automatique des colonnes sensibles**
   - **Détection algorithmique** :
     - Utilisation de listes de mots-clés prédéfinis
     - Analyse des patterns dans les noms de colonnes
   - **Détection par IA** :
     - Utilisation de modèles de langage (LLM) pour l'analyse contextuelle
     - Évaluation du niveau de sensibilité sur une échelle de 0 à 10

4. **Détection des biais algorithmiques**
   - **Analyse syntaxique du code** :
     - Identification des patterns de code potentiellement discriminatoires
     - Vérification des opérations de filtrage et de sélection
   - **Analyse par IA** :
     - Utilisation de LLM pour évaluer les implications éthiques du code
     - Génération de recommandations pour l'amélioration du code

5. **Visualisation et audit**
   - **Exploratory Data Analysis (EDA)** :
     - Génération de rapports de profiling détaillés
     - Visualisations statistiques des distributions
   - **Traçabilité** :
     - Journalisation détaillée des opérations effectuées
     - Rapport d'audit complet avec métriques de performance

#### Analyse des besoins techniques

1. **Langage de programmation**
   - Python choisi pour :
     - Sa richesse en bibliothèques de data science
     - Sa communauté active
     - Sa facilité d'intégration avec les outils d'IA

2. **Environnement de développement**
   - IDE moderne avec support Python
   - Outils de versioning (Git)
   - Environnement virtuel pour la gestion des dépendances

3. **Bibliothèques essentielles**
   - Pandas pour la manipulation des données
   - Scikit-learn pour le prétraitement
   - TensorFlow/Keras pour les autoencoders
   - AI Fairness 360 pour l'analyse des biais
   - Loguru pour la journalisation
   - Pydantic pour la validation des données

4. **Infrastructure**
   - Support multi-plateforme (Windows, Linux, macOS)
   - Gestion des dépendances via pip
   - Configuration via fichiers JSON

### Environnement technique

1. **Configuration matérielle**
   - Ordinateur portable HP laptop 14s-dq2395nia
   - Processeur : 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz
   - RAM : 16,0 Go
   - Système d'exploitation : Windows 11

2. **Environnement logiciel**
   - VSCode comme IDE principal
   - Python 3.8+ comme langage de développement
   - Git pour le contrôle de version
   - Environnement virtuel Python pour l'isolation des dépendances

## METHODES

### Architecture logicielle

L'architecture de FairAutoClean est conçue de manière modulaire pour assurer la maintenabilité et l'extensibilité du système.

1. **Structure générale**
   - Architecture en couches avec séparation claire des responsabilités
   - Modules indépendants et réutilisables
   - Interface unifiée via le module `interface.py`

2. **Composants principaux**
   - **AutoClean** : Classe principale gérant le pipeline de nettoyage
   - **DataProcessor** : Gestion du chargement et du prétraitement des données
   - **FairnessAnalyzer** : Analyse et mitigation des biais
   - **AICodeAnalyzer** : Analyse éthique du code source
   - **ReportGenerator** : Génération des rapports d'audit

3. **Flux de données**

   ```mermaid
   flowchart TB
    subgraph Input
        IN[Data Input]
        CFG[Configuration Input]:::config
    end

    subgraph Core[Core Processing Layer]
        DP[Data Processor]:::core
        DC[Data Cleaner]:::core
        NM[Normalizer]:::core
        DR["Dimension Reduction"]:::core
        FE["Feature Engineering"]:::core
    end

    subgraph Fair[Fairness & Analysis Layer]
        FA[Fairness Analyzer]:::fairness
        CA[Code Analyzer]:::fairness
        AS[Audit System]:::fairness
    end

    subgraph Interface[Interface Layer]
        CLI[CLI Interface]:::interface
        PKG[Python Package]:::interface
        CM[Configuration Management]:::interface
    end

    subgraph AI[AI Agent System]
        LLM[LLM Integration]:::ai
        SPH[System Prompt Handler]:::ai
    end

    subgraph Output[Output & Reporting]
        RG[Report Generator]:::output
        PG[Profile Generator]:::output
        AT[Audit Trail Generator]:::output
        
        subgraph Files[Output Files]
            AD[Audit Trail]:::file
            FR[Fairness Results]:::file
            CD[Cleaned Data]:::file
            PR[Profile Report]:::file
        end
    end

    IN --> CLI
    IN --> PKG
    CFG --> CM

    CLI --> DP
    PKG --> DP
    CM --> DP

    DP --> DC
    DC --> NM
    NM --> DR
    DR --> FE

    FE --> FA
    FA --> CA
    CA --> AS

    LLM --> FA
    LLM --> CA
    SPH --> LLM

    FA --> RG
    CA --> RG
    AS --> AT

    RG --> PG
    RG --> Files
    AT --> AD
    PG --> PR
    FA --> FR
    DC --> CD

    %% Click Events
    click DP "https://github.com/Sedjro2002/AutoClean/blob/main/AutoClean/data_processor.py"
    click DC "https://github.com/Sedjro2002/AutoClean/blob/main/AutoClean/datacleaner.py"
    click NM "https://github.com/Sedjro2002/AutoClean/blob/main/AutoClean/normalizer.py"
    click DR "https://github.com/Sedjro2002/AutoClean/blob/main/AutoClean/dim_reduction.py"
    click FE "https://github.com/Sedjro2002/AutoClean/blob/main/preprocessing/feature_engineering.py"
    click FA "https://github.com/Sedjro2002/AutoClean/blob/main/AutoClean/fairness_analyzer.py"
    click CA "https://github.com/Sedjro2002/AutoClean/blob/main/AutoClean/ai_code_analyzer.py"
    click AS "https://github.com/Sedjro2002/AutoClean/blob/main/AutoClean/audit.py"
    click CLI "https://github.com/Sedjro2002/AutoClean/blob/main/AutoClean/cli.py"
    click CM "https://github.com/Sedjro2002/AutoClean/blob/main/AutoClean/config.py"
    click LLM "https://github.com/Sedjro2002/AutoClean/blob/main/AutoClean/ai_agent/main.py"
    click SPH "https://github.com/Sedjro2002/AutoClean/blob/main/AutoClean/ai_agent/system_prompt.txt"
    click RG "https://github.com/Sedjro2002/AutoClean/blob/main/AutoClean/report_generator.py"
    click Files "https://github.com/Sedjro2002/AutoClean/tree/main/AutoClean/output"
    click AD "https://github.com/Sedjro2002/AutoClean/blob/main/output/audit_trail.json"
    click FR "https://github.com/Sedjro2002/AutoClean/blob/main/output/fairness_results.json"
    click CD "https://github.com/Sedjro2002/AutoClean/blob/main/output/cleaned_data.csv"
    click PR "https://github.com/Sedjro2002/AutoClean/blob/main/AutoClean/output/comparative_profile.html"

    %% Styling
    classDef core fill:#a8d1f0,stroke:#333
    classDef fairness fill:#90EE90,stroke:#333
    classDef interface fill:#FFE5B4,stroke:#333
    classDef ai fill:#FFB6C1,stroke:#333
    classDef output fill:#DDA0DD,stroke:#333
    classDef config fill:#F0E68C,stroke:#333
    classDef file fill:#E6E6FA,stroke:#333

    %% Legend
    subgraph Legend
        L1[Core Processing]:::core
        L2[Fairness Components]:::fairness
        L3[Interface Components]:::interface
        L4[AI Components]:::ai
        L5[Output Components]:::output
        L6[Configuration]:::config
        L7[Files]:::file
    end
   ```

### Implémentation détaillée des fonctionnalités

1. **Prétraitement des données (`modules.py`)**

   a. **Gestion des valeurs manquantes** :

   ```python
   class MissingValues:
       def handle(self, df, _n_neighbors=3):
           # Stratégies d'imputation :
           # - Régression linéaire pour données numériques
           # - Régression logistique pour données catégorielles
           # - KNN avec k=3 par défaut
           # - Imputation simple (moyenne, médiane, mode)
   ```

   b. **Encodage des variables catégorielles** :
   - Conversion automatique des booléens
   - Détection et conversion des valeurs numériques
   - Label Encoding pour variables ordinales
   - One-Hot Encoding pour variables nominales

2. **Analyse d'équité (`fairness_analyzer.py`)**

   a. **Détection des attributs sensibles** :

   ```python
   def _detect_sensitive_features(self):
       # Utilisation de l'IA pour détecter les colonnes sensibles
       # Évaluation du niveau de sensibilité (0-10)
       # Génération de justifications et recommandations
   ```

   b. **Métriques d'équité** :
   - Disparate Impact
   - Statistical Parity Difference
   - Métriques par groupe démographique

   c. **Mitigation des biais** :
   - Repondération des échantillons
   - Transformation des features
   - Validation des résultats

3. **Analyse du code (`ai_code_analyzer.py`)**

   a. **Analyse statique** :

   ```python
   class CodeBiasAnalyzer:
       BIAS_INDICATORS = {
           'data_filtering': {
               'keywords': ['filter', 'drop', 'remove', 'exclude'],
               'risk': 'Selection bias through data filtering'
           },
           'feature_engineering': {
               'keywords': ['encode', 'transform', 'normalize'],
               'risk': 'Potential encoding bias'
           }
       }
   ```

   b. **Analyse par IA** :
   - Intégration avec des LLM via OpenAI API
   - Analyse contextuelle du code
   - Génération de recommandations éthiques

4. **Réduction de dimension (`dim_reduction.py`)**

   a. **PCA** :
   - Calcul adaptatif du nombre de composantes
   - Préservation de la variance expliquée
   - Normalisation préalable des données

   b. **Autoencoder** :

   ```python
   class AutoEncoder(keras.Model):
       def __init__(self, input_dim, encoding_dim):
           # Architecture :
           # - Couche d'entrée (input_dim)
           # - Couches cachées (encoding_dim * 2)
           # - Couche latente (encoding_dim)
   ```

5. **Audit et traçabilité (`audit.py`)**

   a. **Structure des logs** :

   ```python
   @dataclass
   class OperationMetrics:
       start_time: str
       end_time: str
       duration_seconds: float
       input_shape: tuple
       output_shape: tuple
       changes_made: Dict[str, Any]
       success: bool
   ```

   b. **Métriques collectées** :
   - Durée des opérations
   - Changements effectués
   - Statistiques avant/après
   - Erreurs et avertissements

### Interface et utilisation

1. **Interface en ligne de commande (`cli.py`)**

   ```python
   def main():
       parser.add_argument('--config', type=str, required=True)
       parser.add_argument('--dataset', type=str, required=True)
       parser.add_argument('--output', type=str, required=True)
   ```

2. **Configuration JSON** :

   ```json
   {
       "dataset_config": {
           "sensitive_features": ["gender", "race"],
           "target": "outcome",
           "preprocessing": {
               "normalization": {
                   "enabled": true,
                   "method": "standard"
               }
           }
       }
   }
   ```

3. **Pipeline de traitement (`interface.py`)**

   ```python
   def process_dataset(config_path, dataset_path, output_path):
       # 1. Chargement et validation de la configuration
       # 2. Prétraitement des données
       # 3. Analyse d'équité
       # 4. Génération des rapports
       # 5. Sauvegarde des résultats
   ```

Cette implémentation détaillée montre comment les différents composants s'articulent pour former un système cohérent de prétraitement équitable des données.

[Suite dans la prochaine partie...]
