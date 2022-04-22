#-----------------02/27/22---------------------
#Canvas, Reading - Object Oriented Programming
#Ex. Interacive Pet:

class Pet:
    def __init__(self): #<-- Constructor
        self.name = "Cujo" #<-- Name is an Attribute of the instance cujo
        self.fullness = 50 #<-- Fullness is an Attribute of the instance cujo
        self.happiness = 20 #<-- Happiness is an attribute of the instance cujo

#cujo = Pet() #<-- cujo is an "Instance" of Class Pet
#print(cujo.name)
#However, each instance calld from this point forward will have the same attributes as the previous one
#We need to customize each new instance with its own set of attributes.

# This is how we configure each new instance with attributes of its own:
class Custom_Pet:
    #def __init__(self, name, fullness=50, happiness=20) --> This approach provides default argument values
    #def __init__(self, name, fullness, happiness): #<-- this first function is used for defining, or maintaining initial values of an instance
    def __init__(self, name, fullness=50, happiness=20, hunger=5, mopiness=5): #--> This makes the encapsulated attributes configurable
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        #self.hunger = 5 #<-- moves the be_alive amounts to the constructor but doesn't make them configuable
        #self.mopiness = 5 #<-- 
    #Methods - functions inside a class that make use of those values
    def eat_food(self):
        self.fullness += 30
    def get_love(self):
        self.happiness += 30
    #Encapsulation - bundling state (attributes) and behavior (methods) together
    '''
    def be_alive(self):
        self.fullness -= 5
        self.happiness -= 5
     '''
    #Encapsulation that parameterizes the amounts 
    def be_alive(self, hunger, mopiness):
        self.fullness -= hunger
        self.happiness -= mopiness
    
   

#Now the instances have personalities of there own. 
cujo = Custom_Pet("Cujo", 50, 20)
print(cujo.name)
cujo.eat_food() #<-- makes use of the eat_food method
print(cujo.fullness)

benji = Custom_Pet("Benji", 30, 10)
print(benji.name)
benji.eat_food()
print(benji.fullness)

#Inheritance - specialized versions of classes
class CuddlyPet(Custom_Pet): #<-- this is a subclass of Custom_Pet
    pass

benji = CuddlyPet("Benji", 50, 20, 20, 1)
print(benji.fullness, benji.happiness) #<--TEST the subclass
