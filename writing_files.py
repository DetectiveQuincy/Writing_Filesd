#-------------------------------------------------------------------------------
# Name:        Writing
# Purpose:
#
# Author:      kenny.coons
#
# Created:     18/10/2019
# Copyright:   (c) kenny.coons 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def appending_to():
    file = open('master_analyst.txt', 'w')
    print("This file is being opened")

def writing_to():
    file = open("master_analyst.txt", 'w')
    print("The file has been opened")
    choice1 = input("what would you like to add to the file")
    file.write(choice1)
    print('File is being closed')
    file.close()

def character_creation():
    name = input("whats you name?")
    race = input(" what is your race")
    gender = input("what is your gender")
    file = open("character_creation.txt" 'w')
    creation = open(file, 'w')
    creatin.write("Player,")
    creation.write(name + "")
    creation.write(race)
    creation.write(race + ",")
    creation.write(gender)
    creation.write(gender + ",")
    print("File is being closed")
    save.close()

def main():
    writing_to()
    appending_to()
    character_creation()


