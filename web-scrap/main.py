from bs4 import BeautifulSoup

with open("./index.html") as file:
    html_code = file.read()

soup = BeautifulSoup(html_code, "html.parser")

print(soup.title.string)



all_a = soup.find_all("a")
print(all_a)

with open("./a.txt", mode="w" ) as fileA:
    for one_a in all_a:
        a1 = one_a.get("href")

        fileA.write(a1)
        fileA.write("\n")

heading = soup.find(name="h1", id="name") 
print(heading)

heading2= soup.find_all("h2", class_="about")
print(heading2)

contact = soup.select("p a")
# a ktore je v p tagu .. je aj select_one