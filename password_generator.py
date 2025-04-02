import streamlit as st
import random
import string
import re

def password_generator(length, digits, special):
    characters = string.ascii_letters
    
    if digits:
        characters += string.digits
    
    if special:
        characters += string.punctuation
    
    return ''.join(random.choice(characters) for _ in range(length))

def check_password_strength(password):
    length_criteria = len(password) >= 8
    digit_criteria = any(char.isdigit() for char in password)
    special_criteria = any(char in string.punctuation for char in password)
    uppercase_criteria = any(char.isupper() for char in password)
    
    strength = sum([length_criteria, digit_criteria, special_criteria, uppercase_criteria])
    
    if strength == 4:
        return "Strong ✅"
    elif strength == 3:
        return "Moderate ⚠️"
    elif strength == 2:
        return "Weak ❌"
    else:
        return "Very Weak ❌❌"

st.title("🔐 Password Generator & Strength Checker")

option = st.radio("Choose an option:", ("Generate Password", "Check Password Strength"))

if option == "Generate Password":
    length = st.slider("Password Length", min_value=4, max_value=24, value=8)
    digits = st.checkbox("Include Digits")
    special = st.checkbox("Include Special Characters")
    
    if st.button("Generate Password"):
        password = password_generator(length, digits, special)
        st.success(f"Generated Password: {password}")
        # st.code(password, language="")
        st.button("Copy Password", on_click=lambda: st.session_state.update({'clipboard': password}))

elif option == "Check Password Strength":
    user_password = st.text_input("Enter Your Password", type="password")
    if st.button("Check Strength"):
        if user_password:
            strength = check_password_strength(user_password)
            st.info(f"Password Strength: {strength}")
        else:
            st.warning("Please enter a password to check its strength.")

st.write("Made By **Muhammad Salman** ❤")
