import streamlit as st
import pandas 

data= {
    'Series 1': [1,2,3,4,5],
    'Series 2': [10,30,40,100,200]
}

df = pandas.DataFrame(data)

st.title('Welcome to Cloud Gear')
st.subheader('Temperature Converter:')

myslider = st.slider('Celsius')
st.write(myslider,'degrees Celsius in Farenheit is',myslider*9/5 +32,'degrees')

st.subheader('Tables and Charts:')
st.write('''
         Welcome to Cloud Gear...
         Enjoy it!
         ''')
st.write(df)
st.line_chart(df)
st.area_chart(df)

# streamlit run app.py
