import json
import random
import time


class Choice:
    def __init__(self, data):
        self.rerolls = 3
        self.data = data
        self.current_character = None
        self.roll()

    def roll(self):
        random_character_index = random.randint(0, len(self.data["all characters"]) - 1)
        self.current_character = data["all characters"][random_character_index]

    def writeout(self):
        print(self.linebreaker())
        self.roll()
        print(f'Your current character: {self.current_character}')
        print(self.linebreaker())
        self.check_rerolls()

    def check_rerolls(self):
        if self.rerolls != 0:
            while not (user := input(
                    f'Are you satisfied with your pull? (Y/N)\nRemember you have {self.rerolls} rerolls left.\nYour answer: ')) == 'Y' and not user == 'y' and not user == 'N' and not user == 'n':
                print('Value error\nPlease answer with (Y/N)')
            if user == 'Y' or user == 'y':
                self.rerolls -= 1
                self.writeout()
            else:
                print(self.linebreaker())
                print(f'You have selected {self.current_character["Name"]}')
                print(self.linebreaker())
                self.anticheat()
        else:
            print(f"Sorry but you're out of rerolls.\nSo you have to take that.")
            print(self.linebreaker())
            self.anticheat()

    @staticmethod
    def welcome():
        print("Welcome to my program!\nThis program was written in Holocure v0.6.1693021031\nIt may need some debugging if you're using the newer of the game.\nAnyways have fun and good luck!")

    @staticmethod
    def linebreaker():
        return f'--------------------------'

    @staticmethod
    def anticheat():
        minutes_left = 15
        while not minutes_left == -1:
            print(f'{minutes_left} minutes left until you can roll a new character.')
            time.sleep(60)
            minutes_left -= 1
        else:
            waiting()


def importing():
    with open("characters.json", "r") as f:
        return json.load(f)


def waiting():
    while not (user := input('Are you ready to pull? (Y/N) ')) == 'Y':
        continue
    else:
        Choice(data).writeout()


if __name__ == '__main__':
    Choice.welcome()
    print(Choice.linebreaker())
    data = importing()
    waiting()
