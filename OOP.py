# Assignment !: Design Your Own Class!

class SuperHero:
    def __init__(self, name, powers, city):
        self.name = name
        self.powers = powers
        self.city = city 
    
    def hero_info(self):
        print(f"Name: {self.name}")
        print(f"Powers: {self.powers}")
        print(f"City: {self.city}")

my_hero = SuperHero("Barry Allen", "Speed Force", "Central City")

my_hero.hero_info()

print("\n----\n")
        
        
class Heroine(SuperHero):
    def __init__(self, name, powers, city, weakness, rogue):
       
        super().__init__(name, powers, city)
        self.weakness = weakness
        self.rogue = rogue

    def heroine_info(self):
        self.hero_info()
        print(f"weakness : {self.weakness}")
        print(f"rogues : {self.rogue}")

my_heroine = Heroine("Power Girl", "Strength and invulnerability", "metropolis", "Kryptonite", "General Zod")

my_heroine.heroine_info()


# Activity 2: Polymorphism Challenge

class Plane:
    def move(self):
        print("Flying")

class Car:
    def move(self):
        print("Driving")

for vehicles in (Plane(), Car()):
    vehicles.move()



