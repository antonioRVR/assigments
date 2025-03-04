# ## Exercise: Inheritance

# 1. create inheritance using animal Dog relation.


# ```
# for example, 
#     Animal and Dog both has same habitat so create a method for habitat 
# ```

class Animal:
    def habitat(self):
        print("Animal habitat is land")

class Dog(Animal):
    def __init__(self):
        print("Dog is an animal")

d = Dog()
d.habitat()




# 2. use super() constructor for calling parent constructor.

# ```
# class Animal:
#     #code

# class Dog(Animal):
#     super()-it refers Animal class,now you can call Animal's methods.
# ```


# [Solution](https://github.com/codebasics/py/blob/master/Basics/Exercise/17_inheritance/17_inheritance.py)