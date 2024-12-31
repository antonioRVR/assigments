# # Exercise: Array DataStructure

# 1. Let us say your expense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#     3. March - 2600
#     4. April - 2130
#     5. May - 2190

# Create a list to store these monthly expenses and using that find out,

#     1. In Feb, how many dollars you spent extra compare to January?
#     2. Find out your total expense in first quarter (first three months) of the year.
#     3. Find out if you spent exactly 2000 dollars in any month
#     4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
#     5. You returned an item that you bought in a month of April and
#     got a refund of 200$. Make a correction to your monthly expense list
#     based on this

list_of_expenses = [2200, 2350, 2600, 2130, 2190]

extra= list_of_expenses[1] - list_of_expenses[0]
total_expense = sum(list_of_expenses[:3])
spent_2000 = 2000 in list_of_expenses
list_of_expenses.append(1980)
list_of_expenses[3] = list_of_expenses[3] - 200

print("exercise 1")

print(f"Extra spent in Feb compared to Jan: {extra}")
print(f"Total expense in first quarter: {total_expense}")
print(f"Spent exactly 2000 in any month: {spent_2000}")
print(f"List of expenses: {list_of_expenses}")




# 2. You have a list of your favourite marvel super heros.
# ```
# heros=['spider man','thor','hulk','iron man','captain america']
# ```

# Using this find out,

#     1. Length of the list
#     2. Add 'black panther' at the end of this list
#     3. You realize that you need to add 'black panther' after 'hulk',
#        so remove it from the list first and then add it after 'hulk'
#     4. Now you don't like thor and hulk because they get angry easily :)
#        So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#        Do that with one line of code.
#     5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

print("exercise 2")
heros=['spider man','thor','hulk','iron man','captain america']
print(f"Length of the list: {len(heros)}")
print(f"List of heros: {heros}")

heros.append('black panther')

print(f"List of heros: {heros}")

heros.remove('black panther')



heros.insert(3, 'black panther')
print(f"List of heros: {heros}")
heros[1:3] = ['doctor strange']
print(f"List of heros: {heros}")
print(dir(heros))
heros.sort()
print(f"List of heros: {heros}")






# 3. Create a list of all odd numbers between 1 and a max number.
# Max number is something you need to take from a user using input() function

print("exercise 3")
max_number = int(input("Enter a number: "))
list_of_odd_numbers = []

for a in range(1, max_number+1):
  if a % 2 !=0:
    list_of_odd_numbers.append(a)

print(f"List of odd numbers: {list_of_odd_numbers}")
