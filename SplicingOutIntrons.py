#!/usr/bin/python

from __future__ import division
from __future__ import print_function

# Splicing out introns, part one
# Here is a short section of genomic DNA:
# ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT
# It comprises two exons and an intron. The first exon runs from the start of the sequence to the sixty-third character, and the second exon runs from the ninety-first character to the end of the sequence. Write a program that will print just the coding regions of the DNA sequence.

genomicDNA = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
# get substring of 1st intron
exon1 = genomicDNA[0:63]
# get substring of 2nd intron
exon2 = genomicDNA[90:1000]
# print exons
print("1st exon sequence: " + exon1)
print("2nd exon sequence: " + exon2)

# Splicing out introns, part two
# Using the data from part one, write a program that will calculate what percentage of the DNA sequence is coding.

# Calculate total DNA length
DNAlength = len(genomicDNA)
# calculate length of coding regions
exons_length = len(exon1 + exon2)
# calculate percent coding
coding = exons_length / DNAlength
# print out coding content
print("Percent coding DNA: " + str(coding))

# Splicing out introns, part three
# Using the data from part one, write a program that will print out the original genomic DNA sequence with coding bases in uppercase and non-coding bases in lowercase.

# get substring of intron
intron = genomicDNA[63:90].lower()
# print the whole sequence with exons in caps
print("Genomic DNA formatted EXONinronEXON: " + exon1 + intron +exon2)

