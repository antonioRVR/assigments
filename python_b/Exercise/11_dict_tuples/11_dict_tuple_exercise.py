# ## Exercise: Python Dict and Tuples

# 1. We have following information on countries and their population (population is in crores),

#     |Country|Population|
#     |-------|----------|
#     |China|143|
#     |India|136|
#     |USA|32|
#     |Pakistan|21|
#     1. Using above create a dictionary of countries and its population

countries = { "China": 143, "India": 136, "USA": 32, "Pakistan": 21 }

#     2. Write a program that asks user for three type of inputs,
#         1. print: if user enter print then it should print all countries with their population in this format,
#             ```
#             china==>143
#             india==>136
#             usa==>32
#             pakistan==>21
#             ```
#         1. add: if user input add then it should further ask for a country name to add. If country already exist in our 
#               dataset then it should print that it exist and do nothing. If it doesn't then it asks for population and 
#               add that new country/population in our dictionary and print it
#         2. remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary 
#           then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!
#         3. query: on this again ask user for which country he or she wants to query. When user inputs that country it will 
#             print population of that country.

exit = False
while exit == False:

    instructions=input("what do you want to do (print, add, remove, query): ")

    if instructions == 'print':
    
        for key, value in countries.items():
            print(f'{key} ==> {value}')

    if instructions == "add":
        new_country = input("Enter country name: ")
        if new_country in countries.keys():
            print("Country already exists")
        else:
            new_population = int(input("Enter population: "))
            countries[new_country] = new_population
            print(f'{new_country} ==> {new_population}')

    if instructions == "remove":
        remove_country = input("Enter country name to remove: ")
        if remove_country in countries.keys():
            countries.pop(remove_country)
            for key, value in countries.items():
                print(f'{key} ==> {value}')
        else:
            print("Country doesn't exist!")

    if instructions == "query":
        query_country = input("Enter country name to query: ")
        if query_country in countries.keys():
            print(f'{query_country} ==> {countries[query_country]}')
        else:
            print("Country doesn't exist!")

    exit = input("Do you want to exit? (yes/no): ")

    if exit == "yes":
        exit = True
        print("Goodbye!")
    elif exit == "no":
        exit = False
    else:
        print("Invalid input. We will continue.")

        
        


# [Solution](https://github.com/codebasics/py/blob/master/Basics/Exercise/11_dict_tuples/11_dict_exercise_1_country_population.py)

# 2. You are given following list of stocks and their prices in last 3 days,

#     |Stock|Prices|
#     |-------|----------|
#     |info|[600,630,620]|
#     |ril|[1430,1490,1567]|
#     |mtl|[234,180,160]|

#     1. Write a program that asks user for operation. Value of operations could be,
#         1. print: When user enters print it should print following,
#             ```
#             info ==> [600, 630, 620] ==> avg:  616.67
#             ril ==> [1430, 1490, 1567] ==> avg:  1495.67
#             mtl ==> [234, 180, 160] ==> avg:  191.33
#             ```
#         2. add: When user enters 'add', it asks for stock ticker and price. If stock already exist in your list (like info, ril etc) then it will append the price to the list. Otherwise it will create new entry in your dictionary. For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.

# [Solution](https://github.com/codebasics/py/blob/master/Basics/Exercise/11_dict_tuples/11_dict_exercise_2_stocks.py)

# 3. Write circle_calc() function that takes radius of a circle as an input from user and then it calculates and returns area, circumference and diameter. You should get these values in your main program by calling circle_calc function and then print them

# [Solution](https://github.com/codebasics/py/blob/master/Basics/Exercise/11_dict_tuples/11_dict_exercise_3_circle.py)