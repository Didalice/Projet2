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
titre="Divers mécanismes à l’origine de ces évolutions"
texte1="Nous allons maintenant évoquer les grands mécanismes à l’origine des évolutions morphologiques observées. Cela revient à mettre en évidence les systèmes agraires choisis ainsi que les modes de réflexion quant à la question paysagère au cours des décennies."
texte2="Carte paysages visibles 1982"
texte3="Carte paysages visibles 2008"
texte4="A - L’impact d’une unification de l’agriculture au cours du temps"
texte5="Les modes de pratique agricole ont évolué depuis plusieurs siècles. Durant les cinquante dernières années, la mécanisation progressive de l’agriculture a induit une augmentation du nombre et de la taille des champs cultivés partout en France. Notre secteur n’échappe pas à la règle même si les changements morphologiques induits restent relativement limités. On remarque en effet une augmentation de la taille des différentes parcelles agricoles tout particulièrement sur la zone au sud de la Loire."
texte6="B - Une diminution de la visibilité paysagère induite par le développement des zones boisées"
texte7="Par ailleurs, l’évolution de la morphologie des paysages a un impact direct sur la perception du territoire aux abords des cours d’eau. Comme le met en évidence le cône de visibilité ci-après, le développement des ripisylves a pour effet de limiter considérablement la vue sur le paysage (voir aussi Annexe n°3). Ainsi, une question se pose naturellement ; faut-il engager des actions visant à limiter le développement de ces zones boisées ou au contraire encourager cette évolution ?"


if langue == 'Portugues':
  propos = "Sobre"
  t_propos = """[Projeto Multidisciplinar](https://drive.google.com/file/d/1AAZHmcbd7jpFdqhTs5pqXbZqaX4RELUS/view?usp=sharing)
  
  Realizado por: Adèle Coatanéa, Quentin Boivin, Amine Bastaoui, Isabella Wokam, Eliot Bertthié, Danielle Babi
  
  Site: Adèle Coatanéa"""

if langue =='English':
  propos = "About"
  t_propos = """[Interdisciplinary Project](https://drive.google.com/file/d/1AAZHmcbd7jpFdqhTs5pqXbZqaX4RELUS/view?usp=sharing)
  
  Realized by: Adèle Coatanéa, Quentin Boivin, Amine Bastaoui, Isabella Wokam, Eliot Bertthié, Danielle Babi
  
  Website: Adèle Coatanéa"""


st.sidebar.title(propos)
st.sidebar.info(t_propos)
logo = "images/UNESCO.gif"
st.sidebar.image(logo)

st.title(titre)
st.markdown(texte1)


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
  
col1, col2, col3 = st.columns(3)

if col1.button(texte2):
  land_use_map='carte/pays_visibles_1982.geojson'
  m=folium.Map(location=[47.389468, -0.633296], zoom_start=14)
  folium.GeoJson(land_use_map,name='land use map',style_function= lambda feature: {'fillColor':'#e6004dff','fillOpacity':1, 'weight':0}).add_to(m)
  bouton()
  folium_static(m)


if col1.button(texte3):
  land_use_map='carte/pays_visibles_2008.geojson'
  m=folium.Map(location=[47.389468, -0.633296], zoom_start=14)
  folium.GeoJson(land_use_map,name='land use map',style_function= lambda feature: {'fillColor':'#e6004dff','fillOpacity':1, 'weight':0}).add_to(m)
  bouton()
  folium_static(m)

st.subheader(texte4)
st.markdown(texte5)
st.subheader(texte6)
st.markdown(texte7)
