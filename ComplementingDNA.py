#!/usr/bin/python

from __future__ import division
from __future__ import print_function

# Write a program that will print the complement of this sequence.
shortDNAsequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
# replace A with t
replaceA = shortDNAsequence.replace('A', 't')
# replace T with a
replaceT = replaceA.replace('T', 'a')
# replace C with g
replaceC = replaceT.replace('C', 'g')
# replace G with c
replaceG = replaceC.replace('G', 'c')
# print in upper case
print("Complementary DNA: " + replaceG.upper())

