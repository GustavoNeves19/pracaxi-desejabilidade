import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.graph_objects as go

from modelos import codificar, modelo_abts, modelo_tpc, modelo_tf
from desejabilidade import desejabilidade_global

st.title("🎯 Avaliação da Desejabilidade Global - Pracaxi")

st.sidebar.header("🔧 Parâmetros de Entrada")
tempo_real = st.sidebar.slider("Tempo (min)", 15.0, 60.0, 20.0)
etanol_real = st.sidebar.slider("Etanol (%)", 5.0, 80.0, 70.0)
razao_real = st.sidebar.slider("Razão (m/v)", 0.5, 2.0, 0.7)

x_cod = [codificar(tempo_real, 15, 60), codificar(etanol_real, 5, 60), codificar(razao_real, 0.5, 2)]
abts = modelo_abts(x_cod)
tpc = modelo_tpc(x_cod)
tf = modelo_tf(x_cod)
D, d_abts, d_tpc, d_tf = desejabilidade_global(abts, tpc, tf)

st.subheader("📋 Resultados")
st.markdown(f"**ABTS estimado:** {abts:.2f} µmol ET/g")
st.markdown(f"**TPC estimado:** {tpc:.3f} mg GAE/g")
st.markdown(f"**TF estimado:** {tf:.5f} mg QE/g")
st.markdown(f"**Desejabilidade Global:** {D:.4f}")

st.subheader("📊 Perfis de Resposta (1D)")
variaveis = {
    "Tempo": (15, 60, tempo_real, lambda t: [codificar(t, 15, 60), codificar(etanol_real, 5, 60), codificar(razao_real, 0.5, 2)]),
    "Etanol": (5, 80, etanol_real, lambda e: [codificar(tempo_real, 15, 60), codificar(e, 5, 60), codificar(razao_real, 0.5, 2)]),
    "Razão": (0.5, 2.0, razao_real, lambda r: [codificar(tempo_real, 15, 60), codificar(etanol_real, 5, 60), codificar(r, 0.5, 2)])
}

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

# === Gráficos 3D com Plotly ===
st.subheader("🌐 Gráficos Interativos 3D")
tempo_vals = np.linspace(15, 60, 40)
etanol_vals = np.linspace(5, 80, 40)
razao_vals = np.linspace(0.5, 2.0, 40)

# Tempo x Etanol, razão fixa
tempo_mesh, etanol_mesh = np.meshgrid(tempo_vals, etanol_vals)
D_te = np.array([
    desejabilidade_global(
        modelo_abts([codificar(t, 15, 60), codificar(e, 5, 60), codificar(razao_real, 0.5, 2)]),
        modelo_tpc([codificar(t, 15, 60), codificar(e, 5, 60), codificar(razao_real, 0.5, 2)]),
        modelo_tf([codificar(t, 15, 60), codificar(e, 5, 60), codificar(razao_real, 0.5, 2)])
    )[0] for t, e in zip(np.ravel(tempo_mesh), np.ravel(etanol_mesh))
]).reshape(tempo_mesh.shape)

fig1 = go.Figure(data=[go.Surface(z=D_te, x=tempo_vals, y=etanol_vals, colorscale='Viridis')])
fig1.update_layout(title="Desejabilidade: Tempo x Etanol", scene=dict(xaxis_title='Tempo', yaxis_title='Etanol', zaxis_title='D'))
st.plotly_chart(fig1)

# Tempo x Razão, etanol fixo
tempo_mesh2, razao_mesh = np.meshgrid(tempo_vals, razao_vals)
D_tr = np.array([
    desejabilidade_global(
        modelo_abts([codificar(t, 15, 60), codificar(etanol_real, 5, 60), codificar(r, 0.5, 2)]),
        modelo_tpc([codificar(t, 15, 60), codificar(etanol_real, 5, 60), codificar(r, 0.5, 2)]),
        modelo_tf([codificar(t, 15, 60), codificar(etanol_real, 5, 60), codificar(r, 0.5, 2)])
    )[0] for t, r in zip(np.ravel(tempo_mesh2), np.ravel(razao_mesh))
]).reshape(tempo_mesh2.shape)

fig2 = go.Figure(data=[go.Surface(z=D_tr, x=tempo_vals, y=razao_vals, colorscale='Cividis')])
fig2.update_layout(title="Desejabilidade: Tempo x Razão", scene=dict(xaxis_title='Tempo', yaxis_title='Razão', zaxis_title='D'))
st.plotly_chart(fig2)

# Etanol x Razão, tempo fixo
etanol_mesh2, razao_mesh2 = np.meshgrid(etanol_vals, razao_vals)
D_er = np.array([
    desejabilidade_global(
        modelo_abts([codificar(tempo_real, 15, 60), codificar(e, 5, 60), codificar(r, 0.5, 2)]),
        modelo_tpc([codificar(tempo_real, 15, 60), codificar(e, 5, 60), codificar(r, 0.5, 2)]),
        modelo_tf([codificar(tempo_real, 15, 60), codificar(e, 5, 60), codificar(r, 0.5, 2)])
    )[0] for e, r in zip(np.ravel(etanol_mesh2), np.ravel(razao_mesh2))
]).reshape(etanol_mesh2.shape)

fig3 = go.Figure(data=[go.Surface(z=D_er, x=etanol_vals, y=razao_vals, colorscale='Blues')])
fig3.update_layout(title="Desejabilidade: Etanol x Razão", scene=dict(xaxis_title='Etanol', yaxis_title='Razão', zaxis_title='D'))
st.plotly_chart(fig3)

st.markdown("---")
st.caption("Aplicação de Ciência de Dados de forma interativa baseada em modelos de extração por ultrassom - Gustavo Neves")
