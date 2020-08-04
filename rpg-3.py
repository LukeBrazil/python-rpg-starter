"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

class Warrior:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    def status(self):
        return "%s has %d power and %d health. /" % (self.name, self.power, self.health)
        

class Hero(Warrior):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

class Goblin(Warrior):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)


hiro = Hero('Hiro', 10, 5)
django = Goblin('Django', 6, 2)

def main():

    while django.health > 0 and hiro.health > 0:
        print()
        print()
        print(hiro.status(), django.status())
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            django.health -= hiro.power
            print("You do %d damage to the goblin." % hiro.power)
            if django.health <= 0:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if django.health > 0:
            # Goblin attacks hero
            hiro.health -= django.power
            print("The goblin does %d damage to you." % django.power)
            if hiro.health <= 0:
                print("You are dead.")

main()
