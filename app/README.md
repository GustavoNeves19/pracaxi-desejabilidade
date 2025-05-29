# 🚀 Pasta `app/`

Esta pasta contém todos os arquivos Python responsáveis pela aplicação interativa desenvolvida com **Streamlit**, voltada à modelagem e otimização da extração de compostos bioativos do Pracaxi. Aqui se concentram os scripts que estruturam a lógica do deploy, modelos preditivos e a função de desejabilidade global.

---

## 📄 Arquivos

### `app.py`
- **Principal script executável da aplicação**
- Contém toda a lógica da interface desenvolvida com Streamlit.
- Permite que o usuário insira valores de entrada (tempo, etanol, razão) e visualize:
  - Previsões dos compostos bioativos (TPC, TF, ABTS)
  - Gráficos 2D e 3D das superfícies de resposta
  - Valor de desejabilidade global

Execute com:
```bash
streamlit run app/app.py
```

---

### `modelos.py`
- Define os modelos estatísticos ajustados a partir de regressões polinomiais para:
  - `TPC` – Compostos Fenólicos Totais
  - `TF` – Teores de Flavonoides
  - `ABTS` – Atividade Antioxidante
- Utiliza a biblioteca `statsmodels` para estimar os coeficientes.

---

### `desejabilidade.py`
- Implementa o cálculo da **desejabilidade individual** e da **desejabilidade global**.
- Permite identificar as melhores condições experimentais para otimizar simultaneamente todas as respostas.
- Baseado na função de Harrington modificada, comum em projetos de otimização multivariada.

---

## ✅ Requisitos

Certifique-se de que os seguintes pacotes estão listados no `requirements.txt` no diretório raiz do projeto:
- `streamlit`
- `pandas`
- `statsmodels`
- `plotly`
- `matplotlib`
- `numpy`

---

## 📎 Observações

- Este módulo foi construído com foco em **modularização e clareza**, permitindo fácil manutenção e futuras extensões (ex: integração com redes neurais ou banco de dados).
- Os dados são carregados diretamente do arquivo `data/data_pracaxi.csv`, portanto mantenha a estrutura de pastas organizada.

---

## 🔗 Projeto Principal

Este aplicativo faz parte do projeto maior descrito no [README principal](../README.md).
