class Pokemon:
    def __init__ (self, name):
        self.name = name
        self.health = 100
        self.damage = 10

    def attack(self, other_pokemon):
        other_pokemon.health = other_pokemon.health - self.damage
        print("{} attacks {}!".format(self.name, other_pokemon.name))
        print("{} loses {} health points".format(other_pokemon.name, self.damage))

    def __str__(self):
        return "{}: {}".format(self.name, self.health)

pikachu = Pokemon('Pikachu')
raichu = Pokemon('Raichu')

print(pikachu)

print(pikachu.name)
print(raichu.name)

raichu.attack(pikachu)

print(pikachu)
