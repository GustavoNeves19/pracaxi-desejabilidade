# 📒 Análise Exploratória e Modelagem Preditiva: Extração de Compostos Bioativos do Pracaxi

Este notebook concentra a análise exploratória, estatística e modelagem preditiva baseada em experimentos realizados para extração de compostos bioativos do Pracaxi. Os dados foram analisados com foco em **modelos polinomiais de segunda ordem**, com atenção à significância estatística, interpretação química e aplicação prática no contexto laboratorial.

---

## 🎯 Objetivos Técnicos

- Analisar e tratar dados experimentais com base em variáveis contínuas: **tempo de extração**, **concentração de etanol** e **razão sólido-líquido**.
- Desenvolver **modelos de regressão polinomial** para prever as respostas:
  - `TPC` – Compostos Fenólicos Totais
  - `TF` – Teores de Flavonoides
  - `ABTS` – Atividade Antioxidante (método ABTS)
- Identificar **efeitos lineares, quadráticos e de interação** com base na ANOVA.
- Interpretar estatisticamente os coeficientes para embasar recomendações científicas.
- Simular superfícies de resposta com foco em regiões ótimas (potencial para design de experimentos).

---

## 🔍 Estratégias de Modelagem

- **Construção de fórmulas estatísticas** com `ols` do `statsmodels`, combinando:
  - Termos quadráticos: `I(x**2)`
  - Interações cruzadas: `x1:x2`
- **Avaliação dos modelos com ANOVA** (`sm.stats.anova_lm`) e p-valores para determinar a significância de cada fator.
- Análise da **interpretação dos coeficientes estimados**, com embasamento químico.
- Comparação dos modelos obtidos com fórmulas propostas em literatura científica.

---

## 📊 Ferramentas e Bibliotecas Utilizadas

- `pandas`, `numpy` – manipulação e análise de dados
- `matplotlib`, `seaborn`, `plotly` – visualizações estáticas e interativas
- `statsmodels` – regressão e ANOVA

---

## 📊 Análise Comparativa

| Métrica        | Valor no Artigo | Valor Estimado | Erro Absoluto | Erro Percentual (%) |
|----------------|------------------|----------------|----------------|----------------------|
| **TPC**        | 0.738            | 0.7311         | 0.0069         | 0.93%                |
| **TF**         | 0.023            | 0.020801       | 0.002199       | 9.56%                |
| **ABTS**       | 100              | 100.0593       | 0.0593         | 0.06%                |

> 🔎 *Conclusão:* Os valores obtidos pelo modelo mostraram excelente proximidade com os resultados experimentais do artigo, especialmente para ABTS e TPC. O maior desvio observado foi para o TF, com cerca de 9.56% de diferença, ainda dentro de uma faixa aceitável para estudos exploratórios de otimização. O modelo, portanto, demonstra **boa capacidade preditiva** e **aplicabilidade prática** na avaliação do potencial da biomassa de pracaxi.

---

## 📁 Estrutura dos Dados

Os dados utilizados estão disponíveis na pasta `../data/`, contendo:

- `dados_experimento.xlsx`: dados brutos da bancada
- `df_tratado.csv`: dados organizados e tratados para modelagem estatística

---

## ▶️ Como executar

1. Acesse o projeto:
```bash
cd projeto_pracaxi
```

2. Execute o notebook:
```bash
jupyter notebook notebooks/Projeto_Extracao_Pracaxi.ipynb
```

---

## 🧠 Autor

Gustavo Neves da Paz Rafael
  
Cientista de dados em formação | Grupo de Pesquisa em IA e Simulação Aplicado à Ciência de Alimentos (UFRA)

---

## 📚 Base Científica

> *Optimization of bioactive compound extraction from pracaxi residues by ultrasound-assisted process*

Este notebook complementa a aplicação final em `Streamlit`, servindo como base teórica, exploratória e de validação estatística dos modelos utilizados.

