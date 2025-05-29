# 🌿 Aplicação de Avaliação da Desejabilidade Global – Extração de Compostos Bioativos do Pracaxi

Este projeto disponibiliza uma aplicação interativa em **Streamlit** para simular e visualizar a **desejabilidade global** de extração de compostos bioativos a partir do Pracaxi, baseada em modelos estatísticos ajustados com dados experimentais e orientações de um artigo científico de referência.

🔗 **Acesse a aplicação online aqui**:  
👉 [https://pracaxi-desejabilidade-9dfzvxafencva7jawo8k76.streamlit.app/](Pracaxi-Desejabilidade)

---

## ⚙️ Tecnologias e Bibliotecas

- Python
- pandas, numpy
- statsmodels
- matplotlib, seaborn, plotly
- Streamlit

---

## 📁 Estrutura do Repositório

```bash
Natural-Language-Processing/
├── app/    
│   ├── app.py               # Script principal com a interface Streamlit
│   ├── modelos.py           # Modelos polinomiais para ABTS, TPC e TF
│   ├── desejabilidade.py    # Funções para cálculo da desejabilidade global
├── data/                   
│   ├── data_pracaxi.xlsx    # Base de Dados Bruto 
│   ├── data-treated-pracaxi   # Base de Dados Tratados
├── notebooks/                
│   ├── Projeto_Extracao_Pracaxi.ipynb   # Notebooks de análise estatística
│   ├── README.md   # Explicação técnica da modelagem e análises
└── requirements.txt # Lista de Bibliotecas usadas no projeto
└── gitignore   # Arquivos e pastas a serem ignorados no controle de versão
└── README.md               # Este documento
```

## 📌 Objetivo

A ferramenta permite que pesquisadores, estudantes ou químicos explorem como as variáveis experimentais — **tempo de extração**, **razão sólido-líquido** e **concentração de etanol** — afetam a **extração de compostos**:

- **ABTS** (atividade antioxidante)
- **TPC** (compostos fenólicos totais)
- **TF** (teores de flavonoides)

Com base nesses compostos, o sistema calcula a **desejabilidade global** para cada conjunto de condições.

---

## 🧪 Entradas

Via barra lateral, o usuário fornece:

- `Tempo (min)`: 15 a 60 minutos
- `Etanol (%)`: 5 a 60%
- `Razão (m/v)`: 0.5 a 2.0 (massa de sólido por volume de solvente)

---

## 📊 Saídas

A aplicação exibe:

- Valores estimados de **ABTS**, **TPC** e **TF**
- **Desejabilidade global (D)**, combinando as três variáveis de resposta
- Gráficos 2D de perfis de resposta (variável vs desejabilidade)
- Gráficos 3D interativos relacionando pares de variáveis com a desejabilidade

---

## 📈 Base Estatística

Os modelos são do tipo **regressão polinomial de segunda ordem**, com:

- Termos lineares, quadráticos e interações
- Análise de significância via **ANOVA**
- Otimização baseada em função de **desejabilidade de Derringer & Suich**

---

## 🚀 Como Rodar Localmente

1. Clone o repositório:
```bash
git clone https://github.com/GustavoNeves19/pracaxi-desejabilidade.git
cd pracaxi-desejabilidade
```
2. Instale as Dependências
```bash
pip install -r requirements.txt
```

3. Rode o Aplicativo
```bash
streamlit run app.py
```

---

## 🧠 Autor

**Gustavo Neves da Paz Rafael**

Cientista de dados em formação | Grupo de Pesquisa em IA e Simulação Aplicado à Ciência de Alimentos (UFRA)

---

## 📚 Referência Científica

> *“Optimization of bioactive compound extraction from pracaxi residues by ultrasound-assisted process”* , **Luiza Helena**

---

## 📜 Licença
Este projeto é acadêmico e livre para uso não comercial. Consulte o autor para fins científicos ou educacionais.