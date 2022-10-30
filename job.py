import requests 
from bs4 import BeautifulSoup
import pandas as pd



url='https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1'


req = requests.get(url)
content = BeautifulSoup(req.content,'html.parser')
print(content)