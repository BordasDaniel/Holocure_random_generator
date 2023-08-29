import json
import random
import time


class Suffer:
    def __init__(self):
        self.rerolls = 3
        self.data = self.importing()
        self.current_character = None
        self.character_roll()
        self.current_stage = None
        self.stage_roll()

    def startup(self):
        while not (user := input(
                'Are you ready to pull? (Y/N)'
                '\nYou can also quit from the program by typing "quit"'
                '\nYour answer: ')) == 'Y' and not user == 'y':
            print('Sure, I can wait')
            time.sleep(60)
        else:
            self.calling()

    def character_roll(self):
        random_character_index = random.randint(0, len(self.data["all characters"]) - 1)
        self.current_character = self.data["all characters"][random_character_index]

    def stage_roll(self):
        random_stage_index = random.randint(0, len(self.data["all stages"]) - 1)
        self.current_stage = self.data["all stages"][random_stage_index]

    def calling(self):
        self.linebreaker()
        self.character_roll()
        self.stage_roll()
        self.datas_writeout()
        self.linebreaker()
        self.check_rerolls()

    def datas_writeout(self):
        print(
              f"The character's name: {self.current_character['Name']}"
              f"\nThe character's placement is in the {self.current_character['Row']}th row"
              f"\nThe character's placement is in the {self.current_character['Column']}th column"
              f"\nThe current stage: {self.current_stage['Stage']}"
              )

    def check_rerolls(self):
        if self.rerolls > 0:
            while not (user := input(
                    f'Are you satisfied with your pull? (Y/N)'
                    f'\nRemember you have {self.rerolls} rerolls left.'
                    f'\nYour answer: ')) == 'Y' and not user == 'y' and not user == 'N' and not user == 'n':
                print('Value error\nPlease answer with (Y/N)')
            if user == 'Y' or user == 'y':
                self.rerolls -= 1
                self.calling()
            else:
                self.linebreaker()
                print(f'Your final choice:')
                self.datas_writeout()
                self.anticheat()
        else:
            print(f"Sorry but you're out of rerolls.\nSo you have to take that.")
            self.linebreaker()
            self.anticheat()

    @staticmethod
    def welcome():
        print(
            "Welcome to my program!\nThis program was written in Holocure v0.6.1693021031"
            "\nIt may need some debugging if you're using the newer of the game."
            "\nAnyways have fun and good luck!")

    @staticmethod
    def linebreaker():
        print(f'-------------------------------------')

    @staticmethod
    def anticheat():
        minutes_left = 15
        while not minutes_left == -1:
            print(f'{minutes_left} minutes left until you can roll a new character.')
            time.sleep(60)
            minutes_left -= 1
        else:
            Suffer().startup()

    @staticmethod
    def importing():
        with open("datas.json", "r") as f:
            return json.load(f)


if __name__ == '__main__':
    Suffer.welcome()
    Suffer.linebreaker()
    Suffer().startup()
