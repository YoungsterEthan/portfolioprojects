import sys
import time
import random
import numpy as np
import pandas as pd
import simpleaudio as sa
import streamlit as st
import pygame


#function that displays text slowly
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

#prints all of the dataframe
def print_full(df):
    pd.set_option('display.max_rows', len(df))
    print(df)
    pd.reset_option('display.max_rows')

#move class. All attributes of the moves and move database
class move:

    def __init__(self, name, df):
        
        self.name = name
        self.type = df[df.Name == self.name]['Type'].values[0].lower()
        self.power = int(df[df.Name == self.name]['Power'].values[0])
        self.accuracy = int(df[df.Name == self.name]['Acc'].values[0])
        self.category = df[df.Name == self.name]['Category'].values[0]

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

            #play sound
            if self.category == 'Physical':
                filename = 'TakeDown.wav'
                wave_obj = sa.WaveObject.from_wave_file(filename)
                play_obj = wave_obj.play()
                play_obj.wait_done()  
                # Wait until sound has finished playing
                damage = ((((((2 * Pokemon.level) / 5) + 2) * self.power *
                            (Pokemon.attack / Pokemon2.defense)) / 50) + 2) * x
                return int(damage)
            #play sound
            elif self.category == 'Special':
                filename = 'Surf.wav'
                wave_obj = sa.WaveObject.from_wave_file(filename)
                play_obj = wave_obj.play()
                play_obj.wait_done()  
                
                damage = ((((((2 * Pokemon.level) / 5) + 2) * self.power *
                            (Pokemon.spAttack / Pokemon2.spDefense)) / 50) + 2) * x
                return int(damage)
            
        else:
            st.write(f"\n{Pokemon.name}'s attack has missed!")
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
        st.write(f'{self.name} VS {Pokemon2.name}!')

        time.sleep(1)

        st.write(f'\n{self.name}')
        st.write(f'HEALTH: {self.hp}')
        st.write(f'ATTACK: {self.attack}')
        st.write(f'SP.ATTACK: {self.spAttack}')
        st.write(f'DEFENSE: {self.defense}')
        st.write(f'SP.DEFENSE: {self.spDefense}')


        time.sleep(0.5)
        # st.writeing pokemon 2 stats
        st.write(f'\n{Pokemon2.name}')
        st.write(f'HEALTH: {Pokemon2.hp}')
        st.write(f'ATTACK: {Pokemon2.attack}')
        st.write(f'SP.ATTACK: {Pokemon2.spAttack}')
        st.write(f'DEFENSE: {Pokemon2.defense}')
        st.write(f'SP.DEFENSE: {Pokemon2.spDefense}')

        time.sleep(1)
        st.write(f'{self.name}          HEALTH: {self.Bars} ({self.hp} / {self.staticHp})')
        st.write(f'{Pokemon2.name}          HEALTH: {Pokemon2.Bars} ({Pokemon2.hp} / {Pokemon2.staticHp})')

        objectDict = {}

        if self.speed > Pokemon2.speed:
            objectDict["Fast"] = self
            objectDict["Slow"] = Pokemon2
        elif self.speed < Pokemon2.speed:
            objectDict["Slow"] = self
            objectDict["Fast"] = Pokemon2

        while self.hp > 0 and Pokemon2.hp > 0:
            # Display Screen
            st.write(f'Go {objectDict["Fast"].name}!')
            for i, x in enumerate(objectDict["Fast"].moves):
                st.write(f'{i + 1}', x)
            # Testing for bad input
            while True:
                try:
                    isValid = False
                    choice = int(st.text_input("Pick a move: "))
                    while not isValid:
                        if choice < 1 or choice > 4:
                            st.write("Invalid Input. Please try again")
                            choice = int(st.text_input("Pick a move: "))
                        else:
                            isValid = True
                    break

                except ValueError:
                    st.write("Invalid Input. Please try again")
            delay_print(f'{objectDict["Fast"].name} used {objectDict["Fast"].moves[choice - 1]}')

            # Determine Damage
            objectDict["Slow"].hp -= objectDict["Fast"].moves[choice - 1].use_move(objectDict["Fast"],
                                                                                   objectDict["Slow"])
            delay_print("\n" + string_attack + "\n")
            time.sleep(1)

            barPercentage = objectDict["Slow"].hp / objectDict["Slow"].staticHp

            objectDict["Slow"].Bars = int(round(barPercentage * 10, 0)) * "="

            if objectDict["Slow"].hp < 0:
                objectDict["Slow"].hp = 0

            st.write(
                f'{objectDict["Fast"].name}          HEALTH: {objectDict["Fast"].Bars} ({objectDict["Fast"].hp} / {objectDict["Fast"].staticHp})')
            st.write(
                f'{objectDict["Slow"].name}          HEALTH: {objectDict["Slow"].Bars} ({objectDict["Slow"].hp} / {objectDict["Slow"].staticHp})')

            # check if Pokemon2 is alive
            if objectDict["Slow"].hp <= 0:
                delay_print(f'{objectDict["Slow"].name} has fainted!')
                break

            # Display screen
            st.write(f'Go {objectDict["Slow"].name}!')
            for i, x in enumerate(objectDict["Slow"].moves):
                st.write(f'{i + 1}', x)

            # Handling bad data
            while True:
                try:
                    isValid = False
                    choice = int(st.text_input("Pick a move: "))
                    while not isValid:
                        if choice < 1 or choice > 4:
                            st.write("Invalid Input. Please try again")
                            choice = int(st.text_input("Pick a move: "))
                        else:
                            isValid = True
                    break
                except ValueError:
                    st.write("Invalid Input. Please try again")

            delay_print(f'{objectDict["Slow"].name} used {objectDict["Slow"].moves[choice - 1]}')

            # Determine Damage
            objectDict["Fast"].hp -= objectDict["Slow"].moves[choice - 1].use_move(objectDict["Slow"],
                                                                                   objectDict["Fast"])
            st.write("\n" + string_attack)
            time.sleep(1)

            barPercentage2 = objectDict["Fast"].hp / objectDict["Fast"].staticHp
            objectDict["Fast"].Bars = int(round(barPercentage2 * 10, 0)) * "="



            if objectDict["Fast"].hp < 0:
                objectDict["Fast"].hp = 0

            st.write(
                f'{objectDict["Fast"].name}          HEALTH: {objectDict["Fast"].Bars} ({objectDict["Fast"].hp} / {objectDict["Fast"].staticHp})')
            st.write(
                f'{objectDict["Slow"].name}          HEALTH: {objectDict["Slow"].Bars} ({objectDict["Slow"].hp} / {objectDict["Slow"].staticHp})')

            # check if Pokemon1 is alive
            if objectDict["Fast"].hp <= 0:
                delay_print(f'{objectDict["Fast"].name} has fainted!')
                break

            # Pokemon


# Pokemon moves

#sets pokemon1 moves
pokemon = pd.read_csv('pokestats.csv')
moveList = pd.read_csv('All_Moves.csv')

#checking if pokemon1 is in dataframe 
notFound = True
while notFound:

    poke1 = st.text_input("Choose Pokemon 1: ", key = '1').title()
    if poke1 in pokemon.name.values:
        notFound = False
    else:
        st.write("Pokemon Does not exist. Try again")

#creating list of moves to choose from
def createDeck(types):
    try:
        unrefined = moveList[(moveList.Type == types[0]) | (moveList.Type == types[1])]
    except IndexError:
        unrefined = moveList[(moveList.Type == types[0])]
    refined = unrefined[['Name', 'Type', 'Acc', 'Category', 'Power']]
    return refined

#whether or not there is one value or two values
try:
    mAvailable = createDeck([pokemon[pokemon.name == poke1]['type1'].values[0].title(), pokemon[pokemon.name == poke1]['type2'].values[0].title()]).reset_index(drop=True)
except AttributeError:
    mAvailable = createDeck([pokemon[pokemon.name == poke1]['type1'].values[0].title()]).reset_index(drop=True)

    

st.write("Moves Available")
st.write(mAvailable)

moveset1 = []
for i in range(1,5):
    inMoves = True
    while inMoves:
        try:
            hit = int(st.text_input("Choose move #" + str(i) + ": ", key =3))
            moveset1.append(move(mAvailable.iloc[hit]['Name'], mAvailable)) #Gets the move based on the index typed in by user
            inMoves = False   
        except IndexError:
            st.write("Move not in set. Try again")

#sets pokemon2 moves

notFound2 = True
while notFound2:
    poke2 = st.text_input("Choose Pokemon: ").title()
    if poke2 in pokemon.name.values:
        notFound2 = False
    else:
        st.write("Pokemon Does not exist. Try again")
try:
    mAvailable2 = createDeck([pokemon[pokemon.name == poke2]['type1'].values[0].title(), pokemon[pokemon.name == poke2]['type2'].values[0].title()]).reset_index(drop=True)
except AttributeError:
    mAvailable2 = createDeck([pokemon[pokemon.name == poke2]['type1'].values[0].title()]).reset_index(drop=True)

st.write("Moves Available")
st.write(mAvailable2)

moveset2 = []
for i in range(1,5):
    inMoves2 = True
    while inMoves2:
        try:
            hit = int(st.text_input("Choose move #" + str(i) + ": "))
            moveset2.append(move(mAvailable2.iloc[hit]['Name'], mAvailable2))
            inMoves2 = False
        except IndexError:
            st.write("Move not in set. Try again")

#Set pokemon with stats
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