from bs4 import BeautifulSoup
import requests
#pip install requests

response = requests.get("http://www.ekospace.cz/")

web = response.text

soup = BeautifulSoup(web,"html.parser")
text_book = soup.find("a", class_="ucebniceMikro")
pdf = text_book.get("href")

url = "http://www.ekospace.cz/"
pdf_url =  url + pdf
print(pdf_url)

response2 = requests.get(pdf_url)
with open("web-scrap/ucebnice.pdf","wb") as file:
    file.write(response2.content)

