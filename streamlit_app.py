import streamlit as st
import requests
import pandas as pd

# Set the page configuration
st.set_page_config(page_title="Market Price Tracker", layout="wide")

# Title of the app
st.title("🧺 Market Price Tracker")

# Sidebar for user inputs
st.sidebar.header("Filter Options")

# Input fields
commodity = st.sidebar.text_input("Enter Commodity Name", "Potato")
state = st.sidebar.text_input("Enter State Name", "Karnataka")
market = st.sidebar.text_input("Enter Market Name", "Bangalore")

# Button to fetch data
if st.sidebar.button("Fetch Prices"):
    with st.spinner("Fetching data..."):
        try:
            # Construct the API URL
            api_url = f"http://127.0.0.1:5000/request?commodity={commodity}&state={state}&market={market}"
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                if data:
                    # Convert JSON data to DataFrame
                    df = pd.DataFrame(data)
                    # Display the data
                    st.subheader(f"Price Data for {commodity.title()} in {market.title()}, {state.title()}")
                    st.dataframe(df)
                else:
                    st.warning("No data found for the given inputs.")
            else:
                st.error("Failed to fetch data from the API.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
