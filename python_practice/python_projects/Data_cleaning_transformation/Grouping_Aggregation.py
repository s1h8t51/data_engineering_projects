#Problem 2: Grouping & Aggregation

#Task: Given a list of dictionaries (Locomotive ID and Fuel Consumed), 
# #return a dictionary where the key is the ID and the value is the total fuel consumed.

##Skill: Dictionary manipulation, .get() method, or defaultdict.
from collections import defaultdict

def fuel_consumed(details):
        dit_fuel = defaultdict(str)
        for rec in details:
            Locomotive_ID = rec["id"]
            value = rec["fuel"]
            current_total = dit_fuel.get(Locomotive_ID,0)
            dit_fuel[Locomotive_ID] = value + current_total
        return dit_fuel


details = [
    {"id": "LOC_A", "fuel": 85.5}, 
    {"id": "LOC_B", "fuel": 90.1}, 
    {"id": "LOC_A", "fuel": 84.8}
]
print(fuel_consumed(details))