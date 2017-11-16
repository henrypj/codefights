#!/bin/python3
import sys
"""
# Description
# 
# A media access control address (MAC address) is a unique identifier assigned
# to network interfaces for communications on the physical network segment.
#
# The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly
# form is six groups of two hexadecimal digits (0 to 9 or A to F), separated by
# hyphens (e.g. 01-23-45-67-89-AB).
#
# Your task is to check by given string inputString whether it corresponds to 
# MAC-48 address or not.
#
# Example
#
# For inputString = "00-1B-63-84-45-E6", the output should be
# isMAC48Address(inputString) = true;
#
# For inputString = "Z1-1B-63-84-45-E6", the output should be
# isMAC48Address(inputString) = false;
#
# For inputString = "not a MAC-48 address", the output should be
# isMAC48Address(inputString) = false.
#
# Input/Output
#
# [input] string inputString
# Guaranteed constraints:
# 15 ≤ inputString.length ≤ 20.
#
# [output] boolean
# true if inputString corresponds to MAC-48 address naming rules, false otherwise.
#
# Solution:
"""
##############
# SOLUTION 1 #
##############
import re
def isMAC48Address(inputString):
    return True if re.match("^([0-9A-F]{2}-){5}[0-9A-F]{2}$", inputString) else False

print(isMAC48Address("00-1B-63-84-45-E6"))                  # True
print(isMAC48Address("Z1-1B-63-84-45-E6"))                  # False
print(isMAC48Address("not a MAC-48 address"))               # False
print(isMAC48Address("FF-FF-FF-FF-FF-FF"))                  # True
print(isMAC48Address("00-00-00-00-00-00"))                  # True
print(isMAC48Address("G0-00-00-00-00-00"))                  # False
print(isMAC48Address("02-03-04-05-06-07-"))                 # False
print(isMAC48Address("12-34-56-78-9A-BC"))                  # True
print(isMAC48Address("FF-FF-AB-CD-EA-BC"))                  # True
print(isMAC48Address("12-34-56-78-9A-BG"))                  # False

