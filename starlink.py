import streamlit as st
import streamlit as st
import numpy as np
import pandas as pd
import plost

st.set_page_config(layout='wide', initial_sidebar_state='expanded')


st.sidebar.header('Starlink Dashboard')

st.sidebar.subheader('Connection parameter')
time_hist_color = st.sidebar.selectbox('Color by', ('ping_min', 'ping_max')) 

st.sidebar.subheader('Line chart parameters')
plot_data = st.sidebar.multiselect('Select data', ['ping_min', 'ping_max'], ['ping_min', 'ping_max'])

st.write("Starlink Report in Area")


chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Wendeys', 'Planet Fitness', 'Target'])


st.line_chart(chart_data)


chart_data1 = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Starbucks', 'SpaceX', 'Airprot'])


st.line_chart(chart_data1)

# 
st.markdown('### Metrics')
col1, col2, col3 = st.columns(3)
col1.metric("BandWith", "80mb/s", "1.2 %")
col2.metric("Latency", "40.6 ms", "-8%")
col3.metric("Obstruction", "0.00214%", "4%")



