import requests
from pydantic import BaseModel
from constants import CURRENCY_MAP
import re

class Obj(BaseModel):
    city: str

class GetLivingExpenses:

    @staticmethod
    def scrape(doc: Obj):
        html =  requests.get(f"https://www.numbeo.com/cost-of-living/in/{doc.city}").text
        return html
    
    @staticmethod
    def get_individual_expenses(html: str):
        pattern = rf'The estimated monthly costs for a single person are <span.+<span class="in_other_currency">\(([\d\.,]+)([^\);]*)\;?\)</span></span>'
        match = re.search(pattern, html)
        num = match.group(1)
        currency = match.group(2)
        return {
            "living_expenses":{
                "number": num,
                "currency": CURRENCY_MAP[currency]
            }   
        }
    
    @staticmethod
    def get_rent(html: str):
        pattern = rf'1 Bedroom Apartment Outside of City Centre </td> <td .+?> <span class="first_currency">([\d\.\,]+)&nbsp;([^<;]+)\;?</span>'
        match = re.search(pattern, html)
        num = match.group(1)
        currency = match.group(2)
        return {
            "rent":{
                "number": num,
                "currency": CURRENCY_MAP[currency]
            }   
        }
    
    @staticmethod
    def RUN(doc: Obj):

        html = GetLivingExpenses.scrape(doc)
        
        indiv_exp_data = GetLivingExpenses.get_individual_expenses(html)
        rent_data = GetLivingExpenses.get_rent(html)

        return {
            "city": doc.city,
            "data": {
                "living_expenses": indiv_exp_data["living_expenses"],
                "rent": rent_data["rent"]
            }}
    
    


