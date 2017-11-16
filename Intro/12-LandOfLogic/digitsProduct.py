#!/bin/python3
import sys
"""
# Description
# 
# Given an integer product, find the smallest positive (i.e. greater than 0) 
# integer the product of whose digits is equal to product. If there is no such 
# integer, return -1 instead.
#
# Example
#
# For product = 12, the output should be
# digitsProduct(product) = 26;
#
# For product = 19, the output should be
# digitsProduct(product) = -1.
#
# Input/Output
#
# [input] integer product
# Guaranteed constraints:
# 0 ≤ product ≤ 600.
#
# [output] integer
#
# Solution:

"""
##############
# SOLUTION 1 #
##############
def digitsProduct(product):
    result = product
    digits = []
    if product == 0:
        return 10
    elif product <= 9:
        return product
    else:
        while result > 1:
            for divisor in range(9,1,-1):
                if result % divisor == 0:
                    result = result / divisor
                    digits.append(divisor)
                    break
                elif divisor == 2:
                    digits = []
                    digits.append(-1)
                    result = 0
                    break
    return int(''.join(str(x) for x in reversed(digits)))

##############
# SOLUTION 2 #
##############
#def digitsProduct(product):
#    if product ==0:
#        return 10
#    for i in range(2*3*4*5*6*7*8*9):
#        r = 1
#        for j in str(i):
#            print("i, j => ", i, j)
#            r *= int(j)
#            print("r    => ", r)
#        if r == product:
#            return i
#    return -1
    

print(digitsProduct(12))                          # 26 
print(digitsProduct(19))                          # -1
print(digitsProduct(450))                         # 2559
print(digitsProduct(0))                           # 10
print(digitsProduct(13))                          # -1
print(digitsProduct(1))                           # 1
print(digitsProduct(243))                         # 399
print(digitsProduct(576))                         # 889
print(digitsProduct(360))                         # 589
print(digitsProduct(33))                          # -1
