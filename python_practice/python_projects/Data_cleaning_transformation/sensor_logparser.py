#Task: Given a list of strings representing 
#logs: "2023-10-01 12:00:00, LOC_123, TEMP, 85.5", 
#write a function to convert these into a list of dictionaries. 
#Handle cases where the temperature might be missing or corrupted (e.g., "NULL" or "ERROR").

#Skill: String splitting, Type casting, Error handling (try-except).

def list_of_dict(logs):
    log_dict,final_dict={},[]
    parts=[]
    for i in logs:
        parts = [p.strip() for p in i.split(',')]
        if len(parts)<4:
            continue
        try:
            temp_value = float(parts[3])
        except (ValueError, TypeError):
            # Handle "NULL", "ERROR", or empty strings by setting to None
            temp_value = None

        log_dict = {
            "timestamp": parts[0],
            "location_id": parts[1],
            "type": parts[2],
            "temperature": temp_value
        }
        
        final_dict.append(log_dict)
        
    return final_dict

logs=[ "2023-10-01 12:00:00, LOC_123, TEMP, 85.5","2023-10-01 12:00:00, LOC_123, TEMP, 85.5"]

print(list_of_dict(logs))

