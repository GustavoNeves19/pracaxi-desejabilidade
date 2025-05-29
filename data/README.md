# 📁 Pasta `data/`

Esta pasta contém os arquivos de dados utilizados no projeto de modelagem preditiva e desejabilidade aplicado à extração de compostos bioativos do Pracaxi.

---

## 📄 Arquivos

### `data-treated-pracaxi.csv`
- ✅ **Descrição**: Arquivo de dados tratados, contendo as variáveis independentes e respostas dependentes já prontas para uso em regressões e análise estatística.
- 📌 **Variáveis principais**:
  - `tempo` — Tempo de extração (min)
  - `etanol` — Concentração de etanol (%)
  - `razao` — Razão sólido-líquido (m/v)
  - `TPC`, `TF`, `ABTS` — Respostas experimentais (compostos bioativos)

---

### `data_pracaxi.xlsx` 
- ❗ **Uso interno (não público)**: contém os dados brutos originais obtidos em bancada, com possíveis identificações dos experimentos.
- 🧪 Pode conter anotações manuais ou ajustes de laboratório antes da etapa de tratamento.

---

## 🔐 Aviso

Evite versionar dados sensíveis, brutos ou que identifiquem experimentos internos sem autorização do grupo de pesquisa. Recomenda-se que o arquivo `.xlsx` não seja incluído no repositório público, apenas o `.csv` tratado.

---

## 📌 Como utilizar

```python
import pandas as pd

df = pd.read_csv("data/df_tratado.csv")

```

Esse ``DataFrame`` é usado tanto no notebook analítico quanto no app.py para geração dos modelos e gráficos.

## 🧪 Projeto relacionado
Este conjunto de dados serve como base para o projeto ![Pracaxi Desejabilidade](../README.md), em conjunto com notebooks e a aplicação em Streamlit.
