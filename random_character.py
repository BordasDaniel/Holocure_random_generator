import json
import random
import time


class Suffer:
    def __init__(self):
        self.rerolls = 3
        self.data = self.importing()
        self.current_character = None
        self.current_stage = None
        self.current_mode = None
        self.current_food = None

    def startup(self):
        while not (user := input(
                'Are you ready to pull?'
                '\n1. Yes'
                '\n2. No'
                '\n3. Quit program"'
                '\nYour answer: ')) in ['1', '2', '3']:
            print("Value error")
        else:
            match user:
                case '1':
                    self.calling()
                case '2':
                    print('Sure I can wait.'
                          '\nIf you change your mind, come back in 1 minute')
                    time.sleep(60)
                    self.startup()
                case '3':
                    print('See you next time!')
                    quit()

    def character_roll(self):
        random_character_index = random.randint(0, len(self.data["all characters"]) - 1)
        self.current_character = self.data["all characters"][random_character_index]

    def stage_roll(self):
        random_stage_index = random.randint(0, len(self.data["all stages"]) - 1)
        self.current_stage = self.data["all stages"][random_stage_index]

    def mode_roll(self):
        random_mode_index = random.randint(0, len(self.data["all difficulties"]) - 1)
        self.current_mode = self.data["all difficulties"][random_mode_index]

    def food_roll(self):
        random_food_index = random.randint(0, len(self.data["all foods"]) - 1)
        self.current_food = self.data["all foods"][random_food_index]

    def calling(self):
        self.linebreaker()
        self.character_roll()
        self.stage_roll()
        self.mode_roll()
        self.food_roll()
        self.datas_writeout()
        self.linebreaker()
        self.check_rerolls()

    def datas_writeout(self):
        print(
            f"The character's name: {self.current_character['Name']}"
            f"\nThe character's placement is in the {self.current_character['Row']}th row"
            f"\nThe character's placement is in the {self.current_character['Column']}th column"
            f"\nThe current stage: {self.current_stage['Stage']}"
            f"\nThe current mode: {self.current_mode['Mode']}"
            f"\nThe current food: {self.current_food['Food']}"
        )

    def check_rerolls(self):
        if self.rerolls > 0:
            while not (user := input(
                    f'Are you satisfied with your pull?'
                    f'\n1. Reroll parameters.'
                    f'\n2. Lock in the parameters.' 
                    f'\nRemember you have {self.rerolls} rerolls left.'
                    f'\nYour answer: ')) in ['1', '2']:
                self.linebreaker()
                print('Value error\nPlease answer with (1/2)')
                self.linebreaker()
            match user:
                case '1':
                    self.rerolls -= 1
                    self.select_reroll_option()
                case '2':
                    self.linebreaker()
                    print(f'Your final choice:')
                    self.datas_writeout()
                    self.linebreaker()
                    self.anticheat()
        else:
            print(f"Sorry but you're out of rerolls.\nSo you have to take that.")
            self.linebreaker()
            self.anticheat()

    def select_reroll_option(self):
        while True:
            try:
                user_selected_optinon = int(input(f"Please select which one you would like to reroll:"
                                                  f"\n1. Character"
                                                  f"\n2. Stage"
                                                  f"\n3. Mode"
                                                  f"\n4. Food"
                                                  f"\n0. Cancel request"
                                                  f"\nYour answer: "))
                if user_selected_optinon not in [0, 1, 2, 3, 4]:
                    print('Value error')
                    self.linebreaker()
                else:
                    break
            except ValueError:
                print("That's not a valid option.")
                self.linebreaker()

        def __inner_call():
            self.linebreaker()
            print('The new datas:')
            self.datas_writeout()
            self.linebreaker()
            self.check_rerolls()

        match user_selected_optinon:
            case 1:
                self.character_roll()
                __inner_call()
            case 2:
                self.stage_roll()
                __inner_call()
            case 3:
                self.mode_roll()
                __inner_call()
            case 4:
                self.food_roll()
                __inner_call()
            case 0:
                print('Your request have been cancelled.')
                self.rerolls += 1
                self.linebreaker()
                self.check_rerolls()

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
            print(f'{minutes_left} minutes left until you can roll again.')
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
