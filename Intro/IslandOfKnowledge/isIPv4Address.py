#!/bin/python3
import sys
"""
# Description
# 
# An IP address is a numerical label assigned to each device (e.g., computer, 
# printer) participating in a computer network that uses the Internet Protocol 
# for communication. There are two versions of the Internet protocol, and thus 
# two versions of addresses. One of them is the IPv4 address.
#
# IPv4 addresses are represented in dot-decimal notation, which consists of 
# four decimal numbers, each ranging from 0 to 255 inclusive, separated by 
# dots, e.g., 172.16.254.1.
#
# Given a string, find out if it satisfies the IPv4 address naming rules.
#
# Example:
# 
# For inputString = "172.16.254.1", the output should be
# isIPv4Address(inputString) = true
#
# For inputString = "172.316.254.1", the output should be
# isIPv4Address(inputString) = false
#
# 316 is not in range [0, 255]
#
# For inputString = ".254.255.0", the output should be
# isIPv4Address(inputString) = false
#
# There is no first number.
#
# Input Format
#
# string inputString
#
# Constraints
# 1 ≤ inputString.length ≤ 30
#
# Output Format
#
# boolean
# true if inputString satisfies the IPv4 address naming rules, false otherwise.
#
# Solution:
"""
##############
# SOLUTION 1 #
##############
def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
    
def isIPv4Address(inputString):
    a = inputString.split(".")
    if len(a) != 4:
        return False
    else:
#        print("a => ", a)
        numValid = 0
        for i in range(4):
#            print("a[i] => ", a[i])
            if not isInt(a[i]):
#                print("Not int")
                return False
            else:
                numValid += 1 if int(a[i]) in range(0,256) else 0
        return True if numValid == 4 else False


print(isIPv4Address("172.16.254.1"))                                # True
print(isIPv4Address("172.316.254.1"))                               # False
print(isIPv4Address(".254.255.0"))                                  # False
print(isIPv4Address("1.1.1.1a"))                                    # False
print(isIPv4Address("1"))                                           # False
print(isIPv4Address("0.254.255.0"))                                 # True
print(isIPv4Address("1.23.256.255."))                               # False
print(isIPv4Address("1.23.256.."))                                  # False
print(isIPv4Address("0..1.0"))                                      # False
print(isIPv4Address("1.1.1.1."))                                    # False
print(isIPv4Address("1.256.1.1"))                                   # False
print(isIPv4Address("a0.1.1.1"))                                    # False
print(isIPv4Address("0.1.1.256"))                                   # False
print(isIPv4Address("129380129831213981.255.255.255"))              # False
print(isIPv4Address("255.255.255.255abcdekjhf"))                    # False
print(isIPv4Address("7283728"))                                     # False