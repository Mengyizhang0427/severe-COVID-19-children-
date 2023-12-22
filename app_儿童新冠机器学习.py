# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 11:06:55 2023

@author: Starchild
"""
import streamlit as st
import pandas as pd
import pickle

# Title
st.header("RandomForest+TomekLinks for predicting severe COVID-19 in hospitalized children with Omicron variant infection")
#input
CK=st.number_input("Creatine kinase(U/L,Norm:24-229)")
BUN=st.number_input("Blood urea nitrogen(mmol/L,Norm:2.7-7.0)")
TB=st.number_input("Total bilirubin(μmol/L,Norm:3.4-20.5)")
GGT=st.number_input("Gamma-glutamyl transpeptidase(U/L,Norm:5-19)")
CRP=st.number_input("C-reactive protein(mg/dl,Norm:<5)")
LDH=st.number_input("Lactate dehydrogenase(U/L,Nrom:120-345)")
NAL=st.number_input("Neutrophil-to-lymphocyte ratio")
PLT=st.number_input("Platelet(10^9/L,Norm:167-453)")
AST=st.number_input("Aspartate aminotransferase(U/L,Norm:14-44)")
Age=st.number_input("Age(Norm:0-18)")

with open('RandomForest_10.pkl', 'rb') as f:
    clf = pickle.load(f)
with open('data_max.pkl', 'rb') as f:
    data_max = pickle.load(f)
with open('data_min.pkl', 'rb') as f:
    data_min = pickle.load(f)


# If button is pressed
if st.button("Submit"):
    
    # Unpickle classifier
    # Store inputs into dataframe
    columns = ['CK','BUN','TB','GGT','CRP','LDH','NAL','PLT','AST']
    X = pd.DataFrame([[CK,BUN,TB,GGT,CRP,LDH,NAL,PLT,AST]], 
                     columns =columns )
    X = (X-data_min)/(data_max-data_min)
    if Age <1:
        Age=1
    elif Age > 3:
        Age=3
    else:
        Age=2
    X["Age"]=Age
    st.write('Normalized data:')
    st.dataframe(X)
    # Get prediction
    prediction = clf.predict(X)
    pred=clf.predict_proba(X)[0][1]
    
    # Output prediction
    st.text(f" The probability of severe COVID-19 in hospitalized children with Omicron variant infection is {pred}.")

   
    
    
    
    
    
    
    
