import streamlit as st 
import time
from PIL import Image

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    image = Image.open('bmi.png')
    st.image(image)

with col3:
    st.write(' ')

berat = st.number_input('Masukkan berat badan dalam (kg)', min_value = 50.0, max_value = 150.0, value = 50.0)
tinggi = st.number_input('Masukan tinggi badan dalam (cm)', min_value = 100.0, max_value = 250.0, value = 150.0)

bmi = berat/((tinggi/100)**2)

level_bmi = ['KEKURANGAN BERAT BADAN', 'BERAT BADAN IDEAL', 'KELEBIHAN BERAT BADAN', 'OBESITAS']

if bmi < 18.50:
    level = level_bmi[0]
elif bmi <= 24.99:
    level = level_bmi[1]
elif bmi <= 29.99:
    level = level_bmi[2]
else:
    level = level_bmi[3]

if st.button('Lihat hasil'):     

    if level == level_bmi[1]:
        st.balloons()
        st.header(f'{level}')
    else:
            st.header(f'{level}')