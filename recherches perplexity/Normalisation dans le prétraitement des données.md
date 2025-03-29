
## Normalisation dans le prétraitement des données

La normalisation est une étape cruciale du prétraitement des données visant à **uniformiser l'échelle des caractéristiques** pour éviter les biais algorithmiques. Elle permet aux modèles d'apprentissage automatique de traiter équitablement toutes les variables, indépendamment de leurs unités de mesure initiales.

### Fondements mathématiques

Soit un ensemble de données $$
X = \{x_1, x_2, ..., x_n\}
$$ où chaque $$
x_i
$$ représente une observation avec $$
m
$$ caractéristiques. La normalisation transforme ces données selon :

$$
X' = \frac{X - \text{centrage}}{\text{échelle}}
$$

Trois stratégies principales existent dans `sklearn.preprocessing` :

---

## 1. StandardScaler() : Standardisation Z-Score

**Algorithme** : Centre les données sur la moyenne (μ=0) et les scale selon l'écart-type (σ=1).

**Implémentation** :

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler(
    with_mean=True,  # Activation du centrage
    with_std=True    # Activation du scaling
)
X_normalized = scaler.fit_transform(X)
```

**Mécanisme interne** :

- Calcule μ et σ pour chaque colonne
- Applique la transformation :

$$
x' = \frac{x - \mu}{\sigma}
$$
- Stocke μ et σ dans `scaler.mean_` et `scaler.scale_`

**Cas d'usage** :

- Données approximativement gaussiennes
- Comparaison de variables hétérogènes
- Prérequis pour PCA/SVM/Régression Logistique

---

## 2. MinMaxScaler() : Normalisation par plage

**Algorithme** : Projection linéaire des données dans l'intervalle[^1].

**Implémentation** :

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler(
    feature_range=(0, 1),  # Plage cible
    clip=False             # Désactive le clipping des outliers
)
X_normalized = scaler.fit_transform(X)
```

**Mécanisme interne** :

- Détermine min(x) et max(x) par colonne
- Applique :

$$
x' = \frac{x - \text{min}(x)}{\text{max}(x) - \text{min}(x)}
$$
- Stocke les paramètres dans `scaler.data_min_` et `scaler.data_max_`

**Cas d'usage** :

- Réseaux de neurones (entrées bornées)
- Données non-gaussiennes
- Visualisation de données hétérogènes

---

## 3. RobustScaler() : Standardisation robuste

**Algorithme** : Utilise des statistiques robustes aux outliers (médiane et IQR).

**Implémentation** :

```python
from sklearn.preprocessing import RobustScaler

scaler = RobustScaler(
    with_centering=True,   # Centrage sur la médiane
    with_scaling=True,     # Scaling par IQR
    quantile_range=(25.0, 75.0)  # Définition des quantiles
)
X_normalized = scaler.fit_transform(X)
```

**Mécanisme interne** :

- Calcule médiane $$
Q_{50}
$$ et écart interquartile $$
IQR = Q_{75} - Q_{25}
$$
- Transforme :
\$\$

x' = \frac{x - Q_{50}}{IQR}

\$\$
- Stocke $$
Q_{50}
$$ dans `scaler.center_` et $$
IQR
$$ dans `scaler.scale_`

**Cas d'usage** :

- Données avec outliers extrêmes
- Distributions asymétriques
- Données de mesures physiques bruitées
