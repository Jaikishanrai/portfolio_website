import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("006 images/photo.png")

with col2:
    st.title("Jai Kishan Rai")
    content = """
     Hello, my name is Jai Kishan Rai, and I am a final-year student at 
     Lakshmi  Narain College Of Technology, Bhopal.
      I am currently pursuing B.Tech in stream of Mechanical Engineering.
       I’ve always had a natural curiosity for machinery. 
      As a child, I loved taking things apart and putting them back together.
       My passion for machinery continued to develop.          
    """
    st.info(content)
