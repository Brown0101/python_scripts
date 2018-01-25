#!/bin/python
# Python 2.7

import os


with open('heros.txt', 'a') as heros:
    heros.write("Silver Surfer\n")


#heros_file = open('heros.txt', 'a')

# Print without space
#print(heros_file.read())

# Print with space
#for line in heros_file:
#   print(line)

#heros_file.writelines(['Silver Surfer\n', 'Gambit\n'])

#heros_file.close()
