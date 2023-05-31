from bs4 import BeautifulSoup

with open("./precvicovanie.html") as file:
    html_code = file.read()

soup = BeautifulSoup(html_code, "html.parser")

heading = soup.find("h1")
print(heading)

heading2 = soup.find("h2")
print(heading2)

history_List = soup.find("ul")
print(history_List)

all_p = soup.findAll("p")
print(all_p)
print(all_p[0])
print(all_p[1])

for one_p in all_p:
    print(one_p)
    print(one_p.getText())

all_a = soup.find_all("a")
print(all_a)

for one_a in all_a:
    print(one_a)
    print(one_a.getText())
    print(one_a.get("href"))


section = soup.find("section", class_="about-attavena") 
print(section)