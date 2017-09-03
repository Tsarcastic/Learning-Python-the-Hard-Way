class Parent(object):

    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit"

    def altered(self):
        print "PARENT altered()"


class Child(Parent):
    
    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent() #This creates variable called dad that is-a Parent
son = Child() #This creates a variable called son that is-a Child

dad.implicit() #Runs like 6 - is not an override
son.implicit() #Runs like 6 - is not an override

dad.override() #Runs like 3 - is not an override
son.override() #Runs like 14 - is an override

dad.altered() # Line 9 - is not
son.altered() # CBP - PA - CAP