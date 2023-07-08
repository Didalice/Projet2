import streamlit as st
import leafmap.foliumap as leafmap
import folium
from streamlit_folium import folium_static

# Variable de langue
langue = st.sidebar.selectbox(["Francais", "English", "Portugues"])

st.set_page_config(page_title="Projet Pluridisciplinaire",
    page_icon="🗺️",
)

markdown = """
[Projet Pluridisciplinaire](https://drive.google.com/file/d/1AAZHmcbd7jpFdqhTs5pqXbZqaX4RELUS/view?usp=sharing)

Réalisé par : Adèle Coatanéa, Quentin Boivin, Amine Bastaoui, Isabella Wokam, Eliot Bertthié, Danielle Babi

Site: Adèle Coatanéa
"""

st.sidebar.title("A propos")
st.sidebar.info(markdown)
logo = "images/UNESCO.gif"


st.sidebar.image(logo)
opp_dict = {'1': 0, '5': 0, '12': 0,'11': 0, '3': 0, '4': 0,'2': 0, '9': 0, '6': 0,'7': 0, '10': 0, '8': 0,'13': 0}
labels=['1 - Plateau viticole',
            '5 - Coteau boisé',
            '12 - Terrasse alluviale boisée',
            '11 - Terrasse alluviale agricole semi-bocagère',
            '3 - Terrasse alluviale agricole semi-bocagère',
            '4 - Prairies bocagères sur la terrasse alluviale',
            '2 - Village de Savennières',
            '9 - Village de Denée',
            '6 - Réseau routier et ferroviaire',
            '7 - Lit de la Loire',
            '10 - Dépôts de sédiments',
            '8 - Bras de la Loire']




st.title("L’identification de grandes unités paysagères; un moyen de caractériser globalement les paysages actuels et passés")
colors_dict = {'1': '#ffb266ff', '5': '#769674ff', '12': '#9cf5a2ff',
               '11': '#91cd96ff', '3': '#ccedb4ff', '4': '#8ff17eff',
               '2': '#b894e3ff', '9': '#c1b1d4ff', '6': '#d5676bff',
               '7': '#90befaff', '10': '#f4eeeaff', '8': '#90eefaff','13': '#769674ff'}

st.markdown("L’un des premiers modes d’analyse du paysage pouvant être mis en place dans le but d’étudier l’agencement et la composition d’un secteur est l’identification d’unités paysagères. Celles-ci sont définies par le site Web de Géoconfluences comme des “portion[s] d'espace constituant un ensemble relativement homogène sur le plan de la topographie, de l'utilisation de l'espace et de la couverture végétale ou de l'occupation humaine”. Au sein de la zone du Val de Loire que nous analysons grâce aux travaux photogrammétriques, différents grands ensembles apparaissent en effet sur les photographies aériennes (tant au début des années 80 qu’à la fin des années 2000). Leur identification permet alors de caractériser notre périmètre d’étude et de mettre en évidence les changements globaux.")
annee = st.selectbox("Sélectionnez une année", ["1982", "2008"])
if annee == "1982":
            land_use_map = 'carte/pays_1982.geojson'
elif annee == "2008":
            land_use_map = 'carte/pays_2008.geojson'
def opacite(feature):
            chaine=str(feature['properties'].values())
            cle=str(chaine.split('[')[1].split(']')[0])
            #return opp_dict[cle]
            return 0.7
def colors(feature):
    chaine=str(feature['properties'].values())
    cle=str(chaine.split('[')[1].split(']')[0])
    return colors_dict[cle]
def bouton(): 
    loire ='images/loire.png'
    tooltips = 'Clique aqui!'
    folium.Marker([47.396056, -0.628481],
                  popup='<b>Loire</b><br><img src="{}" style="width:128px;height:128px;"><br><a href="https://www.google.com/maps/@47.3960075,-0.6284469,3a,75y,100.44h,90t/data=!3m8!1e1!3m6!1sAF1QipOAZLT5XJoZ6A6a27JnUr1Tv75R7iqoYXF8MXZo!2e10!3e11!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipOAZLT5XJoZ6A6a27JnUr1Tv75R7iqoYXF8MXZo%3Dw203-h100-k-no-pi-0-ya87.22005-ro-0-fo100!7i9728!8i4864">Google Street View</a>'.format(loire),
                  tooltip=tooltips,
                  icon=folium.Icon(icon='star', color='blue')).add_to(m)
    folium.Marker([47.396056, -0.628481], popup='<b>Loire</b><br><img src=loire style="width:128px;height:128px;"><br><a href="https://www.google.com/maps/@47.3960075,-0.6284469,3a,75y,100.44h,90t/data=!3m8!1e1!3m6!1sAF1QipOAZLT5XJoZ6A6a27JnUr1Tv75R7iqoYXF8MXZo!2e10!3e11!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipOAZLT5XJoZ6A6a27JnUr1Tv75R7iqoYXF8MXZo%3Dw203-h100-k-no-pi-0-ya87.22005-ro-0-fo100!7i9728!8i4864">Google street view</a> ',tooltip=tooltips,icon = folium.Icon(icon='star', color = 'blue')).add_to(m)
    vigne = 'images/vigne.jpg'
    folium.Marker([47.39288301234007, -0.6390056258621946], popup='<b>Vigneyard</b><br><img src=vigne style="width:128px;height:128px;"><br><a href="https://www.google.com/maps/@47.3929183,-0.6390139,3a,75y,49.9h,93.99t/data=!3m8!1e1!3m6!1sAF1QipMVC5WEVvHSvPBKYcuM__faN69QVwP-JGTVkOO1!2e10!3e11!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipMVC5WEVvHSvPBKYcuM__faN69QVwP-JGTVkOO1%3Dw203-h100-k-no-pi-0-ya56.273354-ro-0-fo100!7i8704!8i4352">Google street view</a> ', tooltip=tooltips,icon = folium.Icon(icon='star', color = 'purple')).add_to(m)
    behuard = 'images/beguard.jpg'
    folium.Marker([47.3799819,-0.6439028], popup='<b>Behuard</b><br><img src=behuard style="width:128px;height:128px;"><br><a href="https://www.google.com/maps/@47.3799819,-0.6439028,3a,90y,155.2h,91.02t/data=!3m6!1e1!3m4!1seEKAMzX_7GjWNXYhdHm2OA!2e0!7i16384!8i8192">Google street view</a> ', tooltip=tooltips,icon = folium.Icon(icon='star', color = 'red')).add_to(m)
    champ = 'images/champ.jpg'
    folium.Marker([47.3893146,-0.6244117], popup='<b>Champ</b><br><img src=champ style="width:128px;height:128px;"><br><a href="https://www.google.com/maps/@47.3893146,-0.6244117,3a,75y,165.97h,80.27t/data=!3m7!1e1!3m5!1sO6RtFhjCeEkBh_2n8khYnQ!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fpanoid%3DO6RtFhjCeEkBh_2n8khYnQ%26cb_client%3Dmaps_sv.tactile.gps%26w%3D203%26h%3D100%26yaw%3D314.86755%26pitch%3D0%26thumbfov%3D100!7i16384!8i8192">Google street view</a> ', tooltip=tooltips,icon = folium.Icon(icon='star', color = 'orange')).add_to(m)
    foret = 'images/foret.jpg'
    folium.Marker([47.3912095,-0.6347417], popup='<b>Champ</b><br><img src=foret style="width:128px;height:128px;"><br><a href="https://www.google.com/maps/@47.3912095,-0.6347417,3a,75y,67.05h,96.76t/data=!3m8!1e1!3m6!1sAF1QipOueBHS2GcuLtj5NO-v6rf48nTr5Nz7kif1Df0V!2e10!3e11!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipOueBHS2GcuLtj5NO-v6rf48nTr5Nz7kif1Df0V%3Dw203-h100-k-no-pi-0-ya9.331403-ro-0-fo100!7i8704!8i4352">Google street view</a> ', tooltip=tooltips,icon = folium.Icon(icon='star', color = 'green')).add_to(m)
    route = 'images/routetrain.jpg'
    folium.Marker([47.3855089,-0.6449059], popup='<b>Route et train</b><br><img src=route style="width:128px;height:128px;"><br><a href="https://www.google.com/maps/@47.3855089,-0.6449059,3a,75y,257.94h,85.47t/data=!3m6!1e1!3m4!1sA5qNG_T2NEffmnxay7QElQ!2e0!7i16384!8i8192">Google street view</a> ', tooltip=tooltips,icon = folium.Icon(icon='star', color = 'black')).add_to(m)
col1, col2, col3 = st.columns(3)

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
            m=folium.Map(location=[47.389468, -0.633296], zoom_start=14)
            tooltip = folium.GeoJsonTooltip(fields=['Unité'], aliases=['Land Use Class'])
            folium.GeoJson(land_use_map,name='land use map',style_function= lambda feature: {'fillColor':colors(feature),'fillOpacity':opacite(feature), 'weight':0},tooltip=tooltip).add_to(m)
            bouton()
            folium_static(m, width=440, height=400)
  
st.subheader("A - Une évolution des éléments du lit de la Loire")
st.markdown("L’un des points marquants mis en évidence par ces deux cartes concerne l’évolution de la morphologie des éléments paysagers au sein même du lit de la Loire. En effet, le caractère particulièrement changeant et imprévisible du fleuve est à l’origine de sa réputation populaire de “dernier fleuve sauvage d’Europe”. Ainsi, nous observons aisément une radicale différence entre les formes et dispositions des zones d'atterrissement sableux actuels et passés. Les mécanismes à l'origine de ces évolutions sont connus. Parmi eux, on peut entre autres citer une succession de crues violentes au cours des dernières décennies et une extraction de sable importante pendant une longue période (à l’origine d’un creusement progressif du lit du fleuve). Néanmoins, on constate que la morphologie globale de la Loire n’a pas subi d’évolution particulièrement notable sur la portion que nous étudions. Il en est de même pour un de ses bras, le Louet, également visible au sein de notre périmètre d’étude.")
st.subheader("B - Une augmentation de la taille des zones bâties")
st.markdown("Par ailleurs, on peut remarquer un élargissement des espaces couverts par un tissu urbanisé en une quarantaine d’années. Ce phénomène n’a bien sûr rien d’étonnant car l’augmentation démographique partout en France depuis plusieurs décennies est un élément avéré. Il se traduit ici, d’un point de vue paysager, par une densification et une augmentation des zones bâties.")
st.subheader("C - Un phénomène de linéarisation des zones boisées en bord de Loire")
st.markdown("De plus, l’un des éléments à noter ici (bien que moins marqué que sur d’autres zones du Val de Loire) est la linéarisation et le développement des zones boisées en bord de fleuve. Lors de cette première approche globale, ce processus d’évolution est surtout visible si l’on observe l’unité paysagère “Coteau boisé de la commune de Savennières” qui a connu une modification en quarante ans.")
st.subheader("D - Un maintien de l’emprise générale des prairies, zones agricoles et zones boisées de part et d’autre du fleuve")
st.markdown("Dans le même temps, on constate que la superficie générale des zones non-urbanisées n’a pas connu d’évolution majeure entre 1982 et 2008. Ainsi, nous pouvons dores et déjà affirmer que le secteur photogrammétrique sur lequel va se baser une grande partie de notre travail n’est pas caractérisé par des évolutions paysagères fortes.")

