# 🚛 Previsão de Custos de Frete com Machine Learning

Este projeto usa Machine Learning para prever o custo final de fretes com base em variáveis como peso da carga, distância, prazo, tipo de carga, modal e origem/destino.

🔗 [Acesse o app aqui no Streamlit](https://frete-previsao-fz2s5ocwoc97y6ggf2bm2m.streamlit.app)
📁 [Veja o notebook do modelo aqui](modelo.ipynb)

---

## 📊 Tecnologias Usadas

- Python 3.11
- Scikit-learn
- Pandas, NumPy
- Matplotlib, Seaborn
- Streamlit
- Joblib

---

## 🧠 O que o modelo aprende?

O modelo Random Forest foi treinado com `GridSearchCV` e alcançou:

- MAE: ~**R$ 683**
- RMSE: ~**R$ 910**
- R²: ~**0.97**

Ele considera:
- Peso (kg)
- Distância (km)
- Tipo de carga (perecível, inflamável etc.)
- Modal (rodoviário, aéreo etc.)
- Prazo de entrega
- UF de origem e destino

---

## 🚀 Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/frete-previsao.git
cd frete-previsao

# Crie o ambiente virtual
python -m venv .venv
source .venv/Scripts/activate  # no Windows
pip install -r requirements.txt

# Rode o app
streamlit run app.py

## 👨‍💻 Autor
**Leonardo Coelho**  
[LinkedIn](https://www.linkedin.com/in/leoscoelho/) • [GitHub](https://github.com/LeonardCoelho)