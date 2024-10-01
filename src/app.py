import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Carregar o modelo treinado
model = joblib.load('./models/modelo_imovel_regression.pkl')

# Título da aplicação
st.title("Previsão de Preço de Imóveis em São Paulo")

# Entradas do usuário
st.header("Insira os detalhes do imóvel:")

# Entradas numéricas
area_util = st.number_input("Área Útil (m²)", min_value=0.0)
banheiros = st.number_input("Número de Banheiros", min_value=0)
suites = st.number_input("Número de Suítes", min_value=0)
quartos = st.number_input("Número de Quartos", min_value=0)
vagas_garagem = st.number_input("Número de Vagas de Garagem", min_value=0)

# Seleção do tipo de imóvel
tipo_imovel = st.selectbox("Tipo de Imóvel", 
    ['Casa', 'Apartamento', 'Comercial', 'Flat', 'Condomínio', 
     'Cobertura', 'Loja', 'Prédio Residencial', 'Escritório'])

# Botão para fazer a previsão
if st.button("Prever Preço"):
    # Criar DataFrame com as entradas
    input_data = pd.DataFrame({
        'area_util': [area_util],
        'banheiros': [banheiros],
        'suites': [suites],
        'quartos': [quartos],
        'vagas_garagem': [vagas_garagem],
        'tipo_imovel_recategorized': [tipo_imovel]
    })
    
    # Realizar a previsão
    prediction = model.predict(input_data)
    
    # Exibir o resultado
    st.success(f"O preço estimado para o imóvel é: R$ {prediction[0]:,.2f}")
