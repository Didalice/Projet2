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
    st.header("Projet Pluridisciplianire 2022.")
    st.subheader("Objetivo e Usuário")
    st.write("L'objectif de ce projet est d'étudier une portion du Val de Loire située au niveau de l'Île de Béhuard. L'utilisateur de ce programme est intéressé par l'analyse graphique et les résultats obtenus à partir des travaux réalisés.")
    st.write("Ce projet réalisé sur streamlit permet une visualisation plus interactive du rapport.")
    st.subheader("Tipo (aplicação web, plugin QGIS, caderno Jupyter/colab)")
    st.write("Ce programme est une application web développée avec Streamlit.")
    st.subheader("Bibliotecas principais")
    st.write("Les bibliothèques principales utilisées dans ce programme sont :")
    st.write("- Streamlit")
    st.write("- Leafmap")
    st.write("- Pandas")
    st.subheader("Arquitetura")
    st.write("L'architecture de ce programme suit le modèle MVC (Modèle-Vue-Contrôleur), où Streamlit agit comme le contrôleur, Leafmap comme la vue pour la cartographie et Pandas pour la manipulation des données.")
    st.subheader("Dados de Entrada")
    st.write("- Les données pour genere les cartes proviennent de l'analyse de deux photographies aérienne de l'IGN, nomenclature de Croine Land Cover")
    st.write("- Le texte provient du [rapport du projet pluridisciplinaire](https://drive.google.com/file/d/1AAZHmcbd7jpFdqhTs5pqXbZqaX4RELUS/view?usp=sharing) effectué en France en 2022")
    st.write("- Pour les cartes, j'ai utilisé Qgis pour pouvoir les exporter sous le formats Geojson")
    st.subheader("Funcionalidades")
    st.write("Les principales fonctionnalités de ce programme sont :")
    st.write("- Affichage des photographies aériennes")
    st.write("- Identification des unités paysagères")
    st.write("- Caractérisation des paysages actuels et passés")
    st.write("- Génération de cartes et de visualisations graphiques")
    st.subheader("Dados de Saída (atenção para os mapas)")
    st.write("Les données de sortie de ce programme comprennent :")
    st.write("- Les unités paysagères identifiées")
    st.write("- Les caractéristiques des paysages actuels et passés")
    st.write("- Les cartes et visualisations graphiques générées")
    
    
    st.subheader("Esboço da Interface")
    st.write("L'interface de ce programme comprend différentes sections, notamment :")
    st.write("- Une barre latérale avec des informations sur le projet")
    st.write("- Une section d'introduction avec des explications sur la zone étudiée")
    st.write("- Des boutons pour afficher les photographies et les visualisations")
    st.write("- Des marqueurs sur une carte pour identifier les unités paysagères")

if __name__ == "__main__":
    main()
