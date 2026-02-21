import logging
# logging.warning("Remain calm!")

# log levels - debug ,info,warning,error,critical
# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")

#debug() and info() messages didn’t get logged.


## basic logging configuration and adjust the log level
# logging.basicConfig(level=logging.DEBUG)
# logging.debug("This will get logged.")

# # log levels values  - debug --10 ,info-- 20,warning--30,error--40,critical--50
# logging.basicConfig(level=20)
# logging.info("This will get logged.")

# logging.basicConfig(format="%(levelname)s:%(name)s:%(message)s")
# logging.warning("Hello, Warning!")

# # {: Modern, clean. Use this for your new projects.-- wirte place holders
# logging.basicConfig(format="{levelname}:{name}:{message}", style="{")
# logging.warning("Hello, Warning! 2 ")

#timestamp

# logging.basicConfig(
#     format="{asctime} - {levelname} - {message}",
#     style="{",
#     datefmt="%Y-%m-%d %H:%M",
# )
# logging.error("Something went wrong!")

#Logging to a File


# logging.basicConfig(
#     filename="app.log",
#     encoding="utf-8",
#     filemode="a",
#     format="{asctime} - {levelname} - {message}",
#     style="{",
#     datefmt="%Y-%m-%d %H:%M",
#     level = 10
# )
# # name ="samara" #self docuemneting expression 
# # logging.debug(f"{name =}")
# # logging.warning("Save me!")

# donuts =10
# guests = 2
# try: 
#     do_per_guests = donuts/guests 
# except ZeroDivisionError:
#     logging.error("donutcalculationerror",exc_info =True)
# finally:
#     print("your project is sucessfull")

# exc_info -- exceptioninformation 

'''
The Task: The "Fault-Tolerant CSV to JSON Pipeline"

Scenario: You are building a pipeline that reads a "Sensor Data" CSV, cleans it, 
and prepares it for an AI Model. You need to handle different failure modes using your new hierarchy.

Requirements:

Define the Hierarchy:
PipelineError (Base)
ExtractionError (If the file is missing)
TransformError (If data values are "junk")

The Logic:
Create a class DataProcessor.
Method 1 (extract): Try to open a file. If it doesn't exist, raise ExtractionError.
Method 2 (transform): Loop through a list of numbers. If a value is None or a string, raise TransformError.

The Handling (The "Smart" part):
If an ExtractionError happens, log a Critical error and stop.
If a TransformError happens, Log a Warning, skip that specific row, and keep going.
'''


import logging

# --- 1. Define the Hierarchy ---
class PipelineError(Exception): """Base"""
class ExtractionError(PipelineError): """File Issues"""
class TransformError(PipelineError): """Data Issues"""

# --- 2. The Logic (Class Based) ---
class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.logger = logging.getLogger(__name__)

    def extract(self):
        try:
            with open(self.file_path, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            # We catch the system error and raise our CUSTOM error
            raise ExtractionError(f"Critical: {self.file_path} is missing.")

    def transform(self, data_list):
        cleaned_data = []
        for i in data_list:
            try:
                if i is None or isinstance(i, str):
                    raise TransformError(f"Junk data found: {i}")
                cleaned_data.append(i * 10) # Processed value
            except TransformError as e:
                # This 'Smart' block logs the warning and continues the loop
                self.logger.warning(f"Skipping row: {e}")
                continue 
        return cleaned_data

# --- 3. The Handler (The Execution) ---
def run_pipeline():
    # Configure logging once
    logging.basicConfig(level=logging.DEBUG, format="{levelname}: {message}", style="{")
    
    processor = DataProcessor("sensor_data.csv")
    
    # Scenario A: Extraction (Critical)
    try:
        raw_data = processor.extract()
    except ExtractionError as e:
        logging.critical(f"PIPELINE STOPPED: {e}")
        return # Kill the function

    # Scenario B: Transformation (Resilient)
    dirty_data = [1, 5, None, 10, "bad_sensor", 20]
    final_data = processor.transform(dirty_data)
    print(f"Final processed data: {final_data}")

run_pipeline()



