import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("006 images/jai.jpg", width=300)

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

content2 = """
you can find some of the apps i have built in python. Feel free to contact me!
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("006 data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])


