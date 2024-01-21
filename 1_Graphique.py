import streamlit as st
from matplotGraphs import figureComparaison, figureConsommation, figureTeleviseurs
import mpld3
import streamlit.components.v1 as components
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title="Projet DATA", page_icon="📟", layout="wide", initial_sidebar_state="expanded")
add_logo(r"images/cat-64.png", height=50)

figureTeleviseursHtml = mpld3.fig_to_html(figureTeleviseurs)
figureComparaisonHtml = mpld3.fig_to_html(figureComparaison)
figureConsommationHtml = mpld3.fig_to_html(figureConsommation)

st.markdown('<h1 style="text-align: center;">Etude sur la consommation d\'électricité de différents appareils en '
            'France</h1>', unsafe_allow_html=True)

columns1, columns2, columns3 = st.columns(3)
with columns2:
    st.markdown('<h4 style="text-align: center;">Sur la période avril 2019 - avril 2020</h4>', unsafe_allow_html=True)
    st.divider()

with st.sidebar:
    st.header("Les graphiques sont interactifs !")
    st.markdown("- La petit maison pour revenir à l'état initial", unsafe_allow_html=True)
    st.markdown("- Les flèches pour se déplacer", unsafe_allow_html=True)
    st.markdown("- La loupe pour zoomer sur une partie du graphique (attention à sélectionner la zone de zoom)",
                unsafe_allow_html=True)

st.subheader("Introduction")
st.write("""Sur le site du gouvernement datagouv.fr, on peut retrouver différents jeux de donnés sur des thèmes
         différents. Culture, éducation, énergie, tout y passe. Ces données sont le fruit d'études menées par l'État ou
         des entreprises associées à l'état.""")
st.write("""On y retrouve des données de différentes tailles sur différents sujets et dans différents formats.
        Comme le titre l'indique, nous avons choisit comme thème l'électricité, plus précisément la consommation
        d'électricité de différents appareils en France, sur la période avril 2019 - avril 2020.""")
st.write("""En tout, on utilise 3 jeux de données différents pour 5 graphiques. On a un jeu de données avec toutes les
        consommation, tout appareil confondus. Un autre avec les consommations de tout les téléviseur et un autre 
        avec celles de 3 appareils avec des consommations basses, moyennes et élevés.""")
st.divider()

st.subheader("Comparaison de consommation de 3 appareils")
columns4, columns5 = st.columns(2)
with columns4:
    st.write("""Sur ce graphique, on retrouve:""")
    st.write("""🔵 - En bleu la consommation totale des appareils de la catégorie Audio_TV. C'est à dire les 
                enceintes, bar de son, etc...""")
    st.write("""🟠 - En orange la consommation totale de l'éclairage. Donc tout ce qui relève des lumières, leds,
                etc...""")
    st.write("""🟢 - Pour finir, en vert, on a la consommation totale des chauffages électriques.""")
    st.write("""On voit sur ce graphique l'écart de consommation entre le chauffage électrique et le reste des
            apppareils. Le chauffage électrique a un certains monopole sur la consommation électrique.""")
with columns5:
    components.html(figureComparaisonHtml, height=500)

st.divider()
st.subheader("Comparaison des consommations de différents téléviseurs")
components.html(figureTeleviseursHtml, height=500)
st.write("""Cette fois-ci, on retrouve deux graphique pour un seul jeux de données, celui sur la consommation de tout
        les téléviseurs.""")
st.write("""On reconnais le graphique à nuages de points où chaque point est une seul donnée. Mais on voit sur la 
        droite de celui-ci, un autre graphique que à l'air moins familier. C'est ce qu'on appelle une boîte à 
        moustache ou Tukey box et permet de visualiser simplement les valeurs centrales d'un jeu de données.""")
st.write("""Pour expliquer ça simplement, la boîte à moustache est composée d'un rectangle centrale représentant 
    quartile interquartile (Q3-Q1), c'est-à-dire où se situent les 50% des données. La ligne à l'intérieur de la boîte 
    marque la médiane (valeur centrale).""")
st.write("""Les lignes qui sont à la fois au dessus et en dessous du rectangle sont appelées moustaches, c'est la plus
        petite et la plus grande valeur du jeu de données""")
st.write("""On retrouve aussi des points qui représentent une seule valeur chacun, ce sont les points aberrants ou
        outliers en anglais qui sont juste des valeurs extrêmes par rapport au reste des données.""")
st.write("""Maintenant qu'on comprends mieux ce que signifie le deuxième graphique, on peut voir que 50% des téléviseurs
        consomment entre 50 et 210kWh, et que quelqu'un à réussit à consommet plus de 1.100kWh rien qu'avec sa
        télévision...""")

st.divider()
st.subheader("Consommation totale, tout appareils confondus")
components.html(figureConsommationHtml, height=750)
st.write("""Pour la consommation de tout les appareils confondu, on retrouve notre bonne et fidèle boîte à moustache
         qui va être d'une pertinence clef dans la visualisation d'un si grand champs de données.""")
st.write("""La première contient les outliers, ce qui explique sa forme singulière tandis que la deuxième en est 
        débarassée.""")
st.write("""La boîte à moustache est un très bon outil pour visualiser les valeurs centrales dans un jeu de données
        mais elle possède aussi ses limites, dans notre jeu de données on retrouve beaucoup de petites valeurs et
        beaucoup de grandes valeurs ce qui explique la taille du rectangle dans le premier exemple et la multitude
        de points aberrants qui forment presque une ligne continue.""")

st.divider()
st.subheader("Conclusion")
st.write("""Suite à la visualisation de ces différents graphiques, on a pu voir l'importance de la consommation de
        certains appareils par rapport à d'autres ainsi que les différentes consommation d'un appareil et d'une
        gamme d'appareils.""")