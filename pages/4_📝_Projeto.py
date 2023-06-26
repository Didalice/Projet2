import streamlit as st
import leafmap.foliumap as leafmap
import folium
from streamlit_folium import folium_static



markdown = """
[Projet Pluridisciplinaire](https://drive.google.com/file/d/1AAZHmcbd7jpFdqhTs5pqXbZqaX4RELUS/view?usp=sharing)

Réalisé par : Adèle Coatanéa, Quentin Boivin, Amine Bastaoui, Isabella Wokam, Eliot Bertthié, Danielle Babi

Site: Adèle Coatanéa
"""

st.sidebar.title("A propos")
st.sidebar.info(markdown)
logo = "images/UNESCO.gif"
st.sidebar.image(logo)
def main():
    st.header("Projeto Pluridisciplinar 2022.")
    st.subheader("Objetivo e Usuário")
    image = 'images/Capture.jpg'
    st.image(image, caption="Captura do relatório", use_column_width=True)
    
    st.write("O objetivo deste projeto é estudar uma parte do Vale do Loire localizada na Ilha de Béhuard. O usuário deste programa está interessado na análise gráfica e nos resultados obtidos a partir dos trabalhos realizados.")
    st.write("Este projeto desenvolvido no Streamlit permite uma visualização mais interativa do relatório.")
    st.subheader("Tipo (aplicação web, plugin QGIS, caderno Jupyter/colab)")
    st.write("Este programa é uma aplicação web desenvolvida com o Streamlit.")
    st.subheader("Bibliotecas principais")
    st.write("As principais bibliotecas utilizadas neste programa são:")
    st.write("- Streamlit")
    st.write("- Leafmap")
    st.write("- Pandas")
    st.subheader("Arquitetura")
    st.write("A arquitetura deste programa segue o modelo MVC (Model-View-Controller), onde o Streamlit atua como o controlador, o Leafmap como a visualização para mapas e o Pandas para manipulação de dados.")
    st.subheader("Dados de Entrada")
    st.write("- Os dados para gerar os mapas são provenientes da análise de duas fotografias aéreas do IGN, nomenclatura de Croine Land Cover")
    st.write("- O texto é retirado do [relatório do projeto pluridisciplinar](https://drive.google.com/file/d/1AAZHmcbd7jpFdqhTs5pqXbZqaX4RELUS/view?usp=sharing) realizado na França em 2022")
    st.write("- Para os mapas, utilizei o Qgis para poder exportá-los no formato Geojson")
    st.subheader("Funcionalidades")
    st.write("As principais funcionalidades deste programa são:")
    st.write("- Exibição das fotografias aéreas")
    st.write("- Identificação das unidades paisagísticas")
    st.write("- Caracterização das paisagens atuais e passadas")
    st.write("- Geração de mapas e visualizações gráficas")
    st.subheader("Dados de Saída (atenção para os mapas)")
    st.write("Os dados de saída deste programa incluem:")
    st.write("- As unidades paisagísticas identificadas")
    st.write("- As características das paisagens atuais e passadas")
    st.write("- Os mapas e visualizações gráficas gerados")
    
    
    st.subheader("Esboço da Interface")
    st.write("A interface deste programa inclui diferentes seções, incluindo:")
    st.write("- Uma barra lateral com informações sobre o projeto")
    st.write("- Uma seção de introdução com explicações sobre a área estudada")
    st.write("- Botões para exibir fotografias e visualizações")
    st.write("- Marcadores em um mapa para identificar as unidades paisagísticas")

if __name__ == "__main__":
    main()
