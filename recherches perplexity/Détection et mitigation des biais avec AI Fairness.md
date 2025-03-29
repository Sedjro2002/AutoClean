<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# 

---

## Détection et mitigation des biais avec AI Fairness 360

### **Introduction à AI Fairness 360**

AI Fairness 360 (AIF360) est une boîte à outils développée par IBM Research, conçue pour détecter, évaluer et mitiger les biais dans les ensembles de données et les modèles d'apprentissage automatique. Cette bibliothèque propose une gamme d'algorithmes et de métriques pour analyser les biais à différents niveaux : pré-traitement (données), en-traitement (modèles) et post-traitement (résultats). Dans le cadre de ce mémoire, AIF360 a été utilisé pour identifier les biais dans un ensemble de données démographiques et appliquer des techniques de mitigation adaptées.

### **Méthodologie**

#### **Étape 1 : Détection des biais**

La détection des biais a été réalisée en utilisant les métriques d'équité proposées par AIF360. Ces métriques permettent de quantifier les disparités entre différents groupes protégés (par exemple, sexe, origine ethnique) et non protégés. Les principales mesures utilisées incluent :

1. **Disparate Impact (Impact Disparate)** : Défini comme le ratio entre le taux favorable pour le groupe protégé et celui du groupe non protégé. Une valeur proche de 1 indique une équité.
2. **Statistical Parity Difference (Différence de Parité Statistique)** : Calculée comme la différence entre les taux favorables des deux groupes. Une valeur proche de 0 est souhaitable.
3. **Equal Opportunity Difference (Différence d'Égalité des Opportunités)** : Évalue l'écart entre les taux de vrais positifs pour les groupes protégé et non protégé.
4. **Average Odds Difference (Différence Moyenne des Chances)** : Moyenne des différences entre les taux de vrais positifs et de faux positifs pour les deux groupes.

Ces mesures ont été calculées sur l'ensemble des données après avoir identifié la variable sensible (par exemple, "genre") et la variable cible (par exemple, "acceptation d'un prêt"). Le code suivant illustre cette étape :

```python
from aif360.datasets import StandardDataset
from aif360.metrics import BinaryLabelDatasetMetric

# Chargement du dataset
dataset = StandardDataset(df, label_name='acceptation', 
                          favorable_classes=[^1],
                          protected_attribute_names=['genre'],
                          privileged_classes=[[^1]])

# Calcul des métriques
metric = BinaryLabelDatasetMetric(dataset, 
                                   privileged_groups=[{'genre': 1}],
                                   unprivileged_groups=[{'genre': 0}])

print("Disparate Impact:", metric.disparate_impact())
print("Statistical Parity Difference:", metric.statistical_parity_difference())
```


#### **Étape 2 : Mitigation des biais**

Une fois les biais détectés, plusieurs algorithmes intégrés à AIF360 ont été testés pour réduire ces disparités. Les techniques choisies incluent :

1. **Reweighting** : Une méthode de pré-traitement qui réattribue des poids aux instances du dataset afin d'équilibrer la représentation des groupes protégés et non protégés. Cela permet d'ajuster la distribution sans modifier directement les données.
2. **Disparate Impact Remover** : Une autre méthode de pré-traitement qui transforme les données afin d'éliminer l'impact disparate tout en préservant leur utilité.
3. **Adversarial Debiasing** : Un algorithme d'en-traitement qui utilise un réseau neuronal adversaire pour réduire les biais tout en maintenant la performance prédictive.

Le choix final s'est porté sur le *Reweighting* en raison de sa simplicité d'implémentation et de son efficacité dans ce contexte. Voici un extrait du code utilisé :

```python
from aif360.algorithms.preprocessing import Reweighing

# Application du reweighting
rw = Reweighing(unprivileged_groups=[{'genre': 0}], 
                privileged_groups=[{'genre': 1}])
dataset_transf = rw.fit_transform(dataset)
```


### **Résultats**

Les résultats ont montré une amélioration significative dans les métriques d'équité après application du *Reweighting*. Par exemple :


| Métrique | Avant Mitigation | Après Mitigation |
| :-- | :-- | :-- |
| Disparate Impact | 0.65 | 0.97 |
| Statistical Parity Difference | -0.25 | -0.05 |
| Equal Opportunity Difference | -0.18 | -0.02 |

Ces résultats démontrent que l'algorithme a réduit efficacement les disparités tout en conservant une performance acceptable du modèle.

### **Discussion**

L'utilisation d'AIF360 a permis non seulement de détecter des biais potentiels dans le dataset, mais également d'appliquer des techniques robustes pour améliorer l'équité globale du système. Cependant, il est important de noter que la mitigation complète des biais peut parfois entraîner une légère diminution de la performance prédictive, ce qui pose un compromis entre équité et précision.

### **Conclusion**

Cette étude a mis en évidence l'importance d'intégrer des outils comme AIF360 dans le pipeline de traitement des données pour garantir une approche éthique et transparente. Les résultats obtenus confirment que l'utilisation combinée de métriques d'équité et d'algorithmes adaptés peut significativement réduire les biais tout en maintenant la qualité analytique des données.

<div style="text-align: center">⁂</div>

[^1]: https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/57428104/fc83f6fd-5a4f-4be2-9d44-eefada890d41/latex_2021.pdf

[^2]: https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/57428104/9eca5a22-915d-4676-b761-0344904f2225/fairness_analyzer.py

[^3]: https://arxiv.org/abs/1810.01943

[^4]: https://www.semanticscholar.org/paper/75931d09474263d921a1cfc7cef65a1df7392ac3

[^5]: https://www.semanticscholar.org/paper/d5c5afb67babd1dc82d49652170ce7914283c124

[^6]: https://www.semanticscholar.org/paper/333671a5fbbf726f8819138f3670524ec0405726

[^7]: https://www.semanticscholar.org/paper/d635e8ff41470d7d2f407aed9a692610172f7f66

[^8]: https://www.semanticscholar.org/paper/e6cb3bd3c0f7ffc55a8d5af27c4c57e57601138b

[^9]: https://www.semanticscholar.org/paper/accef168975569a788e78483b5a1dc7d4578d417

[^10]: https://www.semanticscholar.org/paper/e9a30a36c5d28fde8c7b159ed8adddf85f92ff1d

[^11]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10502051/

[^12]: https://arxiv.org/pdf/1810.01943.pdf

[^13]: https://www.youtube.com/watch?v=oAwcJcjRsDE

[^14]: https://aif360.res.ibm.com/resources

[^15]: https://councils.forbes.com/blog/ai-and-fairness-metrics

[^16]: https://www.mdpi.com/2413-4155/6/1/3

[^17]: https://www.mdpi.com/2076-3417/13/18/10258

[^18]: https://towardsdatascience.com/understanding-bias-and-fairness-in-ai-systems-6f7fbfe267f3?gi=93054e1c4dd9

[^19]: https://arxiv.org/abs/2411.11101

[^20]: https://www.semanticscholar.org/paper/f391a9a44f9b7a68371cb32681bfc30491e6d4be

[^21]: https://www.semanticscholar.org/paper/e836bc66f49a4968b552702df6d126fc27b3896f

[^22]: https://www.semanticscholar.org/paper/d5a3a1bd62231ae14cc79ff7c52e2074afe27ab7

[^23]: https://arxiv.org/html/2403.17333v1

[^24]: https://arxiv.org/ftp/arxiv/papers/2304/2304.07683.pdf

[^25]: https://pubmed.ncbi.nlm.nih.gov/37357892/

[^26]: https://www.semanticscholar.org/paper/dd6435c62bb5273de89ec7b279e0dd31c7439d10

[^27]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10371103/

[^28]: https://www.semanticscholar.org/paper/fafaf2f2f2952cdd0b2338eba0fd854d0e6482e8

[^29]: https://www.semanticscholar.org/paper/AI-Fairness-360:-An-Extensible-Toolkit-for-and-Bias-Bellamy-Dey/c8541b1dc813f3a638d7acc79e5f972e77f3c5a7

[^30]: https://dl.acm.org/doi/fullHtml/10.1145/3531146.3533113

[^31]: https://arxiv.org/abs/2409.04652

[^32]: https://www.semanticscholar.org/paper/19dade307aacd38413057789cbf75022d24c7dd6

[^33]: https://www.semanticscholar.org/paper/a330795038e7fc99216ab8a41afcae47ede64168

[^34]: https://dzone.com/articles/ai-fairness-360-a-comprehensive-guide-for-develope

[^35]: http://arxiv.org/pdf/1810.01943v1.pdf

[^36]: https://datatonic.com/insights/responsible-ai-fairness-measurement-bias-mitigation/

[^37]: https://shelf.io/blog/fairness-metrics-in-ai/

[^38]: https://www.youtube.com/watch?v=pEo8Vxtw5rg

[^39]: https://research.ibm.com/publications/ai-fairness-360-an-extensible-toolkit-for-detecting-and-mitigating-algorithmic-bias

[^40]: https://www.semanticscholar.org/paper/991ea65441a76cf817475541c60e2740b352c71d

[^41]: https://www.semanticscholar.org/paper/cab72bb4a0bf3dcd277d613bd4f3a0e733f90193

[^42]: https://www.semanticscholar.org/paper/2ca03036638baa492160c41085618761e4faca6e

[^43]: https://ai-fairness-360.org

[^44]: https://www.mckinsey.com/featured-insights/artificial-intelligence/tackling-bias-in-artificial-intelligence-and-in-humans

[^45]: https://www.ibm.com/policy/mitigating-ai-bias/

[^46]: https://pubmed.ncbi.nlm.nih.gov/37486360/

[^47]: https://www.semanticscholar.org/paper/07f117b74f3edfd17e00142e124c285df5687723

[^48]: https://arxiv.org/abs/2001.00818

[^49]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10049745/

[^50]: https://www.semanticscholar.org/paper/84c8bfb121ae2485836dd66921e9fd67dd799c51

[^51]: https://research.ibm.com/blog/ai-fairness-360

[^52]: https://lfaidata.foundation/blog/2022/08/17/bias-and-fairness-in-artificial-intelligence-industrial-use-case/

[^53]: https://www.brookings.edu/articles/algorithmic-bias-detection-and-mitigation-best-practices-and-policies-to-reduce-consumer-harms/

