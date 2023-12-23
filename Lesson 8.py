# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 10:28:31 2023

@author: l
"""
"""
#Common List Patterns# Lesson 8
"""

#Another way to reverse a list:
basket = [1,2,3,4,5]
print(basket[::-1])#This doesn't change the variable, it only changes the display
#In other words to show this in code:
basket = [1,2,3,4,5]
basket.reverse()#This will change the list permanently
print(basket[::-1])#This will only change the list then return it to its most 
#recent form (reversed from basket.reverse())
print(basket[::-1])#This will give the same answer and not reverse the list 
#another time since it is not reversing the list from the prvious line but 
#rather from basket.reverse() as well.

#To create a list quickly you can use the range function
print(list(range(1,100)))
#Another list would be:
print(list(range(0,100)))
#Another way to write range(0,100):
print(list(range(100)))#This automatically goes from 0 to 

#join method (used to join strings)
sentence = ["hi", "my", "name", "is", "JOJO"]
new_sentence = " ".join(sentence)
print(new_sentence)

"""
#List Unpacking# Lesson 9
"""
#When we usually assign a variable to a list we write:
basket = [1,2,3]
#But we can also write:
a,b,c = [1,2,3]
#Unpacking a list is used if we want to use certain values in a list while keeping the unused ones in a list as well
a,b,c, *other = [1,2,3,4,5,6,7]#Here we put the values in the first, second, and third index in a,b, and c while keeping the other values in 1 variable(other)
print(a)
print(b)
print(c)
print(other)

