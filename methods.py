class Pokemon:
    def __init__ (self, name):
        self.name = name
        self.health = 100
        self.damage = 10

    def attack(self, other_pokemon):
        other_pokemon.health = other_pokemon.health - self.damage

pikachu = Pokemon('Pikachu')
raichu = Pokemon('Raichu')

print(pikachu.name)
print(raichu.name)

raichu.attack(pikachu)

print(pikachu.health)
