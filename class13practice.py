#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 12:07:49 2024

@author: robbiekapacinskas
"""

fh = open("dune_2_reviews.csv")
fh.readline()
dune = {}
for line in fh:
   # print(line)
    "splits the lines and gets rid of \n"
    data = line.strip().split(",")
    "finds the rating score ( it's in the last slot in each line) "
    ratings = int(data[-1])
    print(ratings)
    "checks if rating is in the dictionary, if so it adds 1 to the rating"
    if ratings in dune:
        dune[ratings] += 1
 #checks if rating is not in the dictionary, if not it starts the category and
 #adds 1 to the rating"
    else:
        dune[ratings] = 1
print(dune)

file = str(input("What is your file name: "))

fh = open("%s" %(file))
fh.readline()
word_bank = {}
for line in fh:

    data = line.strip().split(",")
    
    word = str(data[0])

    if word in word_bank:
        word_bank[word] += 1

    else:
        word_bank[word] = 1

sorted_dict = {key: word_bank[key] for key in sorted(word_bank)}

for key, value in sorted_dict.items():
    print(f"{word}, {value}")