## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass
## Dog is-an animal
class Dog(Animal):

    def __init__(self, name):
        #this object has-a name
        self.name = name

## Cat is-an animal
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## Person is-a object
class Person(object):
    def __init__(self, name):
        #person has-a name
        self.name = name

#employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ##??????
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

# Fish is-a object
class Fish(object):
    pass

# Salmon is-a Fish:
class Salmon(Fish):
    pass

#Halibut(Fish):
class Halibut(Fish):
    pass 

rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover 

flipper = Fish()

crouse = Salmon()

harry = Halibut()