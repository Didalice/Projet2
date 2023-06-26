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
    st.title("Autor")
    st.markdown("Ce programme a été développé par [votre nom] dans le cadre du [Projet Pluridisciplinaire].")
    
    st.subheader("Título do Projeto")
    st.markdown("Le titre du projet est [insérer le titre du projet].")
    
    st.subheader("Objetivo e Usuário")
    st.markdown("L'objectif principal de ce projet est [insérer l'objectif principal du projet]. Les utilisateurs cibles de ce programme sont [insérer les utilisateurs cibles du programme].")
    
    st.subheader("Tipo (aplicação web, plugin QGIS, caderno Jupyter/colab)")
    st.markdown("Ce programme est une [insérer le type de programme] développé avec [insérer les technologies/utilitaires utilisés pour développer le programme].")
    
    st.subheader("Bibliotecas principais")
    st.markdown("Les bibliothèques principales utilisées dans ce programme sont [insérer les bibliothèques principales utilisées dans le programme].")
    
    st.subheader("Arquitetura")
    st.markdown("L'architecture de ce programme est [insérer l'architecture du programme].")
    
    st.subheader("Dados de Entrada")
    st.markdown("Les données d'entrée utilisées dans ce programme sont [insérer les données d'entrée utilisées dans le programme].")
    
    st.subheader("Funcionalidades")
    st.markdown("Les fonctionnalités de ce programme comprennent [insérer les fonctionnalités du programme].")
    
    st.subheader("Dados de Saída (atenção para os mapas)")
    st.markdown("Les données de sortie générées par ce programme sont [insérer les données de sortie générées par le programme]. Il faut faire attention particulièrement aux [insérer les détails spécifiques sur les cartes ou les données de sortie liées aux cartes].")
    
    st.subheader("Esboço da Interface")
    st.markdown("L'esquisse de l'interface utilisateur de ce programme est [insérer l'esquisse de l'interface utilisateur].")

if __name__ == "__main__":
    main()
