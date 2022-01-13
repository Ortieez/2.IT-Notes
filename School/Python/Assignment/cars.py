import os
import random
from time import sleep


class Game:

    def __init__(self):
        self.cars = ("Toyota", "Honda", "Ford", "Mazda", "Nissan", "Chevrolet",
                     "Tesla", "Hyundai", "Kia", "Audi")

    def start(self):
        self.rand = random.choice(self.cars)
        self.count = 0

        os.system("cls")
        print(*self.cars, sep=", ")
        sleep(5)
        os.system("cls")

    def play(self):
        self.userIn = input(
            "{}. try, What brand did I choose?:  ".format(self.count + 1))
        if self.userIn == self.rand:
            print("Nice you got it!")
            self.count = 3
        else:
            print("Nope that's not it".format(self.count))
            self.count += 1


def main():
    try:
        os.system("cls")
        print(
            """Guess what brand did I choose, you have 3 tries and 5 seconds \n to view what brands are available."""
        )
        sleep(3)
        game = Game()
        game.start()
        while game.count != 3:
            game.play()
    except KeyboardInterrupt:
        exit("Goodbye...")

main()