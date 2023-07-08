import streamlit as st
import leafmap.foliumap as leafmap
import folium
from streamlit_folium import folium_static



st.set_page_config(page_title='Projet Pluridisciplinaire',
    page_icon="🗺️",
)

langue = st.sidebar.selectbox('langue',["Francais", "English", "Portugues"])

propos="A propos"
t_propos="""
[Projet Pluridisciplinaire](https://drive.google.com/file/d/1AAZHmcbd7jpFdqhTs5pqXbZqaX4RELUS/view?usp=sharing)

Réalisé par : Adèle Coatanéa, Quentin Boivin, Amine Bastaoui, Isabella Wokam, Eliot Bertthié, Danielle Babi

Site: Adèle Coatanéa
"""
titre="L’identification de grandes unités paysagères; un moyen de caractériser globalement les paysages actuels et passés"
texte1="L’un des premiers modes d’analyse du paysage pouvant être mis en place dans le but d’étudier l’agencement et la composition d’un secteur est l’identification d’unités paysagères. Celles-ci sont définies par le site Web de Géoconfluences comme des “portion[s] d'espace constituant un ensemble relativement homogène sur le plan de la topographie, de l'utilisation de l'espace et de la couverture végétale ou de l'occupation humaine”. Au sein de la zone du Val de Loire que nous analysons grâce aux travaux photogrammétriques, différents grands ensembles apparaissent en effet sur les photographies aériennes (tant au début des années 80 qu’à la fin des années 2000). Leur identification permet alors de caractériser notre périmètre d’étude et de mettre en évidence les changements globaux."
sel_an="Selectionnez une année"
texte2="L’un des points marquants mis en évidence par ces deux cartes concerne l’évolution de la morphologie des éléments paysagers au sein même du lit de la Loire. En effet, le caractère particulièrement changeant et imprévisible du fleuve est à l’origine de sa réputation populaire de “dernier fleuve sauvage d’Europe”. Ainsi, nous observons aisément une radicale différence entre les formes et dispositions des zones d'atterrissement sableux actuels et passés. Les mécanismes à l'origine de ces évolutions sont connus. Parmi eux, on peut entre autres citer une succession de crues violentes au cours des dernières décennies et une extraction de sable importante pendant une longue période (à l’origine d’un creusement progressif du lit du fleuve). Néanmoins, on constate que la morphologie globale de la Loire n’a pas subi d’évolution particulièrement notable sur la portion que nous étudions. Il en est de même pour un de ses bras, le Louet, également visible au sein de notre périmètre d’étude."
texte3="B - Une augmentation de la taille des zones bâties"
texte4="Par ailleurs, on peut remarquer un élargissement des espaces couverts par un tissu urbanisé en une quarantaine d’années. Ce phénomène n’a bien sûr rien d’étonnant car l’augmentation démographique partout en France depuis plusieurs décennies est un élément avéré. Il se traduit ici, d’un point de vue paysager, par une densification et une augmentation des zones bâties."
texte5="C - Un phénomène de linéarisation des zones boisées en bord de Loire"
texte6="De plus, l’un des éléments à noter ici (bien que moins marqué que sur d’autres zones du Val de Loire) est la linéarisation et le développement des zones boisées en bord de fleuve. Lors de cette première approche globale, ce processus d’évolution est surtout visible si l’on observe l’unité paysagère “Coteau boisé de la commune de Savennières” qui a connu une modification en quarante ans."
texte7="D - Un maintien de l’emprise générale des prairies, zones agricoles et zones boisées de part et d’autre du fleuve"
texte8="Dans le même temps, on constate que la superficie générale des zones non-urbanisées n’a pas connu d’évolution majeure entre 1982 et 2008. Ainsi, nous pouvons dores et déjà affirmer que le secteur photogrammétrique sur lequel va se baser une grande partie de notre travail n’est pas caractérisé par des évolutions paysagères fortes."
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
if langue =='English':
    propos = "About"
    t_propos = """
    [Interdisciplinary Project](https://drive.google.com/file/d/1AAZHmcbd7jpFdqhTs5pqXbZqaX4RELUS/view?usp=sharing)
    
    Realized by: Adèle Coatanéa, Quentin Boivin, Amine Bastaoui, Isabella Wokam, Eliot Bertthié, Danielle Babi
    
    Website: Adèle Coatanéa
    """
    titre = "Identifying Large Landscape Units: A Means to Globally Characterize Current and Past Landscapes"
    texte1 = "One of the first methods for analyzing a landscape and studying its arrangement and composition is to identify landscape units. According to the Géoconfluences website, these units are defined as 'portions of space that constitute a relatively homogeneous ensemble in terms of topography, land use, vegetation cover, or human occupation.' Within the Val de Loire area that we are studying using photogrammetric works, different large ensembles are visible on aerial photographs, both from the early 1980s and the late 2000s. Identifying these units allows us to characterize our study area and highlight global changes."
    sel_an = "Select a year"
    texte2 = "One notable point highlighted by these two maps concerns the evolution of the morphology of landscape elements within the bed of the Loire River. The particularly changing and unpredictable nature of the river has earned it the popular reputation of being the 'last wild river in Europe.' Thus, we can easily observe a radical difference between the forms and arrangements of the current and past sandy landing areas. The mechanisms behind these changes are known. Among them, we can mention a series of violent floods in recent decades and extensive sand extraction over a long period (resulting in a gradual deepening of the river bed). However, we note that the overall morphology of the Loire has not undergone any particularly notable changes in the portion we are studying. The same applies to one of its branches, the Louet, which is also visible within our study area."
    texte3 = "B - An increase in the size of built-up areas"
    texte4 = "Furthermore, we can observe an expansion of areas covered by urban fabric over a forty-year period. This phenomenon is not surprising, as population growth throughout France in recent decades is well established. From a landscape perspective, it is manifested by densification and an increase in built-up areas."
    texte5 = "C - Linearization of wooded areas along the Loire River"
    texte6 = "Moreover, one noteworthy element here (although less pronounced than in other areas of the Val de Loire) is the linearization and development of wooded areas along the river. During this initial comprehensive approach, this process of evolution is particularly visible when observing the 'Wooded slope of the municipality of Savennières' landscape unit, which has undergone changes over forty years."
    texte7 = "D - Maintenance of the overall extent of meadows, agricultural areas, and wooded areas on both sides of the river"
    texte8 = "At the same time, we can observe that the general area of non-urbanized zones has not undergone major changes between 1982 and 2008. Thus, we can already affirm that the photogrammetric sector, which will be the basis for a large part of our work, is not characterized by strong landscape changes."
    labels = ['1 - Vineyard Plateau',
              '5 - Wooded Slope',
              '12 - Wooded Alluvial Terrace',
              '11 - Semi-Bocage Alluvial Terrace',
              '3 - Semi-Bocage Alluvial Terrace',
              '4 - Bocage Meadows on Alluvial Terrace',
              '2 - Savennières Village',
              '9 - Denée Village',
              '6 - Road and Railway Network',
              '7 - Loire Riverbed',
              '10 - Sediment Deposits',
              '8 - Loire Branch']

if langue =='Portugues': 
    propos="A propos3"

markdown = t_propos

st.sidebar.title(propos)
st.sidebar.info(markdown)
logo = "images/UNESCO.gif"


st.sidebar.image(logo)
opp_dict = {'1': 0, '5': 0, '12': 0,'11': 0, '3': 0, '4': 0,'2': 0, '9': 0, '6': 0,'7': 0, '10': 0, '8': 0,'13': 0}



st.title(titre)
colors_dict = {'1': '#ffb266ff', '5': '#769674ff', '12': '#9cf5a2ff',
               '11': '#91cd96ff', '3': '#ccedb4ff', '4': '#8ff17eff',
               '2': '#b894e3ff', '9': '#c1b1d4ff', '6': '#d5676bff',
               '7': '#90befaff', '10': '#f4eeeaff', '8': '#90eefaff','13': '#769674ff'}

st.markdown(texte1)
annee = st.selectbox(sel_an, ["1982", "2008"])
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
  
st.subheader(texte1)
st.markdown(texte2)
st.subheader(texte3)
st.markdown(texte4)
st.subheader(texte5)
st.markdown(texte6)
st.subheader(texte7)
st.markdown(texte8)
