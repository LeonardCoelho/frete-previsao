# 🚛 Previsão de Custo de Frete

Este projeto utiliza aprendizado de máquina para prever o valor estimado de um frete com base em variáveis como peso, distância, tipo de carga, modal de transporte, origem e destino.

---

## 📂 Estrutura do Projeto

```
frete-previsao/
├── data/
│   └── fretes_simulados.csv
├── images/
│   └── Print.jpg
├── src/
│   ├── app.py
│   ├── modelo.ipynb
│   └── modelo_random_forest_tunado.pkl
├── README.md
└── requirements.txt
```

---

## 📊 Tecnologias Utilizadas

- Python 3.10+
- Pandas
- Scikit-learn
- Matplotlib & Seaborn
- Streamlit
- Joblib

---

## 🧪 Como Rodar o Projeto

1. **Clone o repositório:**

```bash
git clone https://github.com/LeonardCoelho/frete-previsao
cd frete-previsao
```

2. **Crie um ambiente virtual (opcional):**

```bash
python -m venv venv
source venv/bin/activate  # no Linux/Mac
venv\Scripts\activate     # no Windows
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Execute a aplicação Streamlit:**

```bash
streamlit run src/app.py
```

---

## 🧠 Como o modelo funciona

- O modelo foi treinado com uma base simulada de fretes, contendo:
  - `peso_kg`, `distancia_km`, `prazo_dias`
  - `tipo_carga`, `modal`, `origem_uf`, `destino_uf`
- Foram testados modelos de Regressão Linear e Random Forest.
- O modelo final é um **Random Forest Regressor tunado via GridSearchCV**, salvo como `modelo_random_forest_tunado.pkl`.

---

## 🧾 Exemplo de uso (via app)

Você pode:
- Inserir os dados manualmente e ver a previsão instantaneamente.
- Fazer upload de um `.csv` com as colunas esperadas e baixar as previsões.

---

## 📷 Imagem do App

![app](images/Print.jpg)

---

## 📬 Contato

Desenvolvido por [Leonardo Coelho](https://github.com/LeonardCoelho) 🚀
