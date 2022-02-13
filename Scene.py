
class Scene:

    def __init__(self, id, name, original, theater, year, chapter, picture):
        self.id = id
        self.name = name
        self.original = original
        self.theater = theater
        self.year = year
        self.chapter = chapter
        self.picture = picture 

    def __str__(self):
        return "azonosító: " + self.id + "\ncíme: " + self.name + "\nSzínház: " + self.theater + "\n Bemutatás Éve:" + self.year + "\nKép: " + self.picture
        
    
