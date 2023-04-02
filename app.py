import os
import pandas as pd
import streamlit as st

# Carregando o arquivo CSV
csv_file = 'gps_tietc.csv'
df = pd.read_csv(csv_file)

# Inicializando o aplicativo Streamlit
st.title('Onde estão nossos amiguinhos do grupo')

# Criando um SelectBox para selecionar o nome
nome = st.selectbox('Selecione o nome:', df['nome'].unique())

# Filtrando as coordenadas pelo nome selecionado
coordenadas = df[df['nome'] == nome][['latitude', 'longitude']]

# Verificando se existe um arquivo .png com o mesmo nome do arquivo CSV
image_file = nome + '.png'
if os.path.isfile(image_file):
    st.image(image_file, caption='é ele mesmo', width=5, use_column_width=True)

# Verificando se existe um arquivo .wav com o mesmo nome do arquivo CSV
audio_file = nome + '.wav'
if os.path.isfile(audio_file):
    st.audio(audio_file, format='audio/wav', start_time=0)

# Exibindo a posição no mapa GPS
st.map(coordenadas)


