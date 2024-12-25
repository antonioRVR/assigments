# ## Exercise: Python Read Write File
# 1. [poem.txt](https://github.com/codebasics/py/blob/master/Basics/Exercise/13_read_write_files/poem.txt) 
# contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in your python program and
#  find out words with maximum occurance.


#1
with open("poem.txt", "r") as f:
    word_stats = {}
    for line in f:
        words=line.split(' ')
        for word in words:
            if word in word_stats:
                word_stats[word]+=1
            else:
                word_stats[word] = 1

print(word_stats)


word_occurances = list(word_stats.values())
max_count = max(word_occurances)
print("Max occurances of any word is:",max_count)

print("Words with max occurances are: ")
for word, count in word_stats.items():
    if count==max_count:
        print(word)



# [Solution](https://github.com/codebasics/py/blob/master/Basics/Exercise/13_read_write_files/exercise_2_stocks.py)

# 2. [stocks.csv](https://github.com/codebasics/py/blob/master/Basics/Exercise/13_read_write_files/stocks.csv) contains stock price,
#  earnings per share and book value. You are writing a stock market application that will process this file and create a new file
# with financial metrics such as pe ratio and price to book ratio. These are calculated as,
# ```
# pe ratio = price / earnings per share
# price to book ratio = price / book value
# ```

with open("stocks.csv", "r") as f, open("output.csv", "w") as out:
    out.write("Company Name,PE Ratio, PB Ratio\n")
    next(f)  # This will skip first line in the file which is a header
    for line in f:
        data = line.split(",")
        company_name = data[0]
        price = float(data[1])
        eps = float(data[2])
        book = float(data[3])
        pe = round(price / eps, 2)
        pb = round(price / book, 2)
        out.write(f"{company_name},{pe},{pb}\n")
    
    

        



# Your input format (stocks.csv) is,

# |Company Name|Price|Earnings Per Share|Book Value|
# |-------|----------|-------|----------|
# |Reliance|1467|66|653|
# |Tata Steel|391|89|572|

# Output.csv should look like this,

# |Company Name|PE Ratio|PB Ratio|
# |-------|----------|-------|
# |Reliance|22.23|2.25|
# |Tata Steel|4.39|0.68|

# [Solution](https://github.com/codebasics/py/blob/master/Basics/Exercise/13_read_write_files/exercise_2_stocks.py)
