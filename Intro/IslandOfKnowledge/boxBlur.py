#!/bin/python3
import sys
"""
# Description
# 
# Last night you partied a little too hard. Now there's a black and white photo
# of you that's about to go viral! You can't let this ruin your reputation, so
# you want to apply the box blur algorithm to the photo to hide its content.
#
# The pixels in the input image are represented as integers. The algorithm 
# distorts the input image in the following way: Every pixel x in the output 
# image has a value equal to the average value of the pixel values from the 
# 3 × 3 square that has its center at x, including x itself. All the pixels 
# on the border of x are then removed.
#
# Return the blurred image as an integer, with the fractions rounded down.
#
# Example:
# 
# For
#
# image = [[1, 1, 1], 
#         [1, 7, 1], 
#         [1, 1, 1]]
#
# the output should be 
# boxBlur(image) = [[1]].
#
# To get the value of the middle pixel in the input 3 × 3 square: 
# (1 + 1 + 1 + 1 + 7 + 1 + 1 + 1 + 1) = 15 / 9 = 1.66666 = 1. The border 
# pixels are cropped from the final result.
# 
# For
#
# image = [[7, 4, 0, 1], 
#          [5, 6, 2, 2], 
#          [6, 10, 7, 8], 
#          [1, 4, 2, 0]]
#
# the output should be
# boxBlur(image) = [[5, 4], 
#                   [4, 4]] 
#
# There are four 3 × 3 squares in the input image, so there should be four 
# integers in the blurred output. To get the first value: 
# (7 + 4 + 0 + 5 + 6 + 2 + 6 + 10 + 7) = 47 / 9 = 5.2222 = 5. The other three 
# integers are obtained the same way, then the surrounding integers are cropped
# from the final result.
#
# Input Format
#
# array.array.integer image
# An image, stored as a rectangular matrix of non-negative integers.
#
# Constraints
# 3 ≤ image.length ≤ 10
# 3 ≤ image[0].length ≤ 10
# 0 ≤ image[i][j] ≤ 255
#
# Output Format
#
# array.array.integer
# A blurred image represented as integers, obtained through the process in the 
# description.
#
# Solution:
"""
##############
# SOLUTION 1 #
##############
def boxBlur(image):
    DEBUG  = False
    starti = 0
    startj = 0
    rows   = len(image)
    cols   = len(image[0])
    numSquares = (rows - 2) * (cols - 2)
    L = [[0] * (cols-2) for i in range(rows-2)]
    if DEBUG:
        print("rows       => ", rows)
        print("cols       => ", cols)
        print("numSquares => ", numSquares)
        print("L => ", L)
        
    while numSquares > 0:
        sum = 0
        if DEBUG:
            print("i range is from: ", starti, " to: ", starti + 2)
        for i in range(starti, starti + 3):
            if DEBUG:
                print("i => ", i)
                print("image[i] => ", image[i])
                print("j range is from: ", startj, " to: ", startj + 2)
            for j in range(startj, startj + 3):
                if DEBUG:
                    print("j => ", j)
                    print("image[i][j] => ", image[i][j])
                sum += image[i][j]
        # Done summing square, add average to list
        L[starti][startj] = sum // 9
        numSquares -= 1
        if DEBUG:
            print("L[Si][Sj]  => ", L[starti][startj])
            print("numSquares => ", numSquares)
            print("startj + 3 => ", startj + 3)
            print("starti + 3 => ", starti + 3)
        if startj + 3 < cols:
            # Another square on this level with starti, so increment startj
            startj += 1
            if DEBUG:
                print("More squares at level: ", starti)
                print("New startj => ", startj)
        elif starti + 3 < rows:
            # Another level of squares exist, increment starti and reset startj
            starti += 1
            startj = 0
            if DEBUG:
                print("Jumping to new level of squares at level: ", starti)
                print("New startj => ", startj)
            
    return(L)
    
print(boxBlur([[1,1,1], 
         [1,7,1], 
         [1,1,1]]))                       # [[1]]
    
print(boxBlur([[0,18,9], 
               [27,9,0], 
               [81,63,45]]))              # [[28]]

print(boxBlur([[36,0,18,9], 
               [27,54,9,0],         
               [81,63,72,45]]))           # [[40,30]]
    
print(boxBlur([[7,4,0,1], 
               [5,6,2,2], 
               [6,10,7,8], 
               [1,4,2,0]]))               # [[5,4], [4,4]]
    
print(boxBlur([[36,0,18,9,9,45,27], 
               [27,0,54,9,0,63,90], 
               [81,63,72,45,18,27,0],     # [[39,30,26,25,31],
               [0,0,9,81,27,18,45],       #  [34,37,35,32,32],
               [45,45,27,27,90,81,72],    #  [38,41,44,46,42], 
               [45,18,9,0,9,18,45],       #  [22,24,31,39,45], 
               [27,81,36,63,63,72,81]]))  #  [37,34,36,47,59]]   
    