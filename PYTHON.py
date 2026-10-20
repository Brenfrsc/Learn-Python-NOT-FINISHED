#--------------------------------------SIMPLE DATA TYPES--------------------------------------#

          #Everything wrote with the hash symbol is a comment, it will not execute in the code.

# (Type> STRING)
'STRING'
"string"
                   #By putting a string in single or double quotes, we can create a string.
"""Favs Pokemon List
Gengar
Slowpoke
Pikachu         
"""     #By using triple quotes(not single or double quotes), we can create a multi-line string.         

#(Type> NUMBER INT)
10
-5
0

#(Type> NUMBER FLOAT)
3.14
-2.5
0.0
#(Type> BOOLEAN)
True   
False  #Capital letter T and F. if we use small letter t and f, it will be considered as a variable name.

#--------------------------------------VARIABLES--------------------------------------#

#To Truly understand the data, we need to use VARIABLES.
#With strings.
name = "Brenda Fresco"
name = "Louis Tomlinson" #all values has an amount of characters from 0 to N.
name = "Harry Styles" 
#print(name) -> We wiil get the last value used with name because we replaced the previous values with the new ones.

#Wtih numbers.
randomnumber = 10 
randomnumber += 5   #dditoning
randomnumber -= 3   #Sustracting
randomnumber *= 2.6 #Multiplying
randomnumber /= 4   #Dividing
#print(randomnumber) > This will give us the result of ALL the operations we did.

#HOW TO CONCATENATE VARIABLES?
greeting = "Hello Naruto, welcome to the Hidden Leaf Village!"
goodbywe = "Goodbye Naruto, see yaaa"
#we concatenate using [variable1 + varianble2]
# print(greeting + " " + goodbywe) the string with the space it counts as a character.

Villages_Amount = 5
#We cannot concatenate a string with a number, we need to convert that data into a string.
Villages=f"The amount of Villages in the Naruto Wold is {Villages_Amount}"# the f before the string converts the variable into a FULL string.

#With Booleans.
Uchiha = "Sasuke"
Clan = f"the stundent {Uchiha} is from the Uchiha Clan"
#print("Sasuke" in Clan) >> the in operator checks if the string is in the variable.
    #This will return True.
#print("Sasuke" not in Clan) >> the not in operator checks if the string is NOT in the variable.
    #This will return False.
