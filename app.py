import streamlit as st
import pickle

st.title('Quanto Custa sua Casa?')

filename = 'modelo_treinado.sav'
modelo_treinado = pickle.load(open(filename, 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

col1, col2 = st.columns([1,1])
with col1:
    quartos = st.slider("Quartos",
                        value=1,
                        min_value=0,
                        max_value=5,
                        step=1)
with col2:
    banheiros = st.slider("Banheiros",
                          value=1,
                          min_value=0,
                          max_value=5,
                          step=1)
    
col3, col4 = st.columns([1,1])

with col3:
    vagas = st.slider("Vagas",
                        value=1,
                        min_value=0,
                        max_value=5,
                        step=1)
with col4:
    area = st.number_input('Área (m2)')

X_novo = [[area, quartos, banheiros, vagas]]
X_novo_scaled = scaler.transform(X_novo)

y_predito = modelo_treinado.predict(X_novo_scaled)

st.divider()

st.markdown("""
<style>
.big-font {
    font-size:30px !important;
}
</style>
""", unsafe_allow_html=True)
# <p class="big-font">Hello World !!</p>
st.markdown(f'<p class="big-font">Preço da casa: R$ {int(y_predito)},00</p>', unsafe_allow_html=True)

