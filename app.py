import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles.csv') # lendo os dados
# criar o header da página
st.header('Anúncios de Vendas de Carros')
st.markdown("""<div style='border-bottom:2px solid #5D2CDA;'></div>""", True)

# Criando radio buttons
selected_chart = st.radio('Selecione o tipo de gráfico:', ['Histograma', 'Gráfico de Dispersão'])

if selected_chart == 'Histograma':
    # escrever uma mensagem
    st.write('Criando um histograma para a coluna Odometer...')
    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

elif selected_chart == 'Gráfico de Dispersão':
    # escrever uma mensagem
    st.write("Criando um gráfico de dispersão para a coluna Odometer x Price...")

    # criar o scatter plot
    fig = px.scatter(car_data, x="odometer", y="price")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
