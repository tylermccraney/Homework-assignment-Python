#!/usr/bin/python

from __future__ import division
from __future__ import print_function

# Write a program that will print out the AT content of this DNA sequence. Hint: you can use normal mathematical symbols like add (+), subtract (-), multiply (*), divide (/) and parentheses to carry out calculations on numbers in Python.
shortDNAsequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
# count total sequence length
length = len(shortDNAsequence)
# count the number of As
As = shortDNAsequence.count('A')
# count the number of Ts
Ts = shortDNAsequence.count('T')
# calculate AT content
ATcontent = (As + Ts) / length
# print AT content
print("At content: " + str(ATcontent))

