"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

class Hero:
    def __init__(self, health, power):
        self.health = health
        self.power = power

class Goblin:
    def __init__(self, health, power):
        self.health = health
        self.power = power

hiroshi = Hero(10, 5)
django = Goblin(6, 2)       
        

def main():
    while django.health > 0 and hiroshi.health > 0:
        print("You have %d health and %d power." % (hiroshi.health, hiroshi.power))
        print("The goblin has %d health and %d power." % (django.health, django.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            django.health -= hiroshi.power
            print("You do %d damage to the goblin." % hiroshi.power)
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
            hiroshi.health -= django.power
            print("The goblin does %d damage to you." % django.power)
            if hiroshi.health <= 0:
                print("You are dead.")

main()
