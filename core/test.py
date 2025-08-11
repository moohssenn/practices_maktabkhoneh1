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

"""

