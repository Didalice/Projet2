import streamlit as st
import leafmap.foliumap as leafmap
import folium
from streamlit_folium import folium_static
#import matplotlib.pyplot as plt


markdown = """
[Projet Pluridisciplinaire](https://drive.google.com/file/d/1AAZHmcbd7jpFdqhTs5pqXbZqaX4RELUS/view?usp=sharing)

Réalisé par : Adèle Coatanéa, Quentin Boivin, Amine Bastaoui, Isabella Wokam, Eliot Bertthié, Danielle Babi

Site: Adèle Coatanéa
"""

st.sidebar.title("A propos")
st.sidebar.info(markdown)
logo = "images/UNESCO.gif"
st.sidebar.image(logo)

st.title("L’identification de grandes unités paysagères; un moyen de caractériser globalement les paysages actuels et passés")
colors_dict = {'1': '#ffb266ff', '2': '#769674ff', '3': '#9cf5a2ff',
               '4': '#91cd96ff', '5': '#ccedb4ff', '6': '#8ff17eff',
               '7': '#b894e3ff', '8': '#c1b1d4ff', '9': '#d5676bff',
               '10': '#90befaff', '11': '#f4eeeaff', '12': '#90eefaff'}

def colors(feature):
    Unité = str(feature['properties']['Unité'])
    return colors_dict[Unité]
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

colu1, colu2 = st.columns([3, 3])

with colu2:
    labels=['1 - Plateau viticole de la commune de Savennières',
            '2 - Coteau boisé de la commune de Savennières',
            '3 - Terrasse alluviale boisée de la commune de Savennières',
            '4 - Terrasse alluviale agricole semi-bocagère de la commune de Denée',
            '5 - Terrasse alluviale agricole semi-bocagère de l\'île de la commune de Béhuard',
            '6 - Prairies bocagères sur la terrasse alluviale de la commune de Denée',
            '7 - Village de Savennières',
            '8 - Village de Denée',
            '9 - Réseau routier et ferroviaire',
            '10 - Lit de la Loire',
            '11 - Dépôts de sédiments dans le lit de la Loire',
            '12 - Bras de la Loire']
    color = [colors_dict[label.split()[0]] for label in labels]
    st.subheader('Legende :')
    for i, label in enumerate(labels):
        st.markdown(f'''<div style="display: flex; align-items: center;"> <div style="background-color: {color[i]}; width: 20px; height: 20px; margin-right: 10px;"></div><span>{label}</span></div>''', unsafe_allow_html=True)


with colu1:
  if col1.button("Carte unité paysagère 1982"):
    land_use_map='carte/pays_1982.geojson'
    m=folium.Map(location=[47.389468, -0.633296], zoom_start=14)
    tooltip = folium.GeoJsonTooltip(fields=['Unité'], aliases=['Land Use Class'])
    folium.GeoJson(land_use_map,name='land use map',style_function= lambda feature: {'fillColor':colors(feature),'fillOpacity':0.7, 'weight':0},tooltip=tooltip).add_to(m)
    bouton()
    folium_static(m, width=470, height=400)
  if col1.button("Carte unité paysagère 2008"):
    land_use_map='carte/pays_2008.geojson'
    m=folium.Map(location=[47.389468, -0.633296], zoom_start=14)
    tooltip = folium.GeoJsonTooltip(fields=['Unité'], aliases=['Land Use Class'])
    folium.GeoJson(land_use_map,name='land use map',style_function= lambda feature: {'fillColor':colors(feature),'fillOpacity':0.7, 'weight':0},tooltip=tooltip).add_to(m)
    bouton()
    folium_static(m, width=470, height=400)

