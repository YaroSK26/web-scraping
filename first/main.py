# file I / O = input / output

my_file = open("first/test.txt", mode="r+")
 #  r = read 
 #  w = write 
 #  r+ = read + write 
 # a = append - prida na koniec


print(my_file.read())
my_file.seek(2) # vrati kurzor na urcitu poziciu , vdaka tomu vieme vypisat viackrat
print(my_file.read())

#print(my_file.readline()) print(my_file.readline())  - vypise iba prve dve riadok 
#print(my_file.readlines()) - vypise to list  odelene \n


my_file.write("\ncauuu")

my_file.close()


with open(f"first/names.txt" , mode= "a") as names_list:
    names_list.write("\nNeville")

#uloha , nefunguje lebo vo vs code nejde interagovat s outputom

pokracovanie = True
while pokracovanie:
    subor = input(str("nazov suboru?"))
    with open(f"first/{subor}.txt",mode="w") as names_list2:
        names_list2.write("ahoj")
    
    odpoved = input("chces dalsi subor? ano/ne")
    if odpoved == "ne":
        pokracovanie = False
