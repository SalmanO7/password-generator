import streamlit as st
import random
import string

def password_generator(length, digits, spcial):
    charachters = string.ascii_letters
    
    if digits:
        charachters += string.digits
        
    if spcial:
        charachters += string.punctuation
        
    return ''.join(random.choice(charachters) for _ in range(length))

st.title("Password Generator")

length = st.slider("Password Length", min_value=4, max_value=24, value=8 )

digits = st.checkbox("Include Digits")

spcial = st.checkbox("Include Spcial Characters")

if st.button("Generate Password"):    
    password = password_generator(length, digits, spcial)
    st.write(f"Generated Your password:   {password}")
    
st.write("Made By Muhammad Salman ❤")

