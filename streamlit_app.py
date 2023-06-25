import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
[Projet Pluridisciplinaire] (https://drive.google.com/file/d/1AAZHmcbd7jpFdqhTs5pqXbZqaX4RELUS/view?usp=sharing)
Réalisé par : 
Adèle Coatanéa 
Quentin Boivin 
Amine Bastaoui
Isabella Wokam
Eliot Bertthié 
Danielle Babi

Site:
Adèle Coatanéa
"""

st.sidebar.title("A propos")
st.sidebar.info(markdown)
logo = "https://www.un.org/youthenvoy/wp-content/uploads/2014/09/unesco-logo-260px.jpg"
st.sidebar.image(logo)

# Customize page title
st.title("Introduction")

st.markdown(
    """
    Ce site a pour but de présenter les résultats graphiques et d’analyse obtenus par notre équipe dans le cadre du [Projet Pluridisciplinaire IG4 2022](https://drive.google.com/file/d/1AAZHmcbd7jpFdqhTs5pqXbZqaX4RELUS/view?usp=sharing). Le travail effectué durant environ trois mois porte sur l’étude d’une portion du Val de Loire située au niveau de l'Île de Béhuard, c’est-à-dire à quelques kilomètres au Sud-Ouest de la ville d’Angers et du confluent Maine-Loire (région Pays de la Loire et département du Maine et Loire).
    """
)

st.header("Zone étudiée")

markdown = """
Notons pour débuter que la zone étudiée grâce aux travaux photogrammétriques (voir Annexe n°1) comporte quatre communes rurales répertoriées dans le tableau ci-après. Comme nous pouvons le constater, celles-ci sont entre autres membres de deux EPCI (Etablissements Publics de Coopération Intercommunale) que sont la Communauté Urbaine Angers Loire Métropole et la Communauté de Communes Loire Layon et Aubance.
1. For the [GitHub repository](https://github.com/giswqs/streamlit-multipage-template) or [use it as a template](https://github.com/giswqs/streamlit-multipage-template/generate) for your own project.
2. Customize the sidebar by changing the sidebar text and logo in each Python files.
3. Find your favorite emoji from https://emojipedia.org.
4. Add a new app to the `pages/` directory with an emoji in the file name, e.g., `1_🚀_Chart.py`.

"""
def main():
    st.title("Bloc diagramme")
    
    # Affiche le bouton pour l'image 1
    if st.button("1983"):
        image_1 = "images/Bloc-diagramme_1983.png"  # Chemin vers l'image 1
        st.image(image_1, caption="Image 1", use_column_width=True)
        
    # Affiche le bouton pour l'image 2
    if st.button("2008"):
        image_2 = "images/Bloc-diagramme_2008.png"  # Chemin vers l'image 2
        st.image(image_2, caption="Image 2", use_column_width=True)

if __name__ == "__main__":
    main()
st.markdown(markdown)

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
