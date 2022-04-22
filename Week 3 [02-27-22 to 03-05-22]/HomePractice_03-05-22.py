#-------------------------03/05/22--------------------------------------
#-------------------------03/06/22--------------------------------------
#-----------------------Home Practice-----------------------------------
#----------------Canvas, Module 2, Lesson: While Loops-------------------
''' 
What we will learn:

"while" loop syntax
infinite loops
when to use while loops
how to break a loop

'''
#--------------Count to X------------------------------------
''' 
Write a script that asks the user for a number, 
then prints all of the numbers up to and including that number:

'''
# def user_inputs_mngr (input, storage):
#     pass

# user_storage = []

# while True: #<-- Infinite Loop - that prints all the user inputs
#     user_input = int(input("\nPlease Enter a Number: "))
#     user_storage.append(user_input)
#     print("\nThese Are the Numbers: ", user_storage)


#---------------Count N to M----------------------------------
'''
Write a script that asks the user for a two numbers, 
then prints all of the numbers including and between both numbers
'''

# number_1 = int(input("\nPlease Enter Low Number: "))
# number_2 = int(input("\nPlease Enter High Number: "))

# x = number_1
# y = number_2

# while x <= y: #<-- Prints all the values between two inputs
#     print(x)
#     x += 1

#-------------Count Odd N to M--------------------------------
'''
Write a script that asks the user for a two numbers, 
then prints all of the odd numbers including and between both numbers
'''

# user_input1 = int(input("\nPlease Enter Low Number: "))
# user_input2 = int(input("\nPlease Enter Hight Number: "))

# a = user_input1
# b = user_input2

# while a <= b:
#     if a%2 != 0:
#         print(a)
#     a += 1

#---------FizzBuzz---------------------------------------------
''' 
Write a script that asks the user for a number. Print all the numbers between 0 and that number except:

If the number is divisible by 3, print fizz
If the number is divisible by 5, print buzz
if the number is divisible by both 3 and 5, print fizzbuzz
'''

# please_enter = int(input("\nPlease Enter A Number: "))

# c = please_enter
# d = 0
# while d <= c:
#     if d%3==0: #<---If the number is divisible by 3
#         print("fizz")
#     elif d%5==0: #<-- If the number is divisible by 5
#         print("buzz") 
#     elif (d%3==0 and d%5==0): #<-- If the number is divisible by 3 and 5
#         print("fizz buzz")
#     else:
#         print(d) #<-- If its none of the conditions, the number prints
#     d += 1 #<-- number is incremented by 1 and the loops starts back over


#--------Grandma CLI-----------------------------------------------------

'''
Write a grandma script that interacts with the user.

Whatever you say to grandma (whatever you type in), she should respond with: HUH?! SPEAK UP, SONNY!
However, if you shout it (type in all capitals), she can hear you (or at least she thinks so) and 
yells back NO, NOT SINCE 1938!
You can't stop talking to grandma until you shout BYE
'''


while True:
    speak = input("\nTalk to Grandma: ")
    if speak.isupper() == False:
        print("\nHUH!, SPEAK UP, SONNY")
        
    elif speak.isupper() == True:
        print("\nNO, NOT SINCE 1938!")

    if speak == "bye" or speak == "BYE": #<--Will terminate the program 
        print("\nCome Back Soon")
        exit()



      



