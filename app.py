#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import datetime
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Liste des passagés sur le Titanic') #### Titre de l'application

#DATE_COLUMN = 'time'


### 1) Récupérer les data Titanic

#### En local
DATA_URL = 'train.csv'

#### Sur serveur

#DATA_URL = 'https://github.com/xanadu31/Dataset/blob/main/train.csv'

nrows=1000
data = pd.read_csv(DATA_URL, nrows=nrows) ####Chargement des données

data_load_state = st.text('Loading data...') #### Affichage de texte: Chargement des données

data_load_state.text("Done! (using st.cache)") #### Affichage de texte: Fin de chargement des données

if st.checkbox('Show raw data'): #### Affichage de la checkbox: Condition si click sur la checkbox 
    st.subheader('Raw data') #### Affichage de texte: "raw data" 
    st.write(data) #### Affichage de l'objet: Dataset ici 


### 2) Distribution des âges des individus

#### Avec streamlit: Afficher la distribution des passagés


st.subheader('1) Distribution des âges des individus')

#import matplotlib.pyplot as plt

#data.Age.plot(kind ="hist")
#st.plot()

#### Valeur de l'histogramme


#### Ajouter un slider

hist_value = np.histogram(data.Age, bins =10, range=(0,100))[0]
st.bar_chart(hist_value )


### 3) Taux de survie des individus en fonction du genre et de la classe


#data.groupby(["Sex","Pclass"])["Survived"].mean().unstack().plot(kind = "barh")

st.subheader('2) Taux de survie des individus en fonction du genre et de la classe')

survie = data.groupby(["Sex","Pclass"])["Survived"].mean().unstack().plot(kind = "barh")
st.set_option('deprecation.showPyplotGlobalUse', False)
st.write(survie)
st.pyplot()
#st.bar_chart(survie)


### 4) Tableau: Compter le nombre de personne ayant survécu en fonction du port d'embarcation

st.subheader("4) Le taux de survie en fonction du port d'embarcation")

survie = pd.DataFrame(data[data["Survived"] ==1].Embarked.value_counts())/pd.DataFrame(data.Embarked.value_counts()) *100

#survie

st.write(survie)


### 5) Boxplot du prix des tickets

st.subheader("5) Boxplot du prix des tickets")

import seaborn as sns #### Importation du package
sns.set_theme(style="whitegrid") ### choix du background
ax = sns.boxplot(x=data["Fare"])

st.set_option('deprecation.showPyplotGlobalUse', False)

st.write(ax)
st.pyplot()




#fig, ax = plt.subplots()
#st.write(sns.boxplot( x=data["Fare"]))
#st.pyplot(fig)


