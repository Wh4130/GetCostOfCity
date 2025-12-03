import streamlit as st
from scripts import GetLivingExpenses
from constants import CURRENCY_MAP,CITIES
import requests

city = st.selectbox("city", CITIES)
if st.button("submit"):
    # response = requests.post("http://127.0.0.1:8000/source_html", json={"city": city})

    # TABs = st.tabs(["body","metrices"])

    # with TABs[0]:
    #     st.write(response.json()["result"])

    # with TABs[1]:
    #     st.write(GetLivingExpenses.get_individual_expenses(response.json()["result"]))
    #     st.write(GetLivingExpenses.get_rent(response.json()["result"]))

    response = requests.post("http://127.0.0.1:8000/expenses", json={"city": city})
    st.write(response.json())