#!/bin/python3
import sys
"""
# Description
# 
# An email address such as "John.Smith@example.com" is made up of a local part
# ("John.Smith"), an "@" symbol, then a domain part ("example.com").
#
# The domain name part of an email address may only consist of letters, digits,
# hyphens and dots. The local part, however, also allows a lot of different 
# special characters. Here you can look at several examples of correct and 
# incorrect email addresses.
#
# Given a valid email address, find its domain part.
#
# Example
#
# For address = "prettyandsimple@example.com", the output should be
# findEmailDomain(address) = "example.com";
#
# For address = "<>[]:,;@\"!#$%&*+-/=?^_{}| ~.a\"@example.org", the output 
# should be
# findEmailDomain(address) = "example.org".
#
# Input/Output
#
# [input] string address
# Guaranteed constraints:
# 10 ≤ address.length ≤ 50.
#
# [output] string
#
# Solution:
"""
##############
# SOLUTION 1 #
##############
import re
def findEmailDomain(address):
    return re.findall("(?<=@)[a-z]*.[a-z]*$",address)[0]

print(findEmailDomain("prettyandsimple@example.com"))                  # example.com
print(findEmailDomain("<>[]:,;@\"!#$%&*+-/=?^_{}| ~.a\"@example.org")) # example.org
print(findEmailDomain("someaddress@yandex.ru"))                        # yandex.ru
print(findEmailDomain("\" \"@xample.org"))                             # xample.org
