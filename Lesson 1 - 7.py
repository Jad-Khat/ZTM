# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 16:14:56 2023

@author: l
"""

"""
#Password Checker Exercise# Lesson 1
"""
username = input("Enter a username: ")
password = input("Enter a password: ")
password_length = len(password)
hidden_password = "*"*password_length
print(f"Dear {username}, your password {hidden_password} is {password_length} characters long")

"""
#Lists# Lessoon 2
"""
# A list is an "ordered" series of "objects" of any type
li = [1,2,3,4,5]
li2 = ["a", "b", "c"]
li3 = [1,2,"a",True]
"""
- Lists are a form of arrays
- Lists are data structures
- A data structure is used to oraganize data

Ex:
    
amazon_cart = ["notebooks", "sunglasses"]
print("amazon_cart[0]")#prints notebooks
"""
"""
#List Slicing# Lesson 3
"""
#Example of string Slicing
string = "hellooooo"
print(string[0:2:1])

#Another way to write lists
amazon_cart = [
    "notebooks",
    "sunglasses",
    "toys",
    "copybooks"]

print(amazon_cart[0:2])#try to read this as taking from the first item (0) to the second item (2)
print(amazon_cart[0::2])#means print everything from the first item (0) till the last item while also skipping every second item
#remember that strings are immutable

#Ex:
string = "grape"
string[0] = "z" #Doesn't work
#We can only change the whole string such as string = hello -> string = goodbye
"""
"""
#However, lists are immutable
amazon_cart = [
    "notebooks",
    "sunglasses",
    "toys",
    "copybooks"]
amazon_cart[0] = "laptops"
print(amazon_cart)#this will show laptops in place of notebooks

#Now let's try list slicing
print(amazon_cart[1:3])
print(amazon_cart)
#You can also do
new_list = amazon_cart[0:3]
new_list[0] = "gum"
print(new_list)
#Be careful of the following:
new_list = amazon_cart
new_list[0] = "gum"
print(new_list)
print(amazon_cart) #Even amazon_cart will change its list and have "gum at position 0
#To fix this issue the following should be done
new_list = amazon_cart[:]
new_list[0] = "gum"
print(new_list)
print(amazon_cart)

"""
#Matrix# Lesson 4
"""
#matrices include multiple lists
matrix = [# This is 2 dimensional since we use the brackets twice even though we have more than 2 lists
    [1,2,3], 
    [2,4,6],
    [7,8,9]
]
"""
to have a 3 dimensional matrix we write it like this:
matrix = [
    [
     [1,2,3,4]
     ]
]
"""
# process a multi-dimensional list (meanig to get exact info from a list)
print(matrix[0][1])#This means, take the item in position 1 (second item) from the list of position 0 (first list)

"""
#List Methods# Lesson 5
"""
basket = [1,2,3,4,5]
print(len(basket)) #len can also show the length of a list

#adding method (This method only adds to the end of a list)
new_list= basket.append(100)
print(new_list)#shows "None" and not the new list
print(basket)#Shows the basket list with the new appended item
#in order for the new list to append like the basket list we need to write
basket = [1,2,3,4,5]
basket.append(100) # This adds 100 to the items in the list
new_list = basket
print(new_list)
print(basket)

#insert method (This method enter based on the signified position)
"""#IMP
#keep in mind that positions within a list are known as index
"""
basket = [1,2,3,4,5]
basket.insert(4, 100)
print(basket)
#extend method (Takes an iterable) (Adds a whole list into the existing list)
basket = [1,2,3,4,5]
basket.extend([100,101])
print(basket)
#removing method (pop method) (Removes depending on the index)
basket = [1,2,3,4,5,100]
basket.pop()#Removes what is that the end of the list
print(basket)
basket.pop()
print(basket)#Removes both the last and the second to last item
basket.pop(0)#Removes the item at the first index
print(basket)
#remove method (Remove a specific value rather than index)
basket = [1,2,3,4,5,100]
basket.remove(3)
print(basket)
"""
#IMP
the pop method returns the value (like when creating functions).
Therefore when writing:
basket = [1,2,3,4,5]
new_list = basket.pop(3)
print(new_list)#This will not show none, but rather the value of the item that was removed
However, the remove method does not return a value
Therefore, if we write:
basket = [1,2,3,4,5]
new_list = basket.remove(3)
print(new_list)#This will show none
In order to combat this we write it in this way
basket = [1,2,3,4,5]
basket.remove(3)
new_list = basket
print(new_list)
"""
#clear method (Empties the lists) (Does not return any value)
basket = [1,2,3,4,5]
basket.clear()
print(basket)

"""
#List Methods 2# Lesson 6
"""

#index method
basket = [1,2,3,4,5]
basket.index(2, 0, 3) #returns the value at index 2
#basket.index(value, starting index, ending index)
#in other words the index function looks for a specific value within the range specified within the list

print(2 in basket) # Shows true
print(89 in basket) #Shows False
print(basket.count(2)) #Prints the amount of times a value was repeated within a list

"""
#List Methods 3# Lesson 7
"""
#sort method
basket = [1,2,3,4,5,7,6,8]
basket.sort()
print(basket) #prints [1,2,3,4,5,6,7,8] 
# Using the sorted function (This does not modify the list but rather creates a copy of the basket and sorts it)
sorted(basket)
print(basket)
"""
This is as if we're saying:
    basket = [1,2,3,4,5,8,6,7]
    new_list = basket[:]
    new_list.sort()
    print(new_list)
"""
# Using the sorted function within the print function
print(sorted(basket))
#Rather than writing new_list = basket[:] we can write
#new_list = basket.copy() (using the copy method)

#reverse method (reverses the basket from last to first)
basket = [1,2,3,4,5]
basket.reverse()
print(basket)

"""
In order to reverse a sorted basket we write:
basket = [1,2,3,4,5]
basket.sort()
basket.reverse()
print(basket)
"""
#This reverses after sorting the values (from last to first)
basket = [1,2,3,4,5,8,6,7]
basket.sort()
basket.reverse()
print(basket)

#This sorts after reversing (from first to last)
basket = [1,2,3,4,5,8,6,7]
basket.reverse()
basket.sort()
print(basket)
