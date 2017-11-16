#x`x`!/bin/python3
import sys
"""
# Description
# 
# You are taking part in an Escape Room challenge designed specifically for 
# programmers. In your efforts to find a clue, you've found a binary code 
# written on the wall behind a vase, and realized that it must be an encrypted
# message. After some thought, your first guess is that each consecutive 8 bits
# of the code stand for the character with the corresponding extended ASCII 
# code (https://www.ascii-code.com/).
#
# Assuming that your hunch is correct, decode the message.
#
# Example
#
# For code = "010010000110010101101100011011000110111100100001", the output 
# should be
# messageFromBinaryCode(code) = "Hello!".
#
# The first 8 characters of the code are 01001000, which is 72 in the binary 
# numeral system. 72 stands for H in the ASCII-table, so the first letter is H.
# Other letters can be obtained in the same manner.
#
# Input/Output
#
# [input] string code
# A string, the encrypted message consisting of characters '0' and '1'.
# Guaranteed constraints:
# 0 < code.length < 800.
#
# [output] string
# The decrypted message.
#
# Solution:

"""
##############
# SOLUTION 1 #
##############
def messageFromBinaryCode(code):
#    for i in range(len(code)):
    message = []
#    print(len(code)//8)
    for i in range(len(code)//8):
#        print(i * 8)
        binStr = code[i*8:i*8+8]
#        print(binStr)
#        print(int(binStr, 2))
#        print(chr(int(binStr, 2)))
        message.append(chr(int(binStr, 2)))
    return ''.join(message)

print(messageFromBinaryCode("010010000110010101101100011011000110111100100001")) # Hello!
print(messageFromBinaryCode("01001101011000010111100100100000011101000110100001100101001000000100011001101111011100100110001101100101001000000110001001100101001000000111011101101001011101000110100000100000011110010110111101110101")) # May the Force be with you
print(messageFromBinaryCode("010110010110111101110101001000000110100001100001011001000010000001101101011001010010000001100001011101000010000001100000011010000110010101101100011011000110111100101110")) # You had me at `hello.

