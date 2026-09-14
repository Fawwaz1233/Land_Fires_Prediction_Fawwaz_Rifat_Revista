import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="Prediksi Wilayah dengan Risiko Karhutla/Wildfire",
    layout="wide",
    initial_sidebar_state="expanded"
)

def run():
    #Membuat Title
    st.title("Wilfire Area Prediction")

    # Membuat Sub Header
    st.subheader("Memprediksi risiko karhutla dengan menggunakan gambar satelit")

    #Menambah Gambar
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOSDuWtqI_FGvOXKloCHMHg75goroqp1RlqQ&s")

    # menambah deskrisi
    st.write("Page ini dibuat oleh Fawwaz")

    # Menambah garis
    st.markdown("====")

    # Magic Syntax
    """
    Pada page ini penulis akan melakukan explorasi sederhana,
    terkait Dataset yang digunakan dalam pembuatan model 
    machine learning
    """
if __name__=="__main__":
    run()