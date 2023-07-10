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
sel_an="Selectionnez une année"
titre="Une modification de l’occupation des sols depuis 40 ans témoin de changements morphologiques"
texte1="Les données cartographiques précédentes peuvent être traduites en données statistiques pour faciliter la visualisation des évolutions entre les deux périodes. Ainsi, en calculant les pourcentages de chaque type d’occupation au sein de la zone commune, on peut obtenir les diagrammes suivants."
texte2="L’étude plus précise de la répartition de l’occupation des sols d’un espace est également un moyen de mettre en évidence certaines évolutions. Après avoir abordé ces dernières avec une vision générale dans la partie précédente, nous allons à présent utiliser des données chiffrées et plus précises pour renforcer nos observations. Pour réaliser les cartes et diagrammes relatifs à l’occupation des sols de notre secteur d’étude, nous avons utilisé les photographies de 1982 et 2008 à notre disposition. Nous avons également adopté la nomenclature de niveau 3 de la base de données Corine Land Cover pour représenter et nommer les différents types d’espace."
texte3="A - Une diminution de la superficie des prairies au profit des espaces cultivés"
texte4="Grâce à l’analyse des unités paysagères, nous avons pu constater que l’espace non-urbanisé de notre périmètre n’a pas connu d’évolution notable au cours des quarante années séparant les prises de vue aériennes. Pour autant, l’analyse des diagrammes précédents met en évidence une diminution de la surface des prairies (de 27,7% à 20,3%) et, parallèlement, une augmentation de la taille des systèmes culturaux (de 20.2% à 27,1%). Ainsi, nous comprenons que la surface de l’espace initialement réservé aux pâturages a progressivement diminué en étant convertie en espace cultivé. Comme nous le détaillerons plus précisément dans la partie III de cette section, certains mécanismes sont directement à l’origine de ces modifications."
texte5="B - Une stabilisation de la proportion de zones boisées marquée par un développement des feuillus en bord de fleuve"
texte6="Par ailleurs, il est particulièrement intéressant de constater une augmentation notable des forêts de feuillus entre 1982 et 2008 (de 7,4% à 13,2%). Cette observation confirme ici les dynamiques d’évolution des ripisylves (formations boisées présentes sur les rives d’un cours d’eau) évoquées dans la partie précédente. On constate en effet une extension et une densification des zones boisées malgré l’augmentation parallèle de l’espace cultivé. L’évolution progressive de celles-ci explique le fait que la somme des pourcentages de “forêts de feuillus” (désignant une végétation dense) et de “forêts et végétation” (désignant une végétation moins imposante) reste finalement relativement stable au cours du temps (de 18% à 17% en quarante ans)."
texte7="C - Un développement des surfaces viticoles"
texte8="Le périmètre d’analyse est aussi caractérisé par la présence de vignes localisées en haut de coteau. Grâce à l’étude des données d’occupation du sol, on remarque une augmentation et une valorisation de ces espaces au cours du temps. Comme nous l’évoquerons en section II, la présence d’une AOC sur notre territoire est à l’origine de ce constat."

labels = ['111 - Tissu urbain continu', '112 - Tissu urbain discontinu', '122 - Réseaux routiers, ferroviaires et espaces ass.', '221 - Vignobles', '231 - Prairies et autres surf. en herbe à usage agri.','242 - Systèmes culturaux et parcellaires complexes', '311 - Forêts de feuillus', '324 - Forêt et végétation arbustive en mutation', '331 - Plages, dunes et sable', '511 - Cours et voies d\'eau']
opp_dict = {'111': 0, '112': 0, '122': 0, '221': 0, '231': 0, '242': 0, '311': 0, '324': 0,'331': 0, '511': 0}
colors_dict = {'111': '#ff0145', '112': '#9b3f0a', '122': '#393076', '221': '#9d3fa0', 
               '231': '#b2df8a', '242': '#e5d411', '311': '#88ff00', '324': '#33a02c', 
               '331': '#f7efc7', '511': '#7ce1de'}
legende='Legende :'
texte_unite='Ocuppation des sols : '
source="Sources: Sur base de deux photographies aériennes, IGN Nomenclature Corine Land Cover de niveau 3"
if langue == 'Portugues':
  propos = "Sobre"
  t_propos = """[Projeto Multidisciplinar](https://drive.google.com/file/d/1AAZHmcbd7jpFdqhTs5pqXbZqaX4RELUS/view?usp=sharing)
  
  Realizado por: Adèle Coatanéa, Quentin Boivin, Amine Bastaoui, Isabella Wokam, Eliot Bertthié, Danielle Babi
  
  Site: Adèle Coatanéa"""
  titre = "Uma modificação na ocupação do solo nos últimos 40 anos reflete mudanças morfológicas"
  texte1 = "O estudo mais preciso da distribuição da ocupação do solo de um espaço também é uma maneira de destacar certas evoluções. Depois de abordar essas últimas com uma visão geral na parte anterior, agora vamos usar dados numéricos mais precisos para reforçar nossas observações. Para criar mapas e diagramas relacionados à ocupação do solo de nossa área de estudo, utilizamos as fotografias de 1982 e 2008 disponíveis para nós. Também adotamos a nomenclatura de nível 3 da base de dados Corine Land Cover para representar e nomear os diferentes tipos de espaço."
  texte2 = "Os dados cartográficos anteriores podem ser traduzidos em dados estatísticos para facilitar a visualização das mudanças entre os dois períodos. Assim, ao calcular as porcentagens de cada tipo de uso da terra dentro da área comum, é possível obter os seguintes diagramas."
  texte3 = "A - Uma diminuição da área de pastagens em favor de áreas cultivadas"
  texte4 = "Por meio da análise das unidades paisagísticas, constatamos que a área não urbanizada de nosso perímetro não sofreu mudanças significativas ao longo dos quarenta anos que separam as imagens aéreas. No entanto, a análise dos diagramas anteriores revela uma diminuição na superfície das pastagens (de 27,7% para 20,3%) e, ao mesmo tempo, um aumento no tamanho dos sistemas culturais (de 20,2% para 27,1%). Assim, compreendemos que a área originalmente reservada para pastagens diminuiu gradualmente, sendo convertida em áreas cultivadas. Como detalharemos mais precisamente na Parte III desta seção, certos mecanismos são diretamente responsáveis por essas mudanças."
  texte5 = "B - Uma estabilização da proporção de áreas florestadas marcada pelo desenvolvimento de folhosas nas margens do rio"
  texte6 = "Além disso, é particularmente interessante observar um aumento significativo nas florestas de folhosas entre 1982 e 2008 (de 7,4% para 13,2%). Essa observação confirma as dinâmicas de evolução das matas ciliares (formações florestais presentes nas margens de um curso d'água) mencionadas na parte anterior. De fato, observa-se uma expansão e densificação das áreas florestadas, apesar do aumento paralelo das áreas cultivadas. A evolução progressiva dessas áreas explica o fato de a soma das porcentagens de 'florestas de folhosas' (que indicam uma vegetação densa) e de 'florestas e vegetação' (que indicam uma vegetação menos imponente) permanecer relativamente estável ao longo do tempo (de 18% para 17% em quarenta anos)."
  texte7 = "C - Um desenvolvimento das áreas de vinhas"
  texte8 = "A área de análise também é caracterizada pela presença de vinhas localizadas no topo do morro. Através do estudo dos dados de ocupação do solo, observamos um aumento e valorização dessas áreas ao longo do tempo. Como mencionaremos na Seção II, a presença de uma AOC em nosso território é a causa desse fato."
  sel_an = "Selecione um ano"
  legende = 'Legenda:'
  labels = ['111 - Tecido urbano contínuo', '112 - Tecido urbano descontínuo', '122 - Redes viárias, ferroviárias e espaços associados', '221 - Vinhas', '231 - Pastagens e outras áreas herbáceas para uso agrícola', 
            '242 - Sistemas culturais e parcelares complexos', '311 - Florestas de folhosas', '324 - Floresta e vegetação arbustiva em mutação', '331 - Praias, dunas e areia', "511 - Cursos e vias d'água"]
  texte_unite = 'Uso do Solo: '
  source = "Fontes: Com base em duas fotografias aéreas, IGN Nomenclatura Corine Land Cover de nível 3"

if langue =='English':
  propos = "About"
  t_propos = """[Interdisciplinary Project](https://drive.google.com/file/d/1AAZHmcbd7jpFdqhTs5pqXbZqaX4RELUS/view?usp=sharing)
  
  Realized by: Adèle Coatanéa, Quentin Boivin, Amine Bastaoui, Isabella Wokam, Eliot Bertthié, Danielle Babi
  
  Website: Adèle Coatanéa"""
  titre = "Changes in Land Use Over 40 Years as Evidence of Morphological Transformations"
  texte1 = "A more precise study of land use distribution in an area is also a means of highlighting certain evolutions. After addressing these with a general overview in the previous section, we will now use numerical data to reinforce our observations. To create maps and diagrams related to land use in our study area, we used the available photographs from 1982 and 2008. We also adopted the level 3 nomenclature of the Corine Land Cover database to represent and name different types of areas."
  texte2 = "The previous cartographic data can be translated into statistical data to facilitate the visualization of changes between the two periods. Thus, by calculating the percentages of each type of land use within the common area, the following diagrams can be obtained."
  texte3 = "A - Decrease in the area of meadows in favor of cultivated spaces"
  texte4 = "Through the analysis of landscape units, we observed that the non-urbanized space within our perimeter did not undergo significant changes over the forty-year period between aerial photographs. However, the analysis of the previous diagrams reveals a decrease in the surface area of meadows (from 27.7% to 20.3%) and, simultaneously, an increase in the size of agricultural systems (from 20.2% to 27.1%). Thus, we understand that the area initially reserved for pastures has gradually diminished and been converted into cultivated space. As we will detail more precisely in Part III of this section, certain mechanisms are directly responsible for these modifications."
  texte5 = "B - Stabilization of the proportion of wooded areas marked by the development of deciduous trees along the riverbank"
  texte6 = "Moreover, it is particularly interesting to note a significant increase in deciduous forests between 1982 and 2008 (from 7.4% to 13.2%). This observation confirms the dynamics of riparian forests (wooded formations along the riverbanks) mentioned in the previous section. Despite the parallel increase in cultivated space, there is indeed an expansion and densification of wooded areas. The gradual evolution of these areas explains why the sum of the percentages of 'deciduous forests' (indicating dense vegetation) and 'forests and vegetation' (indicating less imposing vegetation) remains relatively stable over time (from 18% to 17% over forty years)."
  texte7 = "C - Development of vineyard areas"
  texte8 = "The analysis perimeter is also characterized by the presence of vineyards located on the upper slopes. Through the study of land use data, we can observe an increase and valorization of these areas over time. As we will discuss in Section II, the presence of an Appellation of Origin Control (AOC) in our territory is the reason behind this finding."
  sel_an = "Select a year"
  labels = ['111 - Continuous urban fabric', '112 - Discontinuous urban fabric', '122 - Road networks, railways, and associated land', '221 - Vineyards', '231 - Grassland and other areas used for agriculture', '242 - Complex cultivation patterns and parcels', '311 - Deciduous forests', '324 - Forests and transitional woodland', '331 - Beaches, dunes, and sand', '511 - Water courses and waterways']
  legende = 'Legend:'
  texte_unite = "Land Use: "
  source ="Sources: Based on two aerial photographs, IGN Corine Land Cover Level 3 Nomenclature"

st.sidebar.title(propos)
st.sidebar.info(t_propos)
logo = "images/UNESCO.gif"
st.sidebar.image(logo)

st.title(titre)
st.markdown(texte1)

annee = st.selectbox(sel_an, ["1982", "2008"])
co1, co2, co3, co4, co5 = st.columns(5)
for i, label in enumerate(labels):
  if i in [0,5]:
    column = co1
  if i in [1,6]:
    column=co2
  if i in [2,7]:
    column=co3
  if i in [3,8]:
    column=co4
  if i in [4,9]:
    column=co5
  show_label = column.checkbox(label.split(' - ')[1])
  if show_label:
    opp_dict[label.split(' - ')[0]] = 0.7
if annee == "1982":
  land_use_map = 'carte/occ_1982.geojson'
elif annee == "2008":
  land_use_map = 'carte/occ_2008.geojson'


def colors(feature):
  clc_niv3 = str(feature['properties']['clc_niv3'])
  if clc_niv3=='24':
    return colors_dict['324']
  if clc_niv3=='241':
    return colors_dict['242']
  if clc_niv3 in opp_dict:
    return colors_dict[clc_niv3]

def opacite(feature):
  clc_niv3 = str(feature['properties']['clc_niv3'])
  if clc_niv3=='24':
    return opp_dict['324']
  if clc_niv3=='241':
    return opp_dict['242']
  if clc_niv3 in opp_dict:
    return opp_dict[clc_niv3]

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
  st.subheader(legende)
  for i, label in enumerate(labels):
    st.markdown(f'''<div style="display: flex; align-items: center;"><div style="background-color: {color[i]}; width: 20px; height: 10px; margin-right: 10px;"></div><span style="font-size: 10px;">{label}</span></div>''', unsafe_allow_html=True)
with colu1:
  m=folium.Map(location=[47.389468, -0.633296], zoom_start=14)
  tooltip = folium.GeoJsonTooltip(fields=['clc_niv3'], aliases=[texte_unite])
  folium.GeoJson(land_use_map,name='land use map',style_function= lambda feature: {'fillColor':colors(feature),'fillOpacity':opacite(feature), 'weight':0},tooltip=tooltip).add_to(m)
  bouton()
  folium_static(m, width=440, height=400)
 
st.markdown(f'''<span style="font-size: 10px; font-style: italic;">{source}</span>''', unsafe_allow_html=True)  

st.markdown(texte2)
st.subheader(texte3)
st.markdown(texte4)
st.subheader(texte5)
st.markdown(texte6)
st.subheader(texte7)
st.markdown(texte8)
