
from random import random
import random

names = []

def main():
    readNames()
    print(names)
    #findNameById()
    #printRandomName()
    findPersonByName()


def findPersonByName():
    name = input("Kérek egy nevet: ")
    if szerepel_e(name):
        print("A megadott név szerepel")
    else: 
        print("Nem szerepel a megadott név")


def szerepel_e(name):
    for namee in names:
        if name == namee:
            return True
    return False

def printRandomName():
    print(len(names))
    rnd = random.randint(0, len(names)-1)
    while True:
        rnd2 = random.randint(0, len(names)-1)
        if rnd2 != rnd:
            break
    print(names[rnd])
    print(names[rnd2])
    




def findNameById():
    id = len(names)+1
    while True: 
        id = int(input("Kérem adjon meg egy sorszámot: "))
        if id<=len(names):
            break
    parts = names[id-1].split(' ')
    
    print(f"A keresett személy neve: {names[id-1]}. A {parts[1]}.{parts[0]}@gmail.com az emailcíme.")
    

def readNames():
    file = open("nevsor.csv", encoding="UTF8")
    lines = file.readlines()
    for line in lines:
        names.append(line.strip())
        

    #return file.readlines()

main()