import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

from modelos import codificar, modelo_abts, modelo_tpc, modelo_tf
from desejabilidade import desejabilidade_global

# === Interface Streamlit ===
st.title("🎯 Avaliação da Desejabilidade Global - Pracaxi")

st.sidebar.header("🔧 Parâmetros de Entrada")
tempo_real = st.sidebar.slider("Tempo (min)", 15.0, 60.0, 20.0)
etanol_real = st.sidebar.slider("Etanol (%)", 5.0, 60.0, 70.0)
razao_real = st.sidebar.slider("Razão (m/v)", 0.5, 2.0, 0.7)

# Codificação e cálculo dos modelos
x_cod = [codificar(tempo_real, 15, 60), codificar(etanol_real, 5, 60), codificar(razao_real, 0.5, 2)]
abts = modelo_abts(x_cod)
tpc = modelo_tpc(x_cod)
tf = modelo_tf(x_cod)
D, d_abts, d_tpc, d_tf = desejabilidade_global(abts, tpc, tf)

# === Resultados ===
st.subheader("📋 Resultados")
st.markdown(f"**ABTS estimado:** {abts:.2f} µmol ET/g")
st.markdown(f"**TPC estimado:** {tpc:.3f} mg GAE/g")
st.markdown(f"**TF estimado:** {tf:.5f} mg QE/g")
st.markdown(f"**Desejabilidade Global:** {D:.4f}")

# === Gráficos Interativos ===
variaveis = {
    "Tempo": (15, 60, tempo_real, lambda t: [codificar(t, 15, 60), codificar(etanol_real, 5, 60), codificar(razao_real, 0.5, 2)]),
    "Etanol": (5, 60, etanol_real, lambda e: [codificar(tempo_real, 15, 60), codificar(e, 5, 60), codificar(razao_real, 0.5, 2)]),
    "Razão": (0.5, 2.0, razao_real, lambda r: [codificar(tempo_real, 15, 60), codificar(etanol_real, 5, 60), codificar(r, 0.5, 2)])
}

st.subheader("📊 Perfis de Resposta")
fig, axs = plt.subplots(1, 3, figsize=(18, 4))

for idx, (nome, (vmin, vmax, fixo, func)) in enumerate(variaveis.items()):
    valores = np.linspace(vmin, vmax, 100)
    desejabilidades = [desejabilidade_global(
        modelo_abts(func(v)),
        modelo_tpc(func(v)),
        modelo_tf(func(v))
    )[0] for v in valores]

    axs[idx].plot(valores, desejabilidades, label=f"Desejabilidade vs {nome}", color='green')
    axs[idx].axvline(fixo, color='red', linestyle='--', label='Valor atual')
    axs[idx].set_title(f"Desejabilidade x {nome}")
    axs[idx].set_xlabel(nome)
    axs[idx].set_ylabel("Desejabilidade")
    axs[idx].legend()

st.pyplot(fig)

st.markdown("---")
st.caption("Aplicação interativa baseada em modelos de extração por ultrassom - Pedro Aikau")
