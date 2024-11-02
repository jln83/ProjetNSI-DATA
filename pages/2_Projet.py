import streamlit as st
from streamlit_extras.app_logo import add_logo
from streamlit_extras.mention import mention

st.set_page_config(page_title="Projet DATA", page_icon="📟", layout="wide", initial_sidebar_state="expanded")
add_logo(r"images/cat-64.png", height=50)

jeremy_mention = mention(label="Jeremy",
                         url="https://github.com/JeremyMrz", write=False)
julian_mention = mention(label="Julian",
                         url="https://github.com/jln83", write=False)
tristan_mention = mention(label="Tristan",
                          url="https://github.com/Patatosaurus666", write=False)
columns1, columns2 = st.columns(2)
with columns1:
    st.subheader("Organisation du projet et formalités")
    st.divider()

st.write("""Pour l'organisation et distribution des tâches, chacun avait "une partie" à faire. Le projet se découpe en
        3 partie, une première avec l'extraction des données (Pandas), une autre pour la réalisation des graphiques
        (Matplotlib) et une autre pour mettre en forme les graphique de Matplotlib (Streamlit)""")
st.write("""Chacun s'est donc vu attribué une partie en fonction de ses envie et affinités avec les différents 
        modules""")


with st.sidebar:
    st.write("N'hésitez pas à venir nous voir sur github")
    st.write(jeremy_mention, unsafe_allow_html=True)
    st.write(julian_mention, unsafe_allow_html=True)
    st.write(tristan_mention, unsafe_allow_html=True)
