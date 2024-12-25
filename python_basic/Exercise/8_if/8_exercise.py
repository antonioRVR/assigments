# ## Exercise: Python If Condition
# 1. Using following list of cities per country,
#     ```
#     india = ["mumbai", "banglore", "chennai", "delhi"]
#     pakistan = ["lahore","karachi","islamabad"]
#     bangladesh = ["dhaka", "khulna", "rangpur"]
#     ```

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]


#     1. Write a program that asks user to enter a city name and it should tell which country the city belongs to

city = input("Enter a city name: ")

if city in india:
    print(f"{city} is in India")

elif city in pakistan:
    print(f"{city} is in Pakistan")

elif city in bangladesh:
    print(f"{city} is in Bangladesh")

else:
    print(f"{city} is not in the list")


#     2. Write a program that asks udser to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"

city2 = input("Enter a city name: ")

if city in india and city2 in india:
    print(f"{city} and {city2} are in India")
elif city in pakistan and city2 in pakistan:
    print(f"{city} and {city2} are in Pakistan")
elif city in bangladesh and city2 in bangladesh:
    print(f"{city} and {city2} are in Bangladesh")
else:
    print(f"{city} and {city2} are not in the same country")



# 2. Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
#     1. Ask user to enter his fasting sugar level
#     2. If it is below 80 to 100 range then print that sugar is low
#     3. If it is above 100 then print that it is high otherwise print that it is normal

sugar= int(input("Enter your fasting sugar level: "))

if sugar < 80:
    print("Sugar is low")
elif sugar > 100:
    print("Sugar is high")
else:
    print("Sugar is normal")
    

# [Solution - Exercise 1.i](https://github.com/codebasics/py/blob/master/Basics/Exercise/8_if/8_exercise1_1.py)

# [Solution - Exercise 1.ii](https://github.com/codebasics/py/blob/master/Basics/Exercise/8_if/8_exercise1_2.py)

# [Solution - Exercise 2](https://github.com/codebasics/py/blob/master/Basics/Exercise/8_if/8_exercise2.py)