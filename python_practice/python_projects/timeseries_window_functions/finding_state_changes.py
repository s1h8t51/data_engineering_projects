'''
BNSF tracks trains over time. This is critical for predictive maintenance.

Problem 3: Finding State Changes

Task: You have a list of statuses for a train: ['Idle', 'Idle', 'Moving', 'Moving', 'Stopped', 'Moving']. 
Write a function to count how many times the train changed its status.

Skill: List iteration, indexing (i vs i-1).
'''

# asynchronous batch processing and data coming for every 10 minutes with locomotive_id 

#method 1 
def train_status_change(status):
    # We compare each status with the one following it
    return sum(1 for i in range(len(status) - 1) if status[i] != status[i+1])

def train_status_change(train_id,status):
    l,r =0,1
    change_status = 0
    while r < len(status):
        if status[l] != status[r]:
            change_status += 1
        l = r
        r +=1
    return change_status

train_id =9087
status = ['Idle', 'Idle', 'Moving', 'Moving', 'Stopped', 'Moving']

print(train_status_change(train_id,status))


#method 2

class StatusTracker:
    def __init__(self):
        # We start with None because we haven't seen any data yet
        self.last_status = None
        self.change_count = 0

    def process_new_status(self, current_status):
        # 1. Check if this is the VERY first status we've ever seen
        if self.last_status is None:
            self.last_status = current_status
            return  # No "change" yet, just initializing
        
        # 2. Compare current to the last remembered state
        if current_status != self.last_status:
            self.change_count += 1
            # 3. Update the state to 'remember' it for the next call
            self.last_status = current_status

# --- How it works in a real system ---
tracker = StatusTracker()

# Imagine these arrive 10 minutes apart
tracker.process_new_status("Idle")
tracker.process_new_status("Idle")
tracker.process_new_status("Moving") # Change detected!

print(f"Total changes tracked: {tracker.change_count}") # Output: 1



## further improvements 
## sending data to db attached 
##  pralelly processing by lambda connected to firehouse then to s3 futher to redshift for near real time outcomes 
