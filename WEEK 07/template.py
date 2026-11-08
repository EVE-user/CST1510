"""
RECORD CHECK  -  my version
===========================

Name  :Evelyn Franklin
Lane  :  AI 
Date  :05/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
def parse_line(raw_line):
    """Clean and parse one raw, messy line into a dict."""
    line = raw_line.strip() # Remove the whitespace from the beginning and end of the line.
    dataset_part, rest = line.split(",",1) # Split the string at the first comma only.
    dataset_name = dataset_part.strip().lower() # Remove the whitespace and convert text to lower case.

    # Create a dictionary to store the key-value pairs.
    records = {}

    for piece in rest.split(","): # Loop through the rest of the line and split it at each comma.
        key, value = piece.split("=") # Split the line at each '=' into key and value.

        # Remove the whitespace around key and convert to lower case.
        records[key.strip().lower()] = float(value.strip())# Remove unnecessary space around the value and convert it to float.


    return  {"dataset_name": dataset_name,
             "rating":records["rating"], 
             "age":records["age"]
                 } # Return the dictionary.

def status_of(rating, age):
    """Determine the status of the record based on its values."""
    percent = (rating / age) * 100  # Calculate the percent of the rating to the age.
    
    if percent > 100: # Check if the percentage is at least 100.
        return "OVER LIMIT"
    
    elif percent > 90: # Check if the percentgae is at least 90.
        return "WARNING"

    else:
        return "OK"

total = 0 # Start count for total records at zero.
flagged = 0 # Start count for flagged status at zero.

with open("my_records.txt") as f: # Open my_records.txt.

    # Loop through my_records.txt and try to read the lines into a dict.
    for raw_line in f:    
        try:
            record = parse_line(raw_line)
            rating = record["rating"]
            age = record["age"]

            status = status_of(rating, age)
            print(record, status)

            total += 1 # Add count of total by one.
            if status != "OK": # Check if the status is not "OK".
                flagged += 1 # Add count of flagged by one.

        # Handle ValuError by printing the message.
        except ValueError:
            print("Could not parse:", raw_line.strip()) # Remove the whitespace surrounding the raw_line.

print("TOTAL RECORDS:", total) # Print the count of the total records.
print("FLAGGED RECORDS:", flagged) # Print the count of flagged records.

