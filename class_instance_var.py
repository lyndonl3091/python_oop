class Developer:
    website = "http://lyndonlarosa.com"

    def __init__(self, name):
        self.name = name

lyndon = Developer('Lyndon')

print(lyndon.name)
print(Developer.website)
