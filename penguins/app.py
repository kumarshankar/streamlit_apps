import streamlit
import numpy as np
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Penguin Species Prediction App
This app predicts the **Penguin** species!
""")

st.sidebar.header('User Input Features')

st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/penguins_example.csv)
""")

def user_input_features():
    pass


