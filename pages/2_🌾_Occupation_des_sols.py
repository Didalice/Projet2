import streamlit as st
import leafmap.foliumap as leafmap
import folium
from streamlit_folium import folium_static


st.set_page_config(page_title='Projet Pluridisciplinaire',page_icon="🗺️",)

#Change de langue
langue = st.sidebar.selectbox(' ',["Francais", "English", "Portugues"])

#texte en diff langue
propos="A propos"
t_propos="""[Projet Pluridisciplinaire](https://drive.google.com/file/d/1AAZHmcbd7jpFdqhTs5pqXbZqaX4RELUS/view?usp=sharing)

Réalisé par : Adèle Coatanéa, Quentin Boivin, Amine Bastaoui, Isabella Wokam, Eliot Bertthié, Danielle Babi

Site: Adèle Coatanéa"""
titre="Une modification de l’occupation des sols depuis 40 ans témoin de changements morphologiques"
texte1="L’étude plus précise de la répartition de l’occupation des sols d’un espace est également un moyen de mettre en évidence certaines évolutions. Après avoir abordé ces dernières avec une vision générale dans la partie précédente, nous allons à présent utiliser des données chiffrées et plus précises pour renforcer nos observations. Pour réaliser les cartes et diagrammes relatifs à l’occupation des sols de notre secteur d’étude, nous avons utilisé les photographies de 1982 et 2008 à notre disposition. Nous avons également adopté la nomenclature de niveau 3 de la base de données Corine Land Cover pour représenter et nommer les différents types d’espace."
texte2="L’étude plus précise de la répartition de l’occupation des sols d’un espace est également un moyen de mettre en évidence certaines évolutions. Après avoir abordé ces dernières avec une vision générale dans la partie précédente, nous allons à présent utiliser des données chiffrées et plus précises pour renforcer nos observations. Pour réaliser les cartes et diagrammes relatifs à l’occupation des sols de notre secteur d’étude, nous avons utilisé les photographies de 1982 et 2008 à notre disposition. Nous avons également adopté la nomenclature de niveau 3 de la base de données Corine Land Cover pour représenter et nommer les différents types d’espace."
texte3="A - Une diminution de la superficie des prairies au profit des espaces cultivés"
texte4="Grâce à l’analyse des unités paysagères, nous avons pu constater que l’espace non-urbanisé de notre périmètre n’a pas connu d’évolution notable au cours des quarante années séparant les prises de vue aériennes. Pour autant, l’analyse des diagrammes précédents met en évidence une diminution de la surface des prairies (de 27,7% à 20,3%) et, parallèlement, une augmentation de la taille des systèmes culturaux (de 20.2% à 27,1%). Ainsi, nous comprenons que la surface de l’espace initialement réservé aux pâturages a progressivement diminué en étant convertie en espace cultivé. Comme nous le détaillerons plus précisément dans la partie III de cette section, certains mécanismes sont directement à l’origine de ces modifications."
texte5="B - Une stabilisation de la proportion de zones boisées marquée par un développement des feuillus en bord de fleuve"
texte6="Par ailleurs, il est particulièrement intéressant de constater une augmentation notable des forêts de feuillus entre 1982 et 2008 (de 7,4% à 13,2%). Cette observation confirme ici les dynamiques d’évolution des ripisylves (formations boisées présentes sur les rives d’un cours d’eau) évoquées dans la partie précédente. On constate en effet une extension et une densification des zones boisées malgré l’augmentation parallèle de l’espace cultivé. L’évolution progressive de celles-ci explique le fait que la somme des pourcentages de “forêts de feuillus” (désignant une végétation dense) et de “forêts et végétation” (désignant une végétation moins imposante) reste finalement relativement stable au cours du temps (de 18% à 17% en quarante ans)."
texte7="C - Un développement des surfaces viticoles"
texte8="Le périmètre d’analyse est aussi caractérisé par la présence de vignes localisées en haut de coteau. Grâce à l’étude des données d’occupation du sol, on remarque une augmentation et une valorisation de ces espaces au cours du temps. Comme nous l’évoquerons en section II, la présence d’une AOC sur notre territoire est à l’origine de ce constat."

labels = ['111 - Tissu urbain continu', '112 - Tissu urbain discontinu', '122 - Réseaux routiers, ferroviaires et espaces ass.', '221 - Vignobles', '231 - Prairies et autres surf. en herbe à usage agri.', '242 - Systèmes culturaux et parcellaires complexes', '311 - Forêts de feuillus', '324 - Forêt et végétation arbustive en mutation', '331 - Plages, dunes et sable', '511 - Cours et voies d\'eau']


st.sidebar.title(propos)
st.sidebar.info(t_propos)
logo = "images/UNESCO.gif"
st.sidebar.image(logo)

st.title(titre)
st.markdown(texte1)


colors_dict = {'111': '#ff0145', '112': '#9b3f0a', '122': '#393076', '221': '#9d3fa0', 
               '231': '#b2df8a', '242': '#e5d411', '311': '#88ff00', '324': '#33a02c', 
               '331': '#f7efc7', '511': '#7ce1de'}
def colors(feature):
    clc_niv3 = str(feature['properties']['clc_niv3'])
    if clc_niv3 == '24':
        return '#e5b636'
    elif clc_niv3 in colors_dict:
        return colors_dict[clc_niv3]

def bouton(): 
  loire ='images/loire.png'
  tooltips = 'Clique aqui!'
  folium.Marker([47.396056, -0.628481], popup='<b>Loire</b><br><img src=loire style="width:128px;height:128px;"><br><a href="https://www.google.com/maps/@47.3960075,-0.6284469,3a,75y,100.44h,90t/data=!3m8!1e1!3m6!1sAF1QipOAZLT5XJoZ6A6a27JnUr1Tv75R7iqoYXF8MXZo!2e10!3e11!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipOAZLT5XJoZ6A6a27JnUr1Tv75R7iqoYXF8MXZo%3Dw203-h100-k-no-pi-0-ya87.22005-ro-0-fo100!7i9728!8i4864">Google street view</a> ',tooltip=tooltips,icon = folium.Icon(icon='star', color = 'blue')).add_to(m)
  vigne = 'images/vigne.jpg'
  folium.Marker([47.39288301234007, -0.6390056258621946], popup='<b>Vigneyard</b><br><img src=vigne style="width:128px;height:128px;"><br><a href="https://www.google.com/maps/@47.3929183,-0.6390139,3a,75y,49.9h,93.99t/data=!3m8!1e1!3m6!1sAF1QipMVC5WEVvHSvPBKYcuM__faN69QVwP-JGTVkOO1!2e10!3e11!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipMVC5WEVvHSvPBKYcuM__faN69QVwP-JGTVkOO1%3Dw203-h100-k-no-pi-0-ya56.273354-ro-0-fo100!7i8704!8i4352">Google street view</a> ', tooltip=tooltips,icon = folium.Icon(icon='star', color = 'purple')).add_to(m)
  behuard = 'images/beguard.jpg'
  folium.Marker([47.3799819,-0.6439028], popup='<b>Behuard</b><br><img src=vigne style="width:128px;height:128px;"><br><a href="https://www.google.com/maps/@47.3799819,-0.6439028,3a,90y,155.2h,91.02t/data=!3m6!1e1!3m4!1seEKAMzX_7GjWNXYhdHm2OA!2e0!7i16384!8i8192">Google street view</a> ', tooltip=tooltips,icon = folium.Icon(icon='star', color = 'red')).add_to(m)
  champ = 'images/champ.jpg'
  folium.Marker([47.3893146,-0.6244117], popup='<b>Champ</b><br><img src=vigne style="width:128px;height:128px;"><br><a href="https://www.google.com/maps/@47.3893146,-0.6244117,3a,75y,165.97h,80.27t/data=!3m7!1e1!3m5!1sO6RtFhjCeEkBh_2n8khYnQ!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fpanoid%3DO6RtFhjCeEkBh_2n8khYnQ%26cb_client%3Dmaps_sv.tactile.gps%26w%3D203%26h%3D100%26yaw%3D314.86755%26pitch%3D0%26thumbfov%3D100!7i16384!8i8192">Google street view</a> ', tooltip=tooltips,icon = folium.Icon(icon='star', color = 'orange')).add_to(m)
  foret = 'images/foret.jpg'
  folium.Marker([47.3912095,-0.6347417], popup='<b>Champ</b><br><img src=vigne style="width:128px;height:128px;"><br><a href="https://www.google.com/maps/@47.3912095,-0.6347417,3a,75y,67.05h,96.76t/data=!3m8!1e1!3m6!1sAF1QipOueBHS2GcuLtj5NO-v6rf48nTr5Nz7kif1Df0V!2e10!3e11!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipOueBHS2GcuLtj5NO-v6rf48nTr5Nz7kif1Df0V%3Dw203-h100-k-no-pi-0-ya9.331403-ro-0-fo100!7i8704!8i4352">Google street view</a> ', tooltip=tooltips,icon = folium.Icon(icon='star', color = 'green')).add_to(m)
  route = 'images/routetrain.jpg'
  folium.Marker([47.3855089,-0.6449059], popup='<b>Route et train</b><br><img src=vigne style="width:128px;height:128px;"><br><a href="https://www.google.com/maps/@47.3855089,-0.6449059,3a,75y,257.94h,85.47t/data=!3m6!1e1!3m4!1sA5qNG_T2NEffmnxay7QElQ!2e0!7i16384!8i8192">Google street view</a> ', tooltip=tooltips,icon = folium.Icon(icon='star', color = 'black')).add_to(m)

colu1, colu2 = st.columns([5, 3])
with colu2:
    color = [colors_dict[label.split()[0]] for label in labels]
    st.subheader('Legende :')
    for i, label in enumerate(labels):
         st.markdown(f'''<div style="display: flex; align-items: center;">
                    <div style="background-color: {color[i]}; width: 20px; height: 10px; margin-right: 10px;"></div>
                    <span style="font-size: 10px;">{label}</span>
                </div>''', unsafe_allow_html=True)
with colu1:
  if col1.button("Carte occupation du sol 1982"):
    land_use_map='carte/occ_1982.geojson'
    m=folium.Map(location=[47.389468, -0.633296], zoom_start=14)
    tooltip = folium.GeoJsonTooltip(fields=['clc_niv3'], aliases=['Land Use Class'])
    folium.GeoJson(land_use_map,name='land use map',style_function= lambda feature: {'fillColor':colors(feature),'fillOpacity':0.7, 'weight':0},tooltip=tooltip).add_to(m)
    bouton()
    folium_static(m, width=440, height=400)
  if col1.button("Carte occupation du sol 2008"):
    land_use_map='carte/occ_2008.geojson'
    m=folium.Map(location=[47.389468, -0.633296], zoom_start=14)
    tooltip = folium.GeoJsonTooltip(fields=['clc_niv3'], aliases=['Land Use Class'])
    folium.GeoJson(land_use_map,name='land use map',style_function= lambda feature: {'fillColor':colors(feature),'fillOpacity':0.7, 'weight':0},tooltip=tooltip).add_to(m)
    bouton()
    folium_static(m, width=440, height=400)


st.markdown(texte2)
st.subheader(texte3)
st.markdown(texte4)
st.subheader(texte5)
st.markdown(texte6)
st.subheader(texte7)
st.markdown(texte8)
