with open('story.txt') as story_object:
  print(story_object.readline())

# Use json.load with an opened file object to read the contents into a Python dictionary.

# Contents of file.json
# { 'userId': 10 }


import json
with open('file.json') as json_file:
  python_dict = json.load(json_file)
  
print(python_dict.get('userId'))
# Prints 10

# w -- to rewrite entire file 
# a-- to append new value to file with out chaing existing data
#readlines() -- return list of strings
# read() method of the file object to return the entire file content as a Python string
with open('shopping.txt', 'a') as shop:
  shop.write('Tomatoes, cucumbers, celery\n')
  shop.readlines()
  shop.read()


#to read and write tabular data in CSV format
# DictWriter which operates like a regular writer but maps a dictionary onto output rows
# An example of csv.DictWriter
import csv

with open('companies.csv', 'w') as csvfile:
  fieldnames = ['name', 'type']
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()
  writer.writerow({'name': 'Codecademy', 'type': 'Learning'})
  writer.writerow({'name': 'Google', 'type': 'Search'})

"""
After running the above code, companies.csv will contain the following information:

name,type
Codecademy,Learning
Google,Search
"""