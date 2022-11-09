import streamlit as st
import pandas as pd
import pickle
#import streamlit.components.v1 as components

st.title('Fifa Player Market Value')
Age = st.number_input("Enter Age",0,100)
Best_overall = st.number_input("Enter Best Overall",0,100)
Overall_rating = st.number_input("Enter Overall Rating",0,100)
Potential = st.number_input("Enter Potential",0,100)

if st.button("Predict"):

    pickle_in = open('model_Random.pkl', 'rb') 
    r = pickle.load(pickle_in)
    
    X = pd.DataFrame([[Best_overall,Overall_rating,Potential,Age]], columns = ['Best_overall','Overall_rating','Potential','Age'])
    prediction = r.predict(X)
    
    st.success(f'The Market Value of Player is {prediction} Euro')
    
    
    
