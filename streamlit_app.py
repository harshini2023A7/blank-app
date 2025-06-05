import streamlit as st
from forex_python.converter import CurrencyRates, RatesNotAvailableError

# Initialize the CurrencyRates object
c = CurrencyRates()

# Set the title of the app
st.title("💱 Currency Converter")

# Input fields
amount = st.number_input("Enter amount:", min_value=0.0, value=1.0, step=0.1)
from_currency = st.selectbox("From Currency:", options=sorted(c.get_rates('').keys()))
to_currency = st.selectbox("To Currency:", options=sorted(c.get_rates('').keys()))

# Convert button
if st.button("Convert"):
    try:
        result = c.convert(from_currency, to_currency, amount)
        st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")
    except RatesNotAvailableError:
        st.error("Exchange rate not available for the selected currencies.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
