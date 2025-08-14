import streamlit as st
import pandas as pd
import joblib

# Carregar modelo treinado
path = os.path.join(os.path.dirname(__file__), "src", "modelo_random_forest_tunado.pkl")
modelo = joblib.load(path)

# Título e descrição
st.set_page_config(page_title="Previsão de Frete", layout="centered")
st.title("🚛 Previsão de Custo de Frete")
st.markdown("Preveja o valor estimado de um frete com base em dados como distância, peso e tipo de carga.")
st.divider()

# ========================== ENTRADA MANUAL ===============================
st.subheader("📥 Preencher os dados manualmente")
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

if st.button("🔍 Calcular Frete"):
    if uf_origem == uf_destino:
        st.warning("❗ Origem e destino não podem ser iguais.")
    else:
        with st.spinner("Calculando o valor estimado..."):
            entrada = pd.DataFrame({
                'peso_kg': [peso],
                'distancia_km': [distancia],
                'prazo_dias': [prazo],
                'modal': [modal],
                'tipo_carga': [tipo_carga],
                'origem_uf': [uf_origem],
                'destino_uf': [uf_destino]
            })
            try:
                resultado = modelo.predict(entrada)[0]
                st.success(f"💰 Custo estimado do frete: **R$ {resultado:,.2f}**")
            except Exception as e:
                st.error(f"Erro na previsão: {e}")

st.divider()

# ========================== UPLOAD CSV ===============================
st.subheader("📄 Ou envie um arquivo CSV")

uploaded_file = st.file_uploader("Envie um CSV com as colunas: peso_kg, distancia_km, prazo_dias, modal, tipo_carga, origem_uf, destino_uf", type=["csv"])

if uploaded_file:
    try:
        dados = pd.read_csv(uploaded_file)
        colunas_esperadas = ['peso_kg', 'distancia_km', 'prazo_dias', 'modal', 'tipo_carga', 'origem_uf', 'destino_uf']
        if all(col in dados.columns for col in colunas_esperadas):
            with st.spinner("Calculando previsões em lote..."):
                previsoes = modelo.predict(dados)
                dados['frete_estimado_r$'] = previsoes
                st.success("✅ Previsões realizadas com sucesso!")
                st.dataframe(dados)

                csv = dados.to_csv(index=False).encode('utf-8')
                st.download_button("📥 Baixar resultado em CSV", csv, "previsoes_fretes.csv", "text/csv")
        else:
            st.error("❌ As colunas do CSV estão erradas ou incompletas. Use o formato correto:")
            st.code(','.join(colunas_esperadas))
    except Exception as e:
        st.error(f"Erro ao processar o arquivo: {e}")
