class Superhero:
     def __init__(self, name):
            self.name = name

superman = Superhero('Superman')


class Books:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

atom = Books('Atom', 'Atom Author', 2017)

print (atom.title)
print (atom.author)
print (atom.year)
