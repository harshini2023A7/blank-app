import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="🔄")
st.title("🔄 Universal Unit Converter")

category = st.selectbox("Choose a conversion type:", 
                        ["Length", "Weight", "Temperature"])

if category == "Length":
    units = {"Meters": 1, "Kilometers": 1000, "Centimeters": 0.01, "Miles": 1609.34, "Feet": 0.3048}
elif category == "Weight":
    units = {"Kilograms": 1, "Grams": 0.001, "Pounds": 0.453592, "Ounces": 0.0283495}
elif category == "Temperature":
    units = {"Celsius": "C", "Fahrenheit": "F", "Kelvin": "K"}

# Input section
from_unit = st.selectbox("From:", list(units.keys()))
to_unit = st.selectbox("To:", list(units.keys()))
value = st.number_input("Enter the value to convert:", format="%.4f")

# Conversion logic
def convert_length(val, from_u, to_u):
    return val * units[from_u] / units[to_u]

def convert_weight(val, from_u, to_u):
    return val * units[from_u] / units[to_u]

def convert_temperature(val, from_u, to_u):
    if from_u == to_u:
        return val
    if from_u == "Celsius":
        if to_u == "Fahrenheit":
            return val * 9/5 + 32
        elif to_u == "Kelvin":
            return val + 273.15
    elif from_u == "Fahrenheit":
        if to_u == "Celsius":
            return (val - 32) * 5/9
        elif to_u == "Kelvin":
            return (val - 32) * 5/9 + 273.15
    elif from_u == "Kelvin":
        if to_u == "Celsius":
            return val - 273.15
        elif to_u == "Fahrenheit":
            return (val - 273.15) * 9/5 + 32

# Display result
if st.button("Convert"):
    if category == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif category == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    elif category == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)

    st.success(f"{value} {from_unit} = {round(result, 4)} {to_unit}")
