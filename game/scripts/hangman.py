#!/usr/bin/env python3

from time import sleep
from os import listdir
import random 

words=[]
path="./topics/"
fillcount=0
miss=0
cont=True
# hitflag is used to flag a word 'miss' and to prompt a call to the next hangman 'stage'
hitflag=False
sg=[]

def stages(b):
    if b == 1:
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("------")

    if b == 2:
        print("")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("------")

    if b == 3:
        print(" _____")
        print(" |/")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("------")

    if b == 4:
        print(" _____")
        print(" |/  |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("------")

    if b == 5:
        print(" _____")
        print(" |/  |")
        print(" |   O")
        print(" |")
        print(" |")
        print(" |")
        print("------")

    if b == 6:
        print(" _____")
        print(" |/  |")
        print(" |   O")
        print(" |   |")
        print(" |")
        print(" |")
        print("------")

    if b == 7:
        print(" _____")
        print(" |/  |")
        print(" |   O")
        print(" |  -|")
        print(" |")
        print(" |")
        print("------")

    if b == 8:
        print(" _____")
        print(" |/  |")
        print(" |   O")
        print(" |  -|-")
        print(" |")
        print(" |")
        print("------")

    if b == 9:
        print(" _____")
        print(" |/  |")
        print(" |   O")
        print(" |  -|-")
        print(" |  /")
        print(" |")
        print("------")

    if b == 10:
        print(" _____")
        print(" |/  |")
        print(" |   O")
        print(" |  -|-")
        print(" |  / \\")
        print(" |")
        print("------")

# a hokey function thats called to open the topics file
def opentopic(path,topic):
    with open(f"{path}/{topic}", 'r', encoding='utf-8') as f:
        words=list(f)
    return words

print("Welcome to HANGMAN!!")
print("\nFirstly, choose the topic of words to guess...")

# this part pulls the topic file for the questions
# (too be honest, I ripped off this comprehension)
print([f for f in listdir(path)])

topic=input("Select from the list above: ")
words=opentopic(path,topic)
# this is the hangman word to guess
word=words[random.randint(1,10)].strip()

# set the initial word guess length
print(word)
for a in range(len(word)):
    if word[a] == ' ':
        sg.append(" ")
    else:
        sg.append("-")

print(f"The topic is {words[0]}")
print("Guess the letters to the word below...")

while cont:
    print("\n")

    for item in sg:
        print(item, end="")

    print("\n")

    while True:
        g = input("\nEnter letter guess : ")
        if len(g) == 1 and g.isalpha():    
            break;

    print("\n")

    # this part matches the guess to the word to find
    for j in range(len(word)):
        if g==word[j].lower():
            sg[j]=word[j]
            # needed a way to flag when the word had been guessed, not very elegant though
            # later the fillcount is compared with len(word) 
            fillcount+=1
            hitflag=True

    if hitflag==False:
        miss+=1
        stages(miss)

    hitflag=False

    print(fillcount)
    print(len(sg))
    if fillcount == len(sg):
        print("in fillcount")
        for item in sg:
            print(item, end="")
        print("\n\nYou correctly guessed the word, well done!")
        print("------------------------------------------")
        # setting the cont bool ends the main while loop
        cont=False

    if miss == 10:
        print("\n\noh dear, you didn't correctly guess the word before HANGMAN got HUNG!")
        print("---------------------------------------------------------------------")
        cont=False

print("\n\n")
