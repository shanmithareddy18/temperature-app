import streamlit as st

st.set_page_config(page_title="Temperature Converter")

st.title("🌡️ Temperature Converter")

st.write("Convert temperature between Celsius and Fahrenheit")

# User input
temp = st.number_input("Enter Temperature")

option = st.radio(
    "Choose Conversion",
    ("Celsius to Fahrenheit", "Fahrenheit to Celsius")
)

if st.button("Convert"):

    if option == "Celsius to Fahrenheit":
        result = (temp * 9/5) + 32
        st.success(f"{temp}°C = {result:.2f}°F")

    else:
        result = (temp - 32) * 5/9
        st.success(f"{temp}°F = {result:.2f}°C")