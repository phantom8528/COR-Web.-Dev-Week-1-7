#-------------------DIctionaries----------------------
#From Dictionaries Interview Questions - Create a dictioary that resembles a tweet

#This program simulates a tweet

# tweet = {
#     "Name": "John Doe",
#     "Twitter Handle": "@johndoe",
#     "Entry": "This is my first tweet",
#     "Favorite": False,
#     "Reply": False,
#     "Retweet":False}

# print(f'''  
    
#     {tweet["Name"]}  {tweet["Twitter Handle"]}

#     {tweet["Entry"]}

#     Favorite: {tweet["Favorite"]}  | Reply: {tweet["Reply"]}  | Retweet: {tweet["Retweet"]}
    
#      ''')


''' 
#--------------------------Conditional Statements--------------------------------------------------------
#Canvas, Module 2: Programming Fundamentals, Lesson: Conditions in Code

What we will learn:

if/else if/else statement syntax
condition expressions
comparison operators
combining conditions with logical operators

'''

#------------Work or Sleep In--------------------------
''' 
Write a script that asks for a day of the week. If the day is a business day, print 'go to work!'. 
If the day is a weekend day, print 'sleep in!'. If whatever 
the user entered is not a day, print 'enter a valid day'.

 '''

# from imghdr import what


# seven_days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

# what_day = input("\nWhat Day of the Week is it ?:  ")

# for x in seven_days: #<-- Iterates through a list
#     if what_day == "Monday" or what_day == "Tuesday" or what_day == "Wednesday" or what_day == "Thursday" or what_day == "Friday":
#         print(what_day)
#         print("Go To Work")
#         break #<--Prevents iterating through the list 5 times
#     else:
#         print("Sleep In")
#         break

#---------------------------03/05/22--------------------------------------------------------

#------------------------Secret Password----------------------------
''' 
Write a script that asks the user for a password. 
If the user enters the correct word (pick one yourself) 
then print 'Welcome!', otherwise print 'Try Again!'

 '''

# enter_password = input("Please Enter Password: ")
# correct_answer = "password"
# if enter_password == correct_answer:
#     print("Login Successful")
# else:
#     print("Sorry, Try Again")

#---------------------------------------------------------------

'''  

Day of Week

Write a script that asks the user for a number between 1-7. 
Print the corresponding day for the number, (i.e. 1 = 'Sunday', 2 = 'Monday' etc). 
If the input is invalid, print an error message.

 '''

# days_of_the_week = '''  
 
#  DAYS OF THE WEEK

#  ----------------------------------

#  1. Monday

#  2. Tuesday

#  3. Wednesday

#  4. Thursday

#  5. Friday

#  6. Saturday

#  7. Sunday

#  Please Enter the number that corresponds to the day of the week:  
 
#   '''

# numbers_to_days ={
#       1: "Monday",
#       2: "Tuesday",
#       3: "Wednesday",
#       4: "Thursday",
#       5: "Friday",
#       6: "Saturday",
#       7: "Sunday"
#   }

# choice = int(input("\nPlease Enter a Choice: "))

# if choice in numbers_to_days.keys(): #<-- Compares user input to each of the values in the dictionary
#     print("\nHave a Nice Day")
# else:
#     print("\nSorry, Try Again")

    #------------------------Letter Grade----------------------------------

'''
    Write a script that asks for a score number between 0-100. 
    Print the corresponding grade for that number. (i.e. <60 = F, <70 = D, <80 = C, <90 = B, 90+ = A). 
    If the input is invalid, print an error message.
    
'''

# enter_grade = int(input("\nPlease Enter Grade: "))

# if enter_grade <60:
#     print("\nGrade: F\n")
# elif enter_grade <70 and enter_grade >60:
#     print("\nGrade: D\n")
# elif enter_grade <80 and enter_grade >70:
#     print("\nGrade: C\n")
# elif enter_grade <90 and enter_grade >80:
#     print("\nGrade: B\n")
# elif enter_grade <100 and enter_grade >90:
#     print("\nGrade: A\n")
# elif enter_grade >=100:
#     print("\nGrade: A+ --- Excellent Job---\n")
# else:
#     print("\nSorry, Not Valid\n") #<--- Error Message

#------------------------Picnic Game--------------------------------
'''   
Write a function that returns true if the two input strings start with the same letter. 
Write a script that asks the user for their name. 
Ask them for the food they are bringing to the picnic. 
Use the function to check if the food matches the name. 
If it does, tell them they can come to the party. 
If it doesn't, tell them to try again.

'''
#Function used to compare the first letter of two user inputs to see if they match
# def compare_first_letter(input1, input2): 
#     first_letter_name = input1[0] #<--- Refers to the first character inside of a string
#     first_letter_food = input2[0]
#     if first_letter_name == first_letter_food:
#         print("\nWelcome to the Party\n")
#     else:
#         print("\nSorry, Try Again\n")
    

# name = input("\nPlease Enter Name: ")
# food = input("\nWhat Kind of Food Are You Bringing?: ")

# compare_first_letter(name, food)

#---------------------Username Length Validator-----------------------------------
'''  
Write a function that accepts a parameter username, and checks if the username is valid. 
A valid username must be longer than 3 characters and less than 18. 
Use the function in a script that asks the user for a username 
and then tells them if the username is valid or not.

'''
# def length_auth (input): #<-- Function validates a preset number of characters
#     x = len(input)
#     is_between = 3> x <=18 #<-- This returns a boolean
#     if is_between == False:
#         print("\nUsername is Valid\n")
#     else:
#         print("\nNot Enough Characters")

# username = input("\nPlease Enter Your Preferred Username: ")

# print(len(username)) #<-- TEST - Confirm the number of characters before passing it throught the function below

# length_auth(username)


#-----------------------Odd and Divisible by Three-----------------------------------------
'''   
Write a function that returns true if the input number is odd and divisible by 3. 
Write a script that asks the user for a number, 
then pass that number to the function and print a success message if the function returns true.

'''

# def divisible_three(input):
#     is_divisible = input%3
#     if is_divisible==0:
#         print("Congragulations, {} is divisible by 3" .format(input))
#     else:
#         print("Sorry, {} is not divisiible by 3" .format(input))

# number = int(input("\nPlease Enter an Integer that is divisible by three Please: "))

# divisible_three(number)

#---------------------------------------------------------------------------------------------

