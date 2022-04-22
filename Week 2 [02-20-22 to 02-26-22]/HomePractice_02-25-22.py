#----------------------------Self-Practice (02/25/22)-----------------------------------
#      '''     <--- Note: Copy and paste for quick commenting out of large blocs of code
#------------------Canvas, Module 2, Day 1, Returning Values----------------------------
#-------> Madlib ------>
#Note --> A Function that allows you to exit during user input
import os 
from time import sleep
 
#os.system("clear") # Linux - OSX 
#os.system("cls") # Windows 

print("\nCanvas Module 2, Day 1, Returning Values - Madlib\n")

def escape_clause(input):
    if input == "Quit":
        print("\nYou've Exited this simulation\n")
        exit()

        

noun_input = input("\nPlease provide a noun, \n\nOR Enter Quit to exit: ") #<----- Input Function - returns a string
escape_clause(noun_input)

verb_input = input("\nPlease present a prenet-tense verb, \n\nOR Enter Quit to exit: ") #<----- Input Function - returns a string
escape_clause(verb_input)

name_input = input("\nPlease choose a name, \n\nOR Enter Quit to exit: ") #<------- Input Function - returns a string
escape_clause(name_input)


#Note --> An Example of Interpolation using the "f-strings" approach
print(f''' 
...AND HERE'S YOUR STORY:
===============================================================
There once was a {noun_input} that suddenly came to life, 
called themselves {name_input} and starting {verb_input} around the town. 
{name_input} decided that {verb_input} was unacceptable and decided to move to the countryside an live a life of solitude.
''')
print("\nCongragulations, This Screen will be cleared in 5 seconds\n")

sleep(10) #<-- Clears the command terminal after viewing the output for 10 seconds

os.system("clear")


#-------> Tip Calculator ------>

print("\nCanvas Module 2, Day 1, Returning Values - Tip Calculator\n")
