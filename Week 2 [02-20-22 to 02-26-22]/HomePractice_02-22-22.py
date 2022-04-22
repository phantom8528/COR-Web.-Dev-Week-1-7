#How do i print a tab or line breaks
special_characters = "This\tis\ttabbed!\n\n\nAnd has a line that breaks"
print(special_characters)

#Reassigning Variables 
first_number = 23
second_number = 19
the_answer = first_number + second_number
print("The answer is", the_answer)

second_number = 100
print("The Answer is still", the_answer)
print ("Even though the second number is now", second_number)

#Note: the rhs is never recomputed, even though 
#one of its parts has changed

#How do I get values entered by the user
name_of_user = input("What is your name ?: ")
print ("Hello", name_of_user)

#How do I use the a value as a part of a string
name_of_color = input("What is your favorite color ? ")
print("My favorite color is %s" % name_of_color)

name_of_dog = input("What's your dog's name ?: ")
print("His dog's name is %s" % name_of_dog)

#Making Choices Based on a Users Input


