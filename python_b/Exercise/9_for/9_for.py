# ## Exercise: Python for loop
# 1. After flipping a coin 10 times you got this result,
# ```
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# ```
# Using for loop figure out how many times you got heads

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

count = 0

for item in result:
    if item == "heads":
        count += 1

print(count)

# 2. Print square of all numbers between 1 to 10 except even numbers

for i in range(1, 11):
    if i % 2 !=0:
        print(i**2)

# 3. Your monthly expense list (from Jan to May) looks like this,
# ```
# expense_list = [2340, 2500, 2100, 3100, 2980]
# ```
# Write a program that asks you to enter an expense amount and program
# should tell you in which month that expense occurred. If expense is not
# found then it should print that as well.

expense_list = [2340, 2500, 2100, 3100, 2980]
month_list = ["January", "February", "March", "April", "May"]

number= int(input("Enter an expense amount: "))

found= False
for i in range (len(expense_list)):
    if number == expense_list[i]:
        print(f'You spent {number} in {month_list[i]}')
        found = True  
        break 
  
if not found:
    print(f'You didn\'t spend {number} in any month')



# 4. Lets say you are running a 5 km race. Write a program that,
#    1. Upon completing each 1 km asks you "are you tired?"
#    2. If you reply "yes" then it should break and print "you didn't finish the race"
#    3. If you reply "no" then it should continue and ask "are you tired" on every km
#    4. If you finish all 5 km then it should print congratulations message

for i in range(5):
    input("Are you tired?")
    if input == 'yes':
        print("You didn't finish the race")
    elif input == 'no':
        continue  
    if i == 4:
        print("Congratulations, you finished the race")



# 5. Write a program that prints following shape
# ```
# *
# **
# ***
# ****
# *****
# ```

s=''

for i in range(1,6):
    s += '*'
    print(s)


# [Solution](https://github.com/codebasics/py/blob/master/Basics/Exercise/9_for/9_for_exercise.py)