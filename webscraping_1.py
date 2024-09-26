import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

print(page.text)

soup = BeautifulSoup(page.text, "html.parser")


soup.find_all('div')
