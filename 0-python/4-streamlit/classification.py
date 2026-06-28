import pandas as pd
import numpy as np
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache_data
def load_data():
    iris=load_iris()
    df=pd.DataFrame(iris.data,columns=iris.feature_names)
    df['species']=iris.target
    return df,iris.target_names
df,target_names=load_data()
model=RandomForestClassifier()
model.fit(df.iloc[:,:-1],df['species'])

speal_len=st.sidebar.slider('Speal Length',float(df['sepal length (cm)'].min()),float(df['sepal length (cm)'].max()))
speal_wid=st.sidebar.slider('Speal Width',float(df['sepal width (cm)'].min()),float(df['sepal width (cm)'].max()))
petal_len=st.sidebar.slider('Petal Length',float(df['petal length (cm)'].min()),float(df['petal length (cm)'].max()))
petal_wid=st.sidebar.slider('Petal Width',float(df['petal width (cm)'].min()),float(df['petal width (cm)'].max()))

input_data=[[speal_len,speal_wid,petal_len,petal_wid]]

pred=model.predict(input_data)
pred_species=target_names[pred[0]]

st.write("Predicted Species:")
st.write(pred_species)