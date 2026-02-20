data = [
    "7788, Engine, 5000",
    "9912, Brake, 1200",
    "7788, Wheel, 800",
    "9912, Engine, ERROR",
    " , Light, 50",
    "7788, Paint, 300"
]

#You receive a list of strings representing locomotive repairs: "LOCO_ID, REPAIR_TYPE, COST".
#Calculate the total cost for each LOCO_ID.
#Identify which LOCO_ID had the most expensive single repair.
#Return a dictionary with these results.
#Constraint: If the cost is not a valid number, skip that line. If the ID is empty, skip that line.

def locomotive_cost(data):
    company={}
    current_value=0
    for i in data:
        parts = i.split(",")
        if  parts[2] != ' ERROR' :
            print(parts[2])
            current_value = int(parts[2])
            if parts[0] in company:
                company[parts[0]] = company.get(int(company[parts[0]]),0)+current_value
            else:
                company[parts[0]] = current_value
    return company

print(locomotive_cost(data))

def locomotive_cost(data):
    # Data structures to store our results
    total_costs = {}       # To track sums
    max_repair_val = -1    # To track the highest single repair cost
    max_repair_id = None   # To track WHO had that highest repair
    
    for record in data:
        # 1. Clean and Split
        parts = [p.strip() for p in record.split(",")]
        
        # Ensure we have enough columns to avoid IndexError
        if len(parts) < 3:
            continue
            
        loco_id = parts[0]
        cost_str = parts[2]
        
        # 2. Constraint: Skip if ID is empty
        if not loco_id:
            continue
            
        # 3. Constraint: Validate if cost is a valid number
        try:
            current_cost = float(cost_str)
        except ValueError:
            # This handles "ERROR", "NULL", or any non-numeric string
            continue
            
        # 4. Aggregation: Summing total cost per ID
        if loco_id in total_costs:
            total_costs[loco_id] += current_cost
        else:
            total_costs[loco_id] = current_cost
            
        # 5. Requirement: Track the single most expensive repair
        if current_cost > max_repair_val:
            max_repair_val = current_cost
            max_repair_id = loco_id
            
    # Return results in the requested dictionary format
    return {
        "totals_per_id": total_costs,
        "most_expensive_repair_id": max_repair_id,
        "max_repair_cost": max_repair_val
    }

# Test Data
data = [
    "7788, Engine, 5000",
    "9912, Brake, 1200",
    "7788, Wheel, 800",
    "9912, Engine, ERROR",
    " , Light, 50",
    "7788, Paint, 300"
]

print(locomotive_cost(data))


        



