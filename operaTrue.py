from Scene import Scene

scenes = []

def main():
    loadOperaData()
    for scene in scenes:
        print(scene)

def loadOperaData():
    file = open("adatokopera.csv", encoding="UTF8")
    file.readline()
    lines = file.readlines()
    for sor in lines:
        line=sor.split(";")
        if line[6] == "":
            line[6]==0
        scene = Scene(int(line[0]), line[1], line[2], line[3], line[4], int(line[5]), int(line[6]))
        scenes.append(scene)
    file.close()






main()