from sys import exit
from random import randint

class Scene(object):
    def enter(self):
        print("This scene is not yet configured. Sublcass it and implement enter().")
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print("\n--------")
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):
    quips = [
        "You died. You kenda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
        ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print("The Gothons of Plaet Percal have invaded your ship and...")

        action = input("> ")

        if action == "shoot!":
            print("you are dead. Then he eats you")
            return 'death'

        elif action == "dodge!":
            print("he eats you again")
            return 'death'

        elif action == "tell a joke":
            print("you escape")
            return 'laser_weapon_armory'

        else:
            print("Does not compute")
            return 'central_corridor'

class LaserWeaponArmory(Scene):
    def enter(Self):
        print("Get the bomb. The code is 3 digits.")
        code = "%d%d%d" % (randint(1, 9), randint(1, 9), randint(1, 9))
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZZZEDDD")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print("Correct")
            return 'the_bridge'

        else:
            print("You're out of chances")
            return 'death'

class TheBridge(Scene):
    def enter(self):
        print("theres a bomb. What will you do?")

        action == input("> ")

        if action == "throw the bomb":
            print("it blew up in your hands")
            return 'death'

        elif action == "slowly put it down":
            print("ok, that worked.")
            return 'escape_pod'

        else:
            print("what did you say?")
            return "the_bridge"

class EscapePod(Scene):
    def enter(self):
        print("You made it to the pods.")
        print("there are 5 pods here. Which will you take?")

        good_pod = randint(1, 5)
        guess = input("> ")

        if int(guess) != good_pod:
            print("Wrong one, Fool! You dead now.")
            return 'death'

        else:
            print("Nice! To freedom we go now.")
            return 'finished'

class Map(object):
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
