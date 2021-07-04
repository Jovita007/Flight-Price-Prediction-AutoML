import streamlit as st
import pickle
import pandas as pd
import numpy as np
from PIL import Image
import sklearn
import datetime
import time 
import tpot


#define
def main():   

    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Flight Price Prediction</h1> 
    </div>   
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 


    st.sidebar.subheader("Select Departure")
    m = pd.to_datetime("today").month
    d = pd.to_datetime("today").day
    y = pd.to_datetime("today").year
    
    dep = st.sidebar.date_input("Day" , datetime.date(y,m,d))
    if dep is not None:
        mon_d = dep.month
        day_d = dep.day

        hour_1 = st.sidebar.selectbox("Hour", list(range(1,25)))
        minute_1 = st.sidebar.selectbox("Minute", list(range(0,61)))

    st.subheader("Departure Time :")
    x = "2020" + "/"  +str(mon_d) + "/" + str(day_d) + " " + str(hour_1) + ":" + str(minute_1)
    if x is not None:
        
        op = pd.to_datetime([x])
        if op is not None:
            st.write(op.item())
    

    st.sidebar.subheader("Select Arrival")
    arr = st.sidebar.date_input("Day." , datetime.date(y,m,d+1))
    if arr is not None:
    
        mon_a = arr.month
        day_a = arr.day
        
        

        hour_2 = st.sidebar.selectbox("Hour.", list(range(1,25)) ,2)
        minute_2 = st.sidebar.selectbox("Minute.", list(range(0,61)))

    st.subheader("Arrival Time :")
    x1 = "2020" + "/"  +str(mon_a) + "/" + str(day_a) + " " + str(hour_2) + ":" + str(minute_2)
    if x1 is not None:
        
        op1 = pd.to_datetime([x1] )
        if op1 is not None:
            st.write(op1.item())
    
    

    # Airline
    # AIR ASIA = 0 (not in column)
    st.subheader("Select Airline")
    airline = st.selectbox('',( "Air_India","GoAir","IndiGo","Jet_Airways","Jet_Airways_Business","Multiple_carriers","Multiple_carriers_Premium_economy","SpiceJet","Trujet","Vistara","Vistara_Premium_economy"))
    if(airline=='Jet Airways'):
        Jet_Airways = 1
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0 

    elif (airline=='IndiGo'):
        Jet_Airways = 0
        IndiGo = 1
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0 

    elif (airline=='Air India'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 1
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0 
            
    elif (airline=='Multiple carriers'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 1
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0 
            
    elif (airline=='SpiceJet'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 1
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0 
            
    elif (airline=='Vistara'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 1
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline=='GoAir'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 1
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0
    elif (airline=='Multiple carriers Premium economy'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 1
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline=='Jet Airways Business'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 1
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (airline=='Vistara Premium economy'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0            
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 1
        Trujet = 0
            
    elif (airline=='Trujet'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0      
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 1

    else:
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

        # print(Jet_Airways,
        #     IndiGo,
        #     Air_India,
        #     Multiple_carriers,
        #     SpiceJet,
        #     Vistara,
        #     GoAir,
        #     Multiple_carriers_Premium_economy,
        #     Jet_Airways_Business,
        #     Vistara_Premium_economy,
        #     Trujet)
    st.write("Airline -- " , airline)
        # Source
        # Banglore = 0 (not in column)
    st.subheader("Select Source")
    Source = st.selectbox('',("Chennai","Delhi","Kolkata","Mumbai")) 
    if (Source == 'Delhi'):
        s_Delhi = 1
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 0

    elif (Source == 'Kolkata'):
        s_Delhi = 0
        s_Kolkata = 1
        s_Mumbai = 0
        s_Chennai = 0

    elif (Source == 'Mumbai'):
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 1
        s_Chennai = 0

    elif (Source == 'Chennai'):
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 1


    else:
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 0

        # print(s_Delhi,
        #     s_Kolkata,
        #     s_Mumbai,
        #     s_Chennai)
    st.write("Source -- " , Source)



        # Destination
        # Banglore = 0 (not in column)
    st.subheader("Select Destination")
    Destination = st.selectbox('',("Cochin","New_Delhi","Hyderabad","Kolkata"))
    if (Destination == 'Cochin'):
        d_Cochin = 1
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0

    elif (Destination == 'Delhi'):
        d_Cochin = 0
        d_Delhi = 1
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0

    elif (Destination == 'New_Delhi'):
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 1
        d_Hyderabad = 0
        d_Kolkata = 0

    elif (Destination == 'Hyderabad'):
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 1
        d_Kolkata = 0
    elif (Destination == 'Kolkata'):
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 1

    else:
        d_Cochin = 0
        d_Delhi = 0
        d_New_Delhi = 0
        d_Hyderabad = 0
        d_Kolkata = 0

    st.write("Destination -- ",Destination)

        #stops
    st.subheader("Select Stops")
    stop = st.selectbox("   " , [0,1,2,3,4])
    st.write("Stops -- ", stop)

    if st.checkbox("Duration"):
        if op1 is not None:
            st.write((op1.item() - op.item()))

    
    op2 = str(op1-op)
    if op2 is not None:
        hr = int(op2.split(']')[0][-9:-7])
        mini = int(op2.split(']')[0][-6:-4])

    
    model = pickle.load(open('F_Model.pkl','rb'))

    prediction=[stop, 
        mon_d, 
        day_d, 
        hour_1, 
        minute_1, 
        hour_2,
        minute_2,
        hr, 
        mini,
        Air_India,
        GoAir,
        IndiGo,
        Jet_Airways,
        Jet_Airways_Business,
        Multiple_carriers,
        Multiple_carriers_Premium_economy,
        SpiceJet,
        Trujet,
        Vistara,
        Vistara_Premium_economy,
        s_Chennai,
        s_Delhi,
        s_Kolkata,
        s_Mumbai,
        d_Cochin,
        d_Delhi,
        d_Hyderabad,
        d_Kolkata,
        d_New_Delhi
    ]
        
    if st.button("PREDICT"):
        pred = model.predict([prediction])
        for i in pred:
            st.write("Your Fare Price is : " , round(i ,3)  , "INR")
            st.write("*Happy and Safe Journey ...*")

    st.write("""    """)
    st.write("""    """)
    
      
    
if __name__=='__main__': 
    main()
