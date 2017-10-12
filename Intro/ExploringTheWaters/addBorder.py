#!/bin/python3
import sys
"""
# Description
# 
# Given a rectangular matrix of characters, add a border of asterisks(*) to it.
#
# Example:
# 
# For 
#
# picture = ["abc",
#            "ded"]
#
# The output should be:
#
# addBorder(picture) = ["*****",
#                       "*abc*",
#                       "*ded*",
#                       "*****"]
#
# Input Format
#
# array.string picture
# A non-empty array of non-empty equal-length strings.
#
# Constraints
# 1 ≤ picture.length ≤ 5,
# 1 ≤ picture[i].length ≤ 5.
#
# Output Format 
#
# array.string
# The same matrix of characters, framed with a border of asterisks of width 1.
#
# Solution:
"""
##############
# SOLUTION 1 #
##############
def addBorder(picture):
    border = "*" * (len(picture[0])+2)
    borderPic = [border]                    # Add top border
    for i in picture:
        borderPic.append('*' + i + '*')     # Add edge borders
    borderPic.append(border)                # Add bottom border
    return borderPic

picture = ["abc",
           "ded"]

print(addBorder(picture))