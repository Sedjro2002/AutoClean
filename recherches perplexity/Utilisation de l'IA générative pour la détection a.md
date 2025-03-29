
## Utilisation de l'IA générative pour la détection automatique des colonnes sensibles et l'analyse de code

Dans le cadre de ce projet, nous avons exploité les capacités de l'IA générative pour automatiser deux tâches cruciales : la détection des colonnes sensibles dans un jeu de données et l'analyse du code de prétraitement pour identifier d'éventuels biais. Cette approche s'inscrit dans une démarche d'éthique et de transparence, visant à améliorer la qualité et la fiabilité des données utilisées dans les processus d'apprentissage automatique.

### Détection automatique des colonnes sensibles

Pour la détection des colonnes sensibles, nous avons implémenté un agent intelligent basé sur le modèle OpenAI, en utilisant le package Pydantic pour la validation et la sérialisation des données[^1]. L'agent est conçu pour évaluer chaque feature du dataset selon plusieurs critères de sensibilité :

1. **Type et contenu des données**
2. **Contexte au sein du jeu de données**
3. **Potentiel de révélation d'informations personnelles ou confidentielles**
4. **Risque de discrimination ou de biais**

L'agent attribue un score de sensibilité sur une échelle de 0 à 10, où 0-2 représente des informations non sensibles et publiques, tandis que 9-10 indique des données hautement sensibles présentant un risque élevé[^2]. Cette approche permet une évaluation nuancée et contextuelle de la sensibilité des données.

```python
class Feature(BaseModel):
    is_sensitive: bool = Field(..., description="Whether the feature is sensitive")
    sensibility_level: Annotated[
        int, Field(ge=0, le=10, description="The sensibility level of the feature")
    ]
    justification: str | None = Field(None, description="Justification if the feature is sensitive")
    recommendation: str | None = Field(None, description="Recommendation for handling the risk if the feature is sensitive")
```

L'utilisation de Pydantic pour définir le modèle `Feature` assure une structure cohérente et validée pour les résultats de l'analyse, facilitant ainsi leur interprétation et leur intégration dans le processus de prétraitement des données[^3].

### Analyse du code de prétraitement

Pour l'analyse du code de prétraitement, nous avons développé un analyseur de code basé sur l'IA, capable de détecter les biais potentiels et les problèmes éthiques dans les pipelines de traitement de données. Cette approche s'inspire des travaux récents sur l'utilisation de l'IA pour l'analyse statique de code[^4].

L'analyseur utilise un modèle de langage avancé, configuré avec un prompt système spécialisé :

```python
self.system_prompt = """You are an expert AI ethics advisor specializing in analyzing Python code for potential ethical biases. Your task is to:

1. Identify code sections that could introduce ethical biases in data processing or model training
2. Focus on:
   - Data filtering or selection that might exclude certain groups
   - Feature engineering that could amplify biases
   - Preprocessing steps that might disproportionately affect certain demographics
   - Direct or indirect use of sensitive attributes
   - Sampling methods that might not preserve demographic distributions
3. Provide specific line numbers and explanations for problematic code
4. Rate the overall sensitivity level from 0-10
5. Offer concrete recommendations for addressing the issues
6. Assess the severity of each finding (low, medium, high, critical)

Be thorough but avoid false positives. Focus on real ethical concerns rather than general code quality issues."""
```

Ce prompt guide l'IA pour effectuer une analyse approfondie du code, en se concentrant sur les aspects éthiques et les biais potentiels. L'analyseur produit des résultats structurés, incluant l'identification des sections problématiques, une explication détaillée des problèmes détectés, et des recommandations pour les résoudre[^5].

```python
class CodeBiasAnalysisResult(BaseModel):
    is_problematic: bool = Field(..., description="Whether the code contains potential ethical issues")
    sensitivity_level: int = Field(..., ge=0, le=10, description="The sensitivity level of the potential biases (0-10)")
    problematic_sections: List[CodeSection] = Field(..., description="List of problematic code sections with metadata")
    recommendations: List[str] = Field(..., description="List of recommendations for addressing the potential biases")
    severity: AnalysisSeverity = Field(..., description="Overall severity of the identified issues")
```

Cette approche permet une évaluation systématique et reproductible du code de prétraitement, contribuant ainsi à l'objectif global de transparence et d'éthique dans le traitement des données.

L'utilisation combinée de ces deux techniques - la détection des colonnes sensibles et l'analyse du code - offre une approche holistique pour identifier et atténuer les risques éthiques dans le processus de prétraitement des données. Cette méthodologie s'aligne sur les principes émergents de l'IA responsable et de l'éthique des données, contribuant à renforcer la confiance dans les systèmes d'apprentissage automatique[^6].[^1][^2][^3][^4][^5][^6]


[^1]: https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/57428104/3691e19c-a300-4643-848b-5a4fc5eed217/main.py

[^2]: https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/57428104/16fccc0d-da7c-4789-a876-831a5f0ca995/system_prompt.txt

[^3]: https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/57428104/464fd1a5-f3a8-4f85-9a54-5587fe5739c0/ai_code_analyzer.py

[^4]: https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/57428104/bafe9c2f-4318-4eeb-a802-e719548456b2/latex_2021.pdf

[^5]: https://arxiv.org/abs/2407.10413

[^6]: https://www.tonic.ai/guides/custom-sensitivity-rules-to-automate-sensitive-data-detection

[^7]: https://www.infoq.com/news/2024/12/pydanticai-framework-gen-ai/

[^8]: https://www.semanticscholar.org/paper/9fcf9afededfde2abf8a72f3cf5fef8c51ca07df

[^9]: https://www.semanticscholar.org/paper/36077dd7fd03c85e4b7a06f57cee74be70274d77

[^10]: https://www.egnyte.com/solutions/sensitive-content-classification

[^11]: https://www.semanticscholar.org/paper/79ef552aae7b0edeef45c3a6e76e95896735a434

[^12]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11851526/

[^13]: https://www.semanticscholar.org/paper/b4b6d6a50392f310b6dfd4b5e403e971a3fc4c65

[^14]: https://arxiv.org/abs/2501.19172

[^15]: https://www.sciencedaily.com/releases/2024/07/240709184208.htm

[^16]: https://news.mit.edu/2024/mit-researchers-introduce-generative-ai-databases-0708

[^17]: https://cloud.google.com/blog/products/identity-security/how-sensitive-data-protection-can-help-secure-generative-ai-workloads

[^18]: https://arxiv.org/abs/2503.06054

[^19]: https://arxiv.org/abs/2502.17360

[^20]: https://www.semanticscholar.org/paper/5457cf0fc58ee5a0b2cc8a847bf7141fc2c57c7d

[^21]: https://www.semanticscholar.org/paper/6fef5a1221beacd07464694f99fd4acd19ba1cdf

[^22]: https://www.capitalone.com/tech/open-source/sensitive-data-detection-with-data-profiler/

[^23]: https://stackoverflow.blog/2023/10/23/privacy-in-the-age-of-generative-ai/

[^24]: https://www.isaca.org/resources/news-and-trends/isaca-now-blog/2023/using-machine-learning-to-help-detect-sensitive-information

[^25]: https://www.route-fifty.com/cybersecurity/2023/11/how-use-generative-ai-improve-operations-while-protecting-sensitive-data/392341/

[^26]: https://blog.developer.adobe.com/using-machine-learning-to-help-detect-sensitive-information-5bfb32eeb34e?gi=007f3ef30099

[^27]: https://bigid.com/blog/5-ways-generative-ai-improves-data-privacy/

[^28]: https://www.rubrik.com/blog/technology/23/12/guide-to-ai-driven-data-discovery-and-classification

[^29]: https://blogs.idc.com/2023/05/05/generative-ai-mitigating-data-security-and-privacy-risks/

[^30]: https://www.veeam.com/blog/ai-data-security.html

[^31]: https://www.techtarget.com/searchbusinessanalytics/tip/Generative-AI-capabilities-increase-data-analytics-value

[^32]: https://pii-tools.com/ai-in-sensitive-data-management/

[^33]: https://www.infosecurity-magazine.com/news/sensitive-data-sharing-genai/

[^34]: https://www.helpnetsecurity.com/2021/09/22/identify-sensitive-data/

[^35]: https://towardsdatascience.com/using-generative-ai-to-get-insights-from-disorderly-data-af056e5910eb/?gi=10e35b709da8

[^36]: https://www.semanticscholar.org/paper/2d947740b3e6a4ffd71190e8c4c287f24b3279c5

[^37]: https://arxiv.org/abs/2401.06795

[^38]: https://pubmed.ncbi.nlm.nih.gov/39132828/

[^39]: https://www.semanticscholar.org/paper/d08e39c09453cfa3c1c48541f4a5095f03f4b7e6

[^40]: https://www.andrew.cmu.edu/user/ales/cib/bias_in_gen_ai.pdf

[^41]: https://www.bitrue.com/blog/what-is-pydantic-ai

[^42]: https://cte.ku.edu/addressing-bias-ai

[^43]: https://www.brookings.edu/articles/algorithmic-bias-detection-and-mitigation-best-practices-and-policies-to-reduce-consumer-harms/

[^44]: https://indatalabs.com/blog/generative-ai-bias

[^45]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10287014/

[^46]: https://www.techtarget.com/searchenterpriseai/feature/How-to-detect-bias-in-existing-AI-algorithms

[^47]: https://www.pwc.com/us/en/tech-effect/ai-analytics/algorithmic-bias-and-trust-in-ai.html

[^48]: https://www.mckinsey.com/featured-insights/artificial-intelligence/tackling-bias-in-artificial-intelligence-and-in-humans

[^49]: https://www.techtarget.com/searchenterpriseai/definition/machine-learning-bias-algorithm-bias-or-AI-bias

[^50]: https://arxiv.org/abs/2403.02726

[^51]: https://arxiv.org/html/2310.18834v2

[^52]: https://www.brookings.edu/articles/detecting-and-mitigating-bias-in-natural-language-processing/

[^53]: https://dev.to/devsatasurion/the-good-the-bad-and-the-biased-is-bias-in-generative-ai-a-flaw-or-a-feature-57go

[^54]: https://www.semanticscholar.org/paper/b891a5aedb15d47c32b4de72c1b112e4aa9abfa2

[^55]: https://www.semanticscholar.org/paper/311a9da861c81ae1a81a920f255409f4e6fab7f1

[^56]: https://arxiv.org/abs/2401.12970

[^57]: https://www.semanticscholar.org/paper/745a4df6fab28f0a629e864901b9f316c8b9e554

[^58]: https://www.semanticscholar.org/paper/505d2586f3c78e9d850c745377ec23c7caa623d9

[^59]: https://www.rws.com/artificial-intelligence/train-ai-data-services/blog/address-bias-with-generative-ai-data-explainability/

[^60]: https://patents.google.com/patent/US11301245B2/en

[^61]: https://www.infosys.com/services/incubating-emerging-technologies/documents/managing-biasness-generative-ai.pdf

[^62]: https://sdtimes.com/test/addressing-ai-bias-in-ai-driven-software-testing/

[^63]: https://mostly.ai/blog/data-bias-types

[^64]: https://builtin.com/data-science/auditing-algorithms-data-science-bias

