import streamlit as st
import pandas as pd
import joblib

# Carregar modelo treinado
modelo = joblib.load('modelo_random_forest_tunado.pkl')

# Título e descrição
st.set_page_config(page_title="Previsão de Frete", layout="centered")
st.title("🚛 Previsão de Custo de Frete")
st.markdown("Preveja o valor estimado de um frete com base em dados como distância, peso e tipo de carga.")

st.divider()

# Inputs organizados em colunas
col1, col2 = st.columns(2)

with col1:
    peso = st.number_input("⚖️ Peso da carga (kg)", min_value=1.0, step=500.0, value=500.0)
    prazo = st.number_input("⏱️ Prazo (dias)", min_value=1, step=1, value=5)
    tipo_carga = st.selectbox("📦 Tipo de Carga", ["Industrial", "Inflamável", "Perecível", "Frágil", "Comum"])

with col2:
    distancia = st.number_input("🛣️ Distância (km)", min_value=1.0, step=10.0, value=500.0)
    modal = st.selectbox("🚚 Modal", ["Rodoviário", "Ferroviário", "Aéreo"])
    uf_origem = st.selectbox("📍 UF Origem", ["SP", "RJ", "MG", "PR", "RS", "SC", "GO", "PE", "ES", "BA"])
    uf_destino = st.selectbox("🎯 UF Destino", ["SP", "RJ", "MG", "PR", "RS", "SC", "GO", "PE", "ES", "BA"])

st.divider()

# Botão de previsão
if st.button("🔍 Calcular Frete"):
    # Validação básica
    if uf_origem == uf_destino:
        st.warning("❗ Origem e destino não podem ser iguais.")
    else:
        with st.spinner("Calculando o valor estimado..."):
            # Montar DataFrame de entrada
            dados = pd.DataFrame({
                'peso_kg': [peso],
                'distancia_km': [distancia],
                'prazo_dias': [prazo],
                'modal': [modal],
                'tipo_carga': [tipo_carga],
                'origem_uf': [uf_origem],
                'destino_uf': [uf_destino]
            })

            # Fazer previsão
            try:
                previsao = modelo.predict(dados)[0]
                st.success(f"💰 Custo estimado do frete: **R$ {previsao:,.2f}**")
            except Exception as e:
                st.error(f"Erro ao prever: {e}")