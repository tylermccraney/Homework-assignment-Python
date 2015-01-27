#!/usr/bin/python

from __future__ import division
from __future__ import print_function

# The sequence contains a recognition site for the EcoRI restriction enzyme, which cuts at the motif G*AATTC (the position of the cut is indicated by an asterisk). Write a program which will calculate the size of the two fragments that will be produced when the DNA sequence is digested with EcoRI.
shortDNAsequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
# find length of 1st fragment
fragment1 = shortDNAsequence.find("GAATTC") + 1
# find length of 2nd fragment
fragment2 = len(shortDNAsequence) - fragment1
# print lengths of both fragments
print("Fragment 1 length: " + str(fragment1) + " bp")
print("Fragment 2 length: " + str(fragment2) + " bp")

# Argh... I can't get this program to work correctly!