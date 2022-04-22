#-----------------------02/23/22------------------------
#If..Else Statements
a = 3
b = 4

if b>a:
    print("b is greater than a") #--> lack of indentation will raise an error

#The ...Else Statement

c = 200
d = 33

if c>d:
    print("d is greater than c")
elif c==d:
    print("c and d are equal")
else:
    print("c is greater than d")

#Nested if Statement
x = 41 

if x >10:
    print("Above 10")
    if x>20:
        print("And Alsoe Above 20!")
    else:
        print("but not above 20.")

#The Pass Statement - Empty "If" Statements can cause an error.
#In order to avoid this, put the pass statement on the inside.

y = 400

if y>x:
    pass #<-- Question: Why would a programmer need this?

#While Loops - Execute a set of statements as long as the condition is true
'''
i=1
while i<6:
    print(i)
    i += 1
'''
#While Loop with a Break Statement
i=1
'''
while i<6:
    print(i)
    if i==3:
        break #<-- Once the index reaches 3, the program terminates
    i += 1
#While Loop with a continue statement
while i<6:
    i += 1
    if i==3:
        continue #<-- skips the number 3
    print(i)
'''
#While Loop With an Else Statement
while i<6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
