import streamlit as st
from scripts import GetLivingExpenses
from constants import CURRENCY_MAP,CITIES
import requests

city = st.selectbox("city", CITIES)
if st.button("submit"):
    response = requests.get(f"https://getcostofcity.onrender.com/source_html?city={city}")

    TABs = st.tabs(["body","metrices"])

    with TABs[0]:
        st.write(response.json()["result"])

    with TABs[1]:
        st.write(GetLivingExpenses.get_individual_expenses(response.json()["result"]))
        st.write(GetLivingExpenses.get_rent(response.json()["result"]))
    # url = f"https://getcostofcity.onrender.com/expenses?city={city}"
    # response = requests.get(url)
    # st.write(response.json())