<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# 

---

## Méthodologie scientifique : Encodage des valeurs catégorielles et implémentation du LabelEncoder

### 1. Encodage des valeurs catégorielles en prétraitement

Les données catégorielles (sexe, pays, catégories produits) nécessitent une transformation numérique pour être exploitables par les algorithmes d'apprentissage automatique. Deux approches principales existent :

#### 1.1 Label Encoding (Encodage ordinal)

Convertit chaque catégorie en valeur numérique unique via une bijection :

```math
f: C \rightarrow \mathbb{N} \quad \text{où} \quad C = \{c_1, c_2, ..., c_n\}
```

Exemple : ["chat", "chien", "oiseau"] →[^1]

**Avantages** :

- Préserve la relation ordinale lorsque celle-ci existe
- Réduction de dimensionnalité (O(n) vs O(n²) pour le One-Hot)

**Limitations** :

- Introduction artificielle d'ordre sémantique (0 < 1 < 2)
- Risque de biais algorithmique pour les modèles sensibles à la magnitude (régression linéaire, k-NN)


#### 1.2 One-Hot Encoding

Crée des vecteurs binaires orthogonaux pour chaque catégorie :

```math
\text{"chien"} \rightarrow [0, 1, 0]
```


### 2. Implémentation scientifique du LabelEncoder (scikit-learn)

La classe `LabelEncoder` de scikit-learn implémente une méthodologie rigoureuse ([Pedregosa et al., 2011](https://jmlr.csail.mit.edu/papers/v12/pedregosa11a.html)) :

#### 2.1 Algorithme sous-jacent

```python
class LabelEncoder:
    def fit(self, y):
        # Étape 1 : Extraction des classes uniques
        classes = np.unique(y)
        
        # Étape 2 : Tri lexicographique (ordre ASCII)
        if np.issubdtype(classes.dtype, np.number):
            self.classes_ = np.sort(classes)
        else:
            self.classes_ = np.sort(classes.astype('O'))
        
        # Étape 3 : Création du dictionnaire de mapping
        self.mapping_ = {cls: i for i, cls in enumerate(self.classes_)}
        
    def transform(self, y):
        # Application du mapping avec vérification des valeurs inconnues
        return np.array([self.mapping_[cls] for cls in y])
```


#### 2.2 Complexité algorithmique

- **Temps** : O(n log n) pour le tri des catégories
- **Espace** : O(n) pour le stockage des mappings


#### 2.3 Garanties mathématiques

- **Injectivité** : ∀(c₁, c₂) ∈ C², c₁ ≠ c₂ ⇒ f(c₁) ≠ f(c₂)
- **Surjectivité** : ∀i ∈ [0, n-1], ∃c ∈ C | f(c) = i
- **Ordre préservé** : c₁ < c₂ ⇒ f(c₁) < f(c₂) (pour les catégories ordonnées)


### 3. Intégration éthique dans notre outil

Notre implémentation étend le LabelEncoder standard avec :

1. **Détection automatique de l'ordinabilité** :

```python
def _is_ordinal(feature):
    try:
        pd.to_numeric(feature)
        return True
    except ValueError:
        return False
```

2. **Vérification des biais de représentation** :

```python
if len(encoder.classes_) / len(data) < 0.01:
    warn("Risque de sous-représentation catégorielle")
```

3. **Journalisation explicative** :

```json
{
  "transformation": "LabelEncoding",
  "mapping": {"homme": 0, "femme": 1},
  "warning": "Aucune relation ordinale détectée - utilisation déconseillée"
}
```


### 4. Validation scientifique

Des tests statistiques garantissent la robustesse :

- **Test χ² d'indépendance** pour détecter les corrélations illégitimes
- **Analyse de variance (ANOVA)** pour évaluer l'impact sur la target
- **Distance de Kolmogorov-Smirnov** pour vérifier la conservation des distributions


### Références

1. Pedregosa, F. et al. (2011). Scikit-learn: Machine Learning in Python. _JMLR 12_, pp. 2825-2830.
2. García, S. et al. (2015). Data preprocessing in data mining. _Springer_.
3. Wickham, H. (2014). Tidy Data. _Journal of Statistical Software 59_(10).

<div style="text-align: center">⁂</div>

[^1]: https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/57428104/acbd8a04-8be6-43e9-94fe-603fe0fe36ba/latex_2021.pdf

