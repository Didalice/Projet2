import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
st.set_page_config(page_title="Projet Pluridisciplinaire",page_icon="🗺️",)
#Config langue
langue = st.sidebar.selectbox(' ',["Francais", "English", "Portugues"])

#texte francais
propos="A propos"
t_propos="""
[Projet Pluridisciplinaire](https://drive.google.com/file/d/1AAZHmcbd7jpFdqhTs5pqXbZqaX4RELUS/view?usp=sharing)

Réalisé par : Adèle Coatanéa, Quentin Boivin, Amine Bastaoui, Isabella Wokam, Eliot Bertthié, Danielle Babi

Site: Adèle Coatanéa
"""
titre="Introduction"
texte1= "Ce site a pour but de présenter les résultats graphiques et d’analyse obtenus par notre équipe dans le cadre du [Projet Pluridisciplinaire IG4 2022](https://drive.google.com/file/d/1AAZHmcbd7jpFdqhTs5pqXbZqaX4RELUS/view?usp=sharing). Le travail effectué durant environ trois mois porte sur l’étude d’une portion du Val de Loire située au niveau de l'Île de Béhuard, c’est-à-dire à quelques kilomètres au Sud-Ouest de la ville d’Angers et du confluent Maine-Loire (région Pays de la Loire et département du Maine et Loire)."
texte2="Zones étudié"
texte3="Notons pour débuter que la zone étudiée grâce aux [travaux photogrammétriques](https://drive.google.com/file/d/10QjZFIAcQ9V57X6L0vEXWo8VgV8BCC7S/view?usp=sharing) comporte quatre communes rurales répertoriées dans le tableau ci-après. Comme nous pouvons le constater, celles-ci sont entre autres membres de deux EPCI (Etablissements Publics de Coopération Intercommunale) que sont la Communauté Urbaine Angers Loire Métropole et la Communauté de Communes Loire Layon et Aubance."
texte4="Bloc diagramme de 1983"
texte5="Bloc diagramme de 2008"
texte6="Coupe paysagère en 2008"
source1="Sources: photographies aériennes, IGN (2008) et BRGM"
source2="Sources photographies aériennes, IGN (2008) et carte topographique IGN"
data = [
    ["Commune", "Code Postal et Code Commune", "EPCI principal"],
    ["Béhuard", "49170 / 49028", "Communauté Urbaine Angers Loire Métropole"],
    ["Savennières", "49170 / 49329", "Communauté Urbaine Angers Loire Métropole"],
    ["Bouchemaine", " 49080 /49035", "Communauté Urbaine Angers Loire Métropole"],
    ["Denée", "49190 / 49120", "Communauté de Communes Loire Layon et Aubance"]
]
if langue =='English':
    propos = "About"
    t_propos = """
    [Interdisciplinary Project](https://drive.google.com/file/d/1AAZHmcbd7jpFdqhTs5pqXbZqaX4RELUS/view?usp=sharing)
    
    Realized by: Adèle Coatanéa, Quentin Boivin, Amine Bastaoui, Isabella Wokam, Eliot Bertthié, Danielle Babi
    
    Website: Adèle Coatanéa
    """
    titre = "Introduction"
    texte1 = "This website aims to present the graphical and analytical results obtained by our team as part of the [Interdisciplinary Project IG4 2022](https://drive.google.com/file/d/1AAZHmcbd7jpFdqhTs5pqXbZqaX4RELUS/view?usp=sharing). The work carried out for approximately three months focuses on the study of a portion of the Loire Valley located at Île de Béhuard, which is a few kilometers southwest of the city of Angers and the Maine-Loire confluence (Pays de la Loire region and Maine-et-Loire department)."
    texte2 = "Studied Zones"
    texte3 = "To begin with, the area studied through [photogrammetric works](https://drive.google.com/file/d/10QjZFIAcQ9V57X6L0vEXWo8VgV8BCC7S/view?usp=sharing) includes four rural municipalities listed in the table below. As we can see, these are among the members of two Public Institutions of Intercommunality (EPCI), namely the Angers Loire Métropole Urban Community and the Loire Layon et Aubance Community of Communes."
    texte4 = "1983 Block Diagram"
    texte5 = "2008 Block Diagram"
    texte6 = "Landscape Section in 2008"
    data = [
        ["Municipality", "Postal Code and Municipality Code", "Main EPCI"],
        ["Béhuard", "49170 / 49028", "Angers Loire Métropole Urban Community"],
        ["Savennières", "49170 / 49329", "Angers Loire Métropole Urban Community"],
        ["Bouchemaine", "49080 / 49035", "Angers Loire Métropole Urban Community"],
        ["Denée", "49190 / 49120", "Loire Layon et Aubance Community of Communes"]
    ]
    source1 = "Sources: aerial photographs, IGN (2008) and BRGM"
    source2 = "Sources: aerial photographs, IGN (2008) and IGN topographic map"


if langue == 'Portugues':
    propos = "Sobre"
    t_propos = """
    [Projeto Multidisciplinar](https://drive.google.com/file/d/1AAZHmcbd7jpFdqhTs5pqXbZqaX4RELUS/view?usp=sharing)

    Realizado por: Adèle Coatanéa, Quentin Boivin, Amine Bastaoui, Isabella Wokam, Eliot Bertthié, Danielle Babi

    Site: Adèle Coatanéa
    """
    titre = "Introdução"
    texte1 = "Este site tem como objetivo apresentar os resultados gráficos e análises obtidos pela nossa equipe no âmbito do [Projeto Pluridisciplinar IG4 2022](https://drive.google.com/file/d/1AAZHmcbd7jpFdqhTs5pqXbZqaX4RELUS/view?usp=sharing). O trabalho realizado durante aproximadamente três meses aborda o estudo de uma parte do Vale do Loire localizada na Ilha de Béhuard, a poucos quilômetros a sudoeste da cidade de Angers e da confluência Maine-Loire (região de Pays de la Loire e departamento de Maine et Loire)."
    texte2 = "Áreas estudadas"
    texte3 = "Observamos inicialmente que a área estudada, por meio dos [trabalhos fotogramétricos](https://drive.google.com/file/d/10QjZFIAcQ9V57X6L0vEXWo8VgV8BCC7S/view?usp=sharing), inclui quatro comunas rurais listadas na tabela a seguir. Como podemos ver, elas são, entre outras, membros de duas EPCI (Estabelecimentos Públicos de Cooperação Intercomunal) que são a Comunidade Urbana Angers Loire Métropole e a Comunidade de Comunas Loire Layon et Aubance."
    texte4 = "Diagrama de blocos de 1983"
    texte5 = "Diagrama de blocos de 2008"
    texte6 = "Perfil paisagístico em 2008"
    data = [
        ["Comuna", "Código Postal e Código da Comuna", "EPCI principal"],
        ["Béhuard", "49170 / 49028", "Comunidade Urbana Angers Loire Métropole"],
        ["Savennières", "49170 / 49329", "Comunidade Urbana Angers Loire Métropole"],
        ["Bouchemaine", " 49080 /49035", "Comunidade Urbana Angers Loire Métropole"],
        ["Denée", "49190 / 49120", "Comunidade de Comunas Loire Layon et Aubance"]
    ]
    source1 = "Fontes: fotografias aéreas, IGN (2008) e BRGM"
    source2 = "Fontes: fotografias aéreas, IGN (2008) e mapa topográfico do IGN"



def main():

    st.sidebar.title(propos)
    st.sidebar.info(t_propos)
    logo = "images/UNESCO.gif"
    st.sidebar.image(logo)
    
    st.title(titre)
    st.markdown(texte1)
    st.subheader(texte2)
    st.markdown(texte3)
    
    df = pd.DataFrame(data[1:], columns=data[0])
    st.table(df)
    
    col1, col2, col3 = st.columns(3)
    if col1.button(texte4):
        image_1 = "images/Bloc-diagramme_1983.png"
        st.image(image_1, caption="Image 1", use_column_width=True)
        st.markdown(f'''<span style="font-size: 10px; font-style: italic;">{source1}</span>''', unsafe_allow_html=True)
    if col2.button(texte5):
        image_2 = "images/Bloc-diagramme_2008.png"
        st.image(image_2, caption="Image 2", use_column_width=True)
        st.markdown(f'''<span style="font-size: 10px; font-style: italic;">{source1}</span>''', unsafe_allow_html=True)

    if col3.button(texte6):
        image_2 = "images/COUPE.png"  
        st.image(image_2, caption="Image 2", use_column_width=True)
        st.markdown(f'''<span style="font-size: 10px; font-style: italic;">{source2}</span>''', unsafe_allow_html=True)


if __name__ == "__main__":
    main()

