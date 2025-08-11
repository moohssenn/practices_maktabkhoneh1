"""
import requests
import json

url="http://127.0.0.1:8000/names"

response = requests.get(url)

print(response.text)

if response.status_code == 200:
    
    print(response.text)
else:
    print(f"Error: {response.status_code}")




cost_list = dict(
    id = 1, description = "food",  cost=120.56,
    id = 2, description = "breakfast",  cost=22.43,
    id = 3, description = "lunch",  cost=99.55,
    id = 4, description = "book",  cost=36.22,

)

"""

list_costs = [
    {"id":1,"description":"Housing","price":14.56},
    {"id":2,"description":"Food","price":19.55},
    {"id":3,"description":"Health","price":16.33},
    {"id":4,"description":"Kids","price":17.44},
    {"id":5,"description":"Pets","price":22.52},
    {"id":6,"description":"Personal Development","price":12.66},
    {"id":7,"description":"reza","Technology":11.33},
    {"id":8,"description":"reza","Giving":9.00},
]


for x in names_list:
    print(x['price']),