# ## Exercise: Class and Objects

# 1. Create a sample class named Employee with two attributes id and name 

# ```
# employee :
#     id
#     name
# ```
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# object initializes id and name dynamically for every Employee object created.
 
# ```
# emp = Employee(1, "coder")
# ```

    def display(self):
        print(f"ID: {self.id} \nName: {self.name}")

emp = Employee(1, "coder")


# 2. Use del property to first delete id attribute and then the entire object

del emp.id

try:
    print(emp.id)
except AttributeError:
    print("emp.id is not defined")

del emp
try:
    emp.display()  # it will gives error after deleting emp
except NameError:
    print("emp is not defined")



# [Solution](https://github.com/codebasics/py/blob/master/Basics/Exercise/16_class_and_objects/16_class_and_objects.py)
