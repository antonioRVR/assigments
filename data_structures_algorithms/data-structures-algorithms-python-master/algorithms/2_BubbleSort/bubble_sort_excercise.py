# ### Bubble Sort Exercise

# Modify [bubble_sort function](https://github.com/codebasics/data-structures-algorithms-python/blob/master/algorithms/2_BubbleSort/bubble_sort.py) 
# such that it can sort following list of transactions happening in an electronic store,
# ```
# elements = [
#         { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
#         { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
#         { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
#         { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
#     ]
# ``` 
# bubble_sort function should take key from a transaction record and sort the list as per that key. For example,
# ```
# bubble_sort(elements, key='transaction_amount')
# ```
# This will sort elements by transaction_amount and your sorted list will look like,
# ```
# elements = [
#         { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
#         { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
#         { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
#         { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
#     ]
# ``` 
# But if you call it like this,
# ```
# bubble_sort(elements, key='name')
# ```
# output will be,
# ```
# elements = [
#         { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
#         { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
#         { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
#         { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
#     ]
# ``` 

# you can use this to sort strings too
def bubble_sort_s(elements, key):
    size = len(elements)

    #every element in elements is a dictionary
    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            #we have to look for the key value of the key in the dictionary
            #so first we look at the element and then we look at the key
            if elements[j][key] > elements[j+1][key]:
                tmp = elements[j]
                elements[j]= elements[j+1]
                elements[j+1] = tmp
                swapped = True

        if not swapped:
            break


elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

bubble_sort_s(elements, key='transaction_amount')
print("order by amount \n ",elements)


bubble_sort_s(elements, key='name')


print("\n order by name \n ",elements) 
