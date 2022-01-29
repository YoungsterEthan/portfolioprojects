import sys
import time
import random
import numpy as np
import pandas as pd



def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


class move:
    

    def __init__(self, name):
        allMoves = pd.read_csv("moves.csv")
        self.name = name
        self.type = allMoves[allMoves.Name == self.name]['Type'].values[0].lower()
        self.power = int(allMoves[allMoves.Name == self.name]['Power'].values[0])
        self.accuracy = int(allMoves[allMoves.Name == self.name]['Accuracy'].values[0])

    def __repr__(self):
        return self.name

    def use_move(self, Pokemon, Pokemon2):
        random_list = [x for x in range(1, 101)]
        random_number = random.choice(random_list)

        # calculating type effectivness

        types = {"normal": 0, "fire": 1, "water": 2, "electric": 3, "grass": 4, "ice": 5, "fighting": 6, "poison": 7,
                 "ground": 8, "flying": 9, "psychic": 10, "bug": 11, "rock": 12, "ghost": 13, "dragon": 14, "dark": 15,
                 "steel": 16, "fairy": 17}
        types["normal"]

        typeAdv = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0, 1, 1, 0.5, 1],
                            [1, 0.5, 0.5, 1, 2, 2, 1, 1, 1, 1, 1, 2, 0.5, 1, 0.5, 1, 2, 1],
                            [1, 2, 0.5, 1, 0.5, 1, 1, 1, 2, 1, 1, 1, 2, 1, 0.5, 1, 1, 1],
                            [1, 1, 2, 0.5, 0.5, 1, 1, 1, 0, 2, 1, 1, 1, 1, 0.5, 1, 1, 1],
                            [1, 0.5, 2, 1, 0.5, 1, 1, 0.5, 2, 0.5, 1, 0.5, 2, 1, 0.5, 1, 0.5, 1],
                            [1, 0.5, 0.5, 1, 2, 0.5, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 0.5, 1],
                            [2, 1, 1, 1, 1, 2, 1, 0.5, 1, 0.5, 0.5, 0.5, 2, 0, 1, 2, 2, 0.5],
                            [1, 1, 1, 1, 2, 1, 1, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 1, 1, 0, 2],
                            [1, 2, 1, 2, 0.5, 1, 1, 2, 1, 0, 1, 0.5, 2, 1, 1, 1, 2, 1],
                            [1, 1, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 0.5, 1],
                            [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0.5, 1, 1, 1, 1, 0, 0.5, 1],
                            [1, 0.5, 1, 1, 2, 1, 0.5, 0.5, 1, 0.5, 2, 1, 1, 0.5, 1, 2, 0.5, 0.5],
                            [1, 2, 1, 1, 1, 2, 0.5, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 0.5, 1],
                            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 1, 1],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 0.5, 0],
                            [1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 1, 0.5],
                            [1, 0.5, 0.5, 0.5, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0.5, 2],
                            [1, 0.5, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 1, 1, 1, 2, 2, 0.5, 1]])

        x = typeAdv[types[self.type], types[Pokemon2.types]]

        global string_attack

        if x == 1:
            string_attack = "It's effective"
        elif x == 0.5:
            string_attack = "It's not very effective"
        elif x == 2:
            string_attack = "It's super effective!"

        if random_number <= self.accuracy:
            # the move has hit, calculate damage
            damage = ((((((2 * Pokemon.level) / 5) + 2) * self.power *
                        (Pokemon.attack / Pokemon2.defense)) / 50) + 2) * x
            return int(damage)
        else:
            print(f"\n{Pokemon.name}'s attack has missed!")
            string_attack = ""
            return 0


class Pokemon:
    # Initializing the pokemon
    def __init__(self, name, moves, types, EVs, level):
        self.name = name
        self.moves = moves
        self.types = types
        self.attack = EVs['ATTACK']
        self.spAttack = EVs['SP.ATTACK']
        self.spDefense = EVs['SP.DEFENSE']
        self.defense = EVs['DEFENSE']
        self.speed = EVs['SPEED']
        self.level = level
        self.hp = EVs['HP']
        self.staticHp = EVs["HP"]
        self.Bars = "=========="

    # fight function

    def fight(self, Pokemon2):
        # Printing pokemon 1 stats
        print(f'{self.name} VS {Pokemon2.name}!')

        time.sleep(1)

        print(f'\n{self.name}')
        print(f'HEALTH: {self.hp}')
        print(f'ATTACK: {self.attack}')
        print(f'DEFENSE: {self.defense}')

        time.sleep(0.5)
        # printing pokemon 2 stats
        print(f'\n{Pokemon2.name}')
        print(f'HEALTH: {Pokemon2.hp}')
        print(f'ATTACK: {Pokemon2.attack}')
        print(f'DEFENSE: {Pokemon2.defense}')

        time.sleep(1)
        print(f'{self.name}          HEALTH: {self.Bars} ({self.hp} / {self.staticHp})')
        print(f'{Pokemon2.name}          HEALTH: {Pokemon2.Bars} ({Pokemon2.hp} / {Pokemon2.staticHp})')

        objectDict = {}

        if self.speed > Pokemon2.speed:
            objectDict["Fast"] = self
            objectDict["Slow"] = Pokemon2
        elif self.speed < Pokemon2.speed:
            objectDict["Slow"] = self
            objectDict["Fast"] = Pokemon2

        while self.hp > 0 and Pokemon2.hp > 0:
            # Display Screen
            print(f'Go {objectDict["Fast"].name}!')
            for i, x in enumerate(objectDict["Fast"].moves):
                print(f'{i + 1}', x)
            # Testing for bad input
            while True:
                try:
                    isValid = False
                    choice = int(input("Pick a move: "))
                    while not isValid:
                        if choice < 1 or choice > 4:
                            print("Invalid Input. Please try again")
                            choice = int(input("Pick a move: "))
                        else:
                            isValid = True
                    break

                except ValueError:
                    print("Invalid Input. Please try again")
            delay_print(f'{objectDict["Fast"].name} used {objectDict["Fast"].moves[choice - 1]}')

            # Determine Damage
            objectDict["Slow"].hp -= objectDict["Fast"].moves[choice - 1].use_move(objectDict["Fast"],
                                                                                   objectDict["Slow"])
            delay_print("\n" + string_attack + "\n")
            time.sleep(1)

            barPercentage = objectDict["Slow"].hp / objectDict["Slow"].staticHp

            # Very tedious process of determining how many bars
            if barPercentage < 1 and barPercentage >= 0.90:
                objectDict["Slow"].Bars = "========="
            elif barPercentage < 0.89 and barPercentage >= 0.80:
                objectDict["Slow"].Bars = "======== "
            elif barPercentage < 0.79 and barPercentage >= 0.70:
                objectDict["Slow"].Bars = "=======  "
            elif barPercentage < 0.69 and barPercentage >= 0.60:
                objectDict["Slow"].Bars = "======   "
            elif barPercentage < 0.59 and barPercentage >= 0.50:
                objectDict["Slow"].Bars = "=====    "
            elif barPercentage < 0.49 and barPercentage >= 0.40:
                objectDict["Slow"].Bars = "====     "
            elif barPercentage < 0.39 and barPercentage >= 0.30:
                objectDict["Slow"].Bars = "===      "
            elif barPercentage < 0.29 and barPercentage >= 0.20:
                objectDict["Slow"].Bars = "==       "
            elif barPercentage < 0.19 and barPercentage >= 0.10:
                objectDict["Slow"].Bars = "=        "
            elif barPercentage < 0.09 and Pokemon2.staticHp / Pokemon2.hp >= 0.01:
                objectDict["Slow"].Bars = "-        "
            else:
                objectDict["Slow"].Bars = ""

            if objectDict["Slow"].hp < 0:
                objectDict["Slow"].hp = 0

            print(
                f'{objectDict["Fast"].name}          HEALTH: {objectDict["Fast"].Bars} ({objectDict["Fast"].hp} / {objectDict["Fast"].staticHp})')
            print(
                f'{objectDict["Slow"].name}          HEALTH: {objectDict["Slow"].Bars} ({objectDict["Slow"].hp} / {objectDict["Slow"].staticHp})')

            # check if Pokemon2 is alive
            if objectDict["Slow"].hp <= 0:
                delay_print(f'{objectDict["Slow"].name} has fainted!')
                break

            # Display screen
            print(f'Go {objectDict["Slow"].name}!')
            for i, x in enumerate(objectDict["Slow"].moves):
                print(f'{i + 1}', x)

            # Handling bad data
            while True:
                try:
                    isValid = False
                    choice = int(input("Pick a move: "))
                    while not isValid:
                        if choice < 1 or choice > 4:
                            print("Invalid Input. Please try again")
                            choice = int(input("Pick a move: "))
                        else:
                            isValid = True
                    break
                except ValueError:
                    print("Invalid Input. Please try again")

            delay_print(f'{objectDict["Slow"].name} used {objectDict["Slow"].moves[choice - 1]}')

            # Determine Damage
            objectDict["Fast"].hp -= objectDict["Slow"].moves[choice - 1].use_move(objectDict["Slow"],
                                                                                   objectDict["Fast"])
            print("\n" + string_attack)
            time.sleep(1)

            barPercentage2 = objectDict["Fast"].hp / objectDict["Fast"].staticHp

            # Very tedious process of determining how many bars
            if barPercentage2 < 1 and barPercentage2 >= 0.90:
                objectDict["Fast"].Bars = "========="
            elif barPercentage2 < 0.89 and barPercentage2 >= 0.80:
                objectDict["Fast"].Bars = "======== "
            elif barPercentage2 < 0.79 and barPercentage2 >= 0.70:
                objectDict["Fast"].Bars = "=======  "
            elif barPercentage2 < 0.69 and barPercentage2 >= 0.60:
                objectDict["Fast"].Bars = "======   "
            elif barPercentage2 < 0.59 and barPercentage2 >= 0.50:
                objectDict["Fast"].Bars = "=====    "
            elif barPercentage2 < 0.49 and barPercentage2 >= 0.40:
                objectDict["Fast"].Bars = "====     "
            elif barPercentage2 < 0.39 and barPercentage2 >= 0.30:
                objectDict["Fast"].Bars = "===      "
            elif barPercentage2 < 0.29 and barPercentage2 >= 0.20:
                objectDict["Fast"].Bars = "==       "
            elif barPercentage2 < 0.19 and barPercentage2 >= 0.10:
                objectDict["Fast"].Bars = "=        "
            elif barPercentage2 < 0.09 and barPercentage2 >= 0.01:
                objectDict["Fast"].Bars = "-        "
            else:
                objectDict["Fast"].Bars = ""

            if objectDict["Fast"].hp < 0:
                objectDict["Fast"].hp = 0

            print(
                f'{objectDict["Fast"].name}          HEALTH: {objectDict["Fast"].Bars} ({objectDict["Fast"].hp} / {objectDict["Fast"].staticHp})')
            print(
                f'{objectDict["Slow"].name}          HEALTH: {objectDict["Slow"].Bars} ({objectDict["Slow"].hp} / {objectDict["Slow"].staticHp})')

            # check if Pokemon1 is alive
            if objectDict["Fast"].hp <= 0:
                delay_print(f'{objectDict["Fast"].name} has fainted!')
                break

            # Pokemon


# Pokemon moves

#sets pokemon1 moves
pokemon = pd.read_csv('pokestats.csv')
poke1 = input("Choose Pokemon: ").title()
moveset1 = []
for i in range(1,5):
    hit = input("Choose move #" + str(i) + ": ").title()
    moveset1.append(move(hit))



#sets pokemon2 moves
poke2 = input("Choose Pokemon 2: ").title()
moveset2 = []
for i in range(1,5):
    hit = input("Choose move #" + str(i) + ": ").title()
    moveset2.append(move(hit))



# fly = move("Fly", "normal", 90, 95)
# fireBlast = move("Fire Blast", "fire", 110, 85)
# flameThrower = move("Flame Thrower", "fire", 90, 100)
# scratch = move("Scratch", "normal", 40, 100)

# hydroPump = move("Hydro Pump", "water", 110, 80)
# surf = move("Surf", "water", 90, 100)
# bite = move("Bite", "dark", 60, 100)
# flashCannon = move("Flash Cannon", "steel", 80, 100)

# thunder = move("Thunder", "electric", 110, 70)
# hyperBeam = move("Hyper Beam", "normal", 150, 90)

# print(pokemon[pokemon.Name == 'Pikachu'].index)

pokemon1 = Pokemon(pokemon[pokemon.name == poke1]['name'].values[0], [moveset1[0], moveset1[1], moveset1[2], moveset1[3]], pokemon[pokemon.name == poke1]['type1'].values[0],
                    {'ATTACK': pokemon[pokemon.name == poke1]['attack'].values[0], 'DEFENSE': pokemon[pokemon.name == poke1]['defense'].values[0], 
                    'HP': pokemon[pokemon.name == poke1]['hp'].values[0], 'SPEED': pokemon[pokemon.name == poke1]['speed'].values[0], 
                    'SP.ATTACK': pokemon[pokemon.name == poke1]['sp_attack'].values[0], 'SP.DEFENSE': pokemon[pokemon.name == poke1]['sp_defense'].values[0]
                    }, 36)
pokemon2 = Pokemon(pokemon[pokemon.name == poke2]['name'].values[0], [moveset2[0], moveset2[1], moveset2[2], moveset2[3]], pokemon[pokemon.name == poke2]['type1'].values[0],
                    {'ATTACK': pokemon[pokemon.name == poke2]['attack'].values[0], 'DEFENSE': pokemon[pokemon.name == poke2]['defense'].values[0], 
                    'HP': pokemon[pokemon.name == poke2]['hp'].values[0], 'SPEED': pokemon[pokemon.name == poke2]['speed'].values[0],
                    'SP.ATTACK': pokemon[pokemon.name == poke2]['sp_attack'].values[0], 'SP.DEFENSE': pokemon[pokemon.name == poke2]['sp_defense'].values[0]
                    }, 36)

pokemon1.fight(pokemon2)