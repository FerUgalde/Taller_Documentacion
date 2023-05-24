#An animal shelter which holds dogs (name,age,breed) operates a FIFO. 
#People must adopt the oldest (based on the arrival date). 
#Create the data structure to maintain the system and implement operations such as enqueue_dogs or dequeue_dogs.
from datetime import datetime 

class Dog:

    def __init__(self, name, age, breed, date):
        self.name = name
        self.age = age
        self.breed = breed
        self.date = date
        self.next = None


class Shelter:

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    
    def print_list(self):
        temp = self.first
        while temp is not None:
            print(f"Name: {temp.name}   Age: {temp.age}   Breed: {temp.breed}   Entry date: {temp.date}")
            temp = temp.next


    def enqueue_dog(self, name, age, breed, date):

        new_dog = Dog(name, age, breed, date)

        if self.length == 0:
            self.first = new_dog
            self.last = new_dog
        else:
            self.last.next =  new_dog
            self.last = new_dog
        self.length += 1 


    def dequeue_dog(self):
        if self.length == 0:
            return "Sorry! There are no more dogs"

        if self.first == self.last:
            temp = self.first
            self.first = None
            self.last = None
        
        else:
            temp = self.first
            self.first = temp.next
            temp.next = None
        self.length -= 1    
        return f"Name: {temp.name}   Age: {temp.age}   Breed: {temp.breed}   Entry date: {temp.date}"


my_animal_shelter = Shelter()

op = 0
while op != 4:
    op = int(input("""
    \n\tWelcome to the Animal Shelter!\n
    1. Put in the shelter
    2. Adopt
    3. Show current dogs at the shelter
    4. Exit\n"""))

    if op == 1:
        today = datetime.today()
        day = f"{today.day}/{today.month}/{today.year}   {today.hour}:{today.minute}"

        name = input("Enter de name:    ")
        age = input("Enter de age:   ")
        breed = input("Enter de breed:  ")
        my_animal_shelter.enqueue_dog(name, age, breed, day)

    elif op == 2:
        get = my_animal_shelter.dequeue_dog()
        print(f'\nThe data of the dog you adopted are: \n\t{get}\n')

    elif op == 3:
        print("\nThe current dogs at the shelter are: ")
        my_animal_shelter.print_list()

    elif op == 4:
        print("\nLeaving the program...\n")
    
    else:
        print("\nInvalid option\n")

