## 1. Introduction to Modules ##

import math
root = math.sqrt(99)
flr = math.floor(89.9)

## 2. Importing Using An Alias ##

import math as m
root = m.sqrt(33)

## 3. Importing A Specific Object ##

from math import *
root = sqrt(1001)

## 4. Variables Within Modules ##

import math as m

a = m.sqrt(m.pi)
b = m.ceil(m.pi)
c = m.floor(m.pi)

## 5. The CSV Module ##

import csv
f = open("nfl.csv")
nfl = list(csv.reader(f))

## 6. Counting How Many Times a Team Won ##

import csv
f = open("nfl.csv")
nfl = list(csv.reader(f))
counter = 0
for item in nfl:
    if item[2] == "New England Patriots":
        counter +=1
patriots_wins = counter
print(counter)

## 7. Making a Function that Counts Wins ##

import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

# Define your function here.
def nfl_wins(data,win_team):
    counter = 0
    for item in data:
        if item[2] == win_team:
            counter +=1
    return counter

cowboys_wins = nfl_wins(nfl,"Dallas Cowboys")
falcons_wins = nfl_wins(nfl,"Atlanta Falcons")
    