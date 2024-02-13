import streamlit as st
import pickle                                #it is required to import df.pkl and pipe.pkl
                                             #you need to install sklearn for pickle to work
import numpy as np


#import the model
pipe =pickle.load(open('pipe.pkl','rb'))     #rb = read binary
df = pickle.load(open('df.pkl','rb'))
 
st.title("laptop price predictor")

#brand
company = st.selectbox('Brand',df['Company'].unique())
#type of laptop
type = st.selectbox('Type',df['TypeName'].unique())
#RAM
ram = st.selectbox('RAM (in GB)',[2,4,6,8,12,16,24,32,64])
#weight of laptop
weight = st.number_input("Weight of the laptop")
#touchscreen
touchscreen = st.selectbox('Touchscreen',['No','Yes'])
#ips display
ips = st.selectbox('IPS',['No','Yes'])
#screen size
screen_size = st.number_input('Screen Size')
#resolution
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])
#cpu
cpu = st.selectbox('CPU Brand',df['cpu_brand'].unique())
#hdd
hdd = st.selectbox('HDD (in GB)',[0,128,256,512,1024,2048])
#ssd
ssd = st.selectbox('SSD (in GB)',[0,8,128,256,512,1024])
#gpu
gpu = st.selectbox('GPU Brand',df['gpu_brand'].unique())
#os
os = st.selectbox('Operating System',df['os'].unique())


#step 1: now i have to pick all these values for input purpose and we will make a row for input and 
#step 2: then we send these values to pipe and in last
#step 3: we will display the prediction of pipe

if st.button('Predict Price'):

    #i don't need touchscreen value in the form of yes/no. i need them as 0/1
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    #i don't need ips value in the form of yes/no. i need them as 0/1
    if ips == 'Yes':
        ips = 1
    else:
        ips = 0
    
    
    #ppi calculation
    x_res = int(resolution.split('x')[0])
    y_res = int(resolution.split('x')[1])
    ppi = (((x_res**2) + (y_res**2))**0.5) / screen_size


    #query (construction of input query point)
    query = np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])

    query = query.reshape(1,12)
    #st.title(np.exp(pipe.predict(query)))     #bcoz we transformed price into log while building model
    st.title("the predicted price is : " + str(np.exp(pipe.predict(query)))) 

