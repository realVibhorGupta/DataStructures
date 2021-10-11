
# def locate_card(cards, query):
#   print
#   pass


# a = 3 -- 2 -- 1
# print(a)

# What are the keywords in python

import keyword

print ("The list of keywords is : ")
print (keyword.kwlist)

# How to check if a string is a keyword?
import keyword

keys =  ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield','Vibhor']

for counter in range(len(keys)):
  if keyword.iskeyword(keys[counter]):
      print(keys[counter] + " is a  python keyword")
  else:
      print(keys[counter] + " is not a python keyword")
