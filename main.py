
# # def locate_card(cards, query):
# #   print
# #   pass


# # a = 3 -- 2 -- 1
# # print(a)

# # What are the keywords in python

# import keyword

# print ("The list of keywords is : ")
# print (keyword.kwlist)

# # How to check if a string is a keyword?
# import keyword

# keys =  ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield','Vibhor']

# for counter in range(len(keys)):
#   if keyword.iskeyword(keys[counter]):
#       print(keys[counter] + " is a  python keyword")
#   else:
#       print(keys[counter] + " is not a python keyword")

# import regularexp
# 


# Examples of Iterations for loops 
my_list =  [ 0,1,2,3,4,5]

#Print each value in my_list. Note you can use in keyword  to interate the List 
for item in my_list:
  print ('the value of iem is:' + str(item))


# Print each index and value pair :
for i , value in enumerate(my_list):
  print("the index value is :" + str(i) + "The value is:" + str(value) )


# Print each num er from 0-9 using while loop
i=0
while(i<10):
  print(i)
  i=i+1

# Print each key and dictionay value.Note that you can use the "in" keyword to iterate over dictionay keys
  
