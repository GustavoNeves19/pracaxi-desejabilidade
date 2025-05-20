# 📒 Notebook: Projeto de Extração de Compostos Bioativos do Pracaxi

Este notebook contém toda a análise estatística e a modelagem preditiva realizada com base nos dados experimentais da extração de compostos bioativos do Pracaxi, utilizando diferentes condições de tempo, concentração de etanol e razão sólido-líquido.

---

## 📌 Objetivos

- Realizar o tratamento e limpeza dos dados experimentais
- Aplicar modelos polinomiais de regressão para prever:
  - TPC (Compostos Fenólicos Totais)
  - TF (Teores de Flavonoides)
  - ABTS (Atividade Antioxidante)
- Avaliar os modelos usando ANOVA, p-valores, R² ajustado
- Explorar interações e efeitos quadráticos
- Validar os modelos com base em artigo científico de referência
- Preparar os modelos para integração no app `Streamlit`

---

## 🧪 Dados utilizados

O notebook usa dados presentes no diretório `../data/`, como:

- `dados_experimento.xlsx` → Dados brutos
- `df_tratado.csv` → Dados tratados e prontos para regressão

---

## 🧠 Modelos

Cada variável de resposta foi modelada com regressão polinomial de segunda ordem com termos:

- Lineares: tempo, etanol, razão
- Quadráticos: tempo², etanol², razão²
- Interações: tempo × etanol, etanol × razão

---

## 🧰 Requisitos

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `statsmodels`
- `scikit-learn` (opcional para teste de modelos ML)

---

## ▶️ Como executar

1. Navegue até o diretório do projeto:

```bash
cd projeto_pracaxi
```

2. Abra o Jupyter Notebook:

```bash
jupyter notebook notebooks/Projeto_Extracao_Pracaxi.ipynb
```

---

## 🧠 Autor

Gustavo Neves da Paz Rafael

Projeto acadêmico em Ciência de Dados com aplicação em química experimental

---

## 📚 Referência

> *Optimization of bioactive compound extraction from pracaxi residues by ultrasound-assisted process*, **Luiza Helena**

