# generators are lazy iteros  donot store  
# reading large files  and data streams

## finding no of rows
#
import csv

## list read so may a memory error so do not run 
# def csv_reader(file_name):
#     file = open(file_name)
#     result = file.read().split("\n")
#     return result

def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row

# genertaor expresiion /comprehension 
file_name = 0
csv_gen = (x for x in open(file_name))

#generating infinite sequence 

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_sequence()
# even though infinite sequence because of generators we can control the out put 
print(next(gen))
print(next(gen))


## detecting palindromes. generate continous palindrom 
## in practice iter tools handel the efficient infinote sequence 
#undersatnding generators 
## list comprehensions 

## here we can observe how same lines of code for list and generators occupy different meemory 
import sys
nums_squared_lc = [i ** 2 for i in range(10000)]
print(sys.getsizeof(nums_squared_lc)) 
# 85176

nums_squared_gc = (i ** 2 for i in range(10000))
print(sys.getsizeof(nums_squared_gc))
# 200

#list comprehensions return full lists, while generator expressions return generator

#StopIteration is a natural exception that’s raised to signal the end of an iterator

letters = ["a", "b", "c", "y"]
it = iter(letters)
while True:
    try:
        letter = next(it)
    except StopIteration:
        break
    print(letter)

# yeild sends data out for push  data , eroors or termination signals we use .send(), .throw(),.close()
# examples 

## .send() value back to generator 
def control_tower():
    print("Tower is active.")
    while True:
        # The generator pauses here and "yields" None.
        # When .send() is called, the result is assigned to 'message'
        message = yield 
        if message == "LAND":
            print("Clearing runway for landing...")
        else:
            print(f"Received signal: {message}")

generator = control_tower()
next(generator)          # Prime the generator
generator.send("HELLO")  # Received signal: HELLO
generator.send("LAND")   # Clearing runway for landing...

# throw for signelling

def data_stream():
    try:
        while True:
            yield "Normal Data"
    except ValueError:
        print("Generator caught a ValueError! Cleaning up...")
    finally:
        print("Closing stream.")

# gen = data_stream()
# print(next(gen))
# gen.throw(ValueError)  # This forces the ValueError inside the 'try' block
## close() -- stops geenrator bu raising generator exit

def log_generator():
    try:
        while True:
            yield "Logging..."
    finally:
        # This runs when .close() is called
        print("Generator is shutting down safely.")

# logger = log_generator()
# next(logger)
# logger.close()  # Generator is shutting down safely.
# Calling next(logger) now would raise StopIteration


## creating datapipelines with generators 

file_name = "/workspaces/data_engineering_projects/python_practice/python_projects/python_basics/techcrunch.csv"
lines = (line for line in open(file_name))
list_line = (s.rstrip().split(",") for s in lines)
# store collumn as list 
cols = next(list_line)
# happens only once as it is not in loop or none calling and headers attached 
company_dicts = (dict(zip(cols, data)) for data in list_line)
# list_line is triggered here and new row is take 

funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)
## funding need company_dictcs to check column  so it triggers that 
total_series_a = sum(funding)
#first trigger starts here 
print(f"Total series A fundraising: ${total_series_a}")



'''
The Task: "Clean Tech" ETL Pipeline

Goal: Create a script that reads techcrunch.csv and generates a clean summary of companies that raised more than $5,000,000, 
saving their names and the exact amount to a new file.

1. Extract (E)

Create a generator that reads the file line-by-line and yields dictionaries (using the cols and zip logic we discussed).

Bonus: Use a try...except block inside the generator to handle rows that might be broken or have missing columns.


2. Transform (T)

Create a second generator that "consumes" the first one.

Filter for companies with raisedAmt > 5000000.

Convert the company names to UPPERCASE.

Handle the empty numEmps values by assigning a default of 0.

3. Load (L)

Instead of using sum(), use a for loop to iterate through your final generator and write each "clean" row into a new text file or print a formatted report.
'''

file_name = "/workspaces/data_engineering_projects/python_practice/python_projects/python_basics/techcrunch.csv"
def clean_tech(file_name):
    lines = (line for line in open(file_name))
    gen_rows = (s.strip().split(",") for s in lines)
    cols = next(gen_rows)
    for data in gen_rows:
        data_dict = dict(zip(cols,data))
        try:
            if int(data_dict["raisedAmt"]) > 5000000:
                data_dict["company"] = data_dict["company"].upper()
                if not data_dict["numEmps"]:
                    data_dict["numEmps"] = 0 
                yield data_dict
        except  ValueError :
            print("missing data")
            continue


with open("new_text_file.txt","w") as f :
    try:
        for i in clean_tech(file_name):
            f.write(f"written by {i["company"]} raised amount {i["raisedAmt"]} \n ")
    finally:
        print("new file created")


    

