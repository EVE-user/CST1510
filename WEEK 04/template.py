"""
RECORD CHECK  -  my version
===========================

Name  : Evelyn Franklin
Lane  :  AI 
Date  : 16/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def check_record (record):
    """Return the difference and the percentage of the expected and loaded rows."""
    difference = record['rows_expected'] - record['rows_loaded'] # Calculate the difference between the expected and loaded rows.
    percent = (record['rows_loaded'] / record['rows_expected']) * 100 # Calculate the percentage of the loaded rows compared to the expected rows.
    return difference, percent

def check_status_of (percent):
    """Return the status based on the percent."""
    if percent >= 100: # Check if the percentage is greater than or equal to 100.
      return "OVER LIMIT"
    
    elif percent >= 90: # Check if the percentage is greater than or equal to 90.
      return "WARNING"
    
    else:
      return "OK"
  
def print_report(record, difference, percent, status):
    """Print the bordered report of the records."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -    {record['dataset_name']}")
    print("=" * 34)
    print(f"  Rows_loaded:       {record['rows_loaded']:>10.2f}") # Print the number of rows loaded with two decimal places and right-aligned with a width of 10.
    print(f"  Rows_expected:     {record['rows_expected']:>10.2f}")
    print(f"  Percent:           {percent:>10.2f}%")
    print(f"  Free:              {difference:>10.2f}")
    print(f"  Status:            {status:>10}")
    print("=" * 34)
    
        
def load_records(path):
    """Read the  file and return a list of record dictionaries."""
    records = [] # Create an empty list to store the records.
    
    # Open the file using the given path.
    with open(path) as f:
         for line in f: # Loop over each line in the file.
             line = line.strip() # Remove the white space from the beginning to the end of the line.
             dataset_name, rows_loaded, rows_expected = line.split(",") # Split the line at each comma into three lines.

            # Create a record dictionary.
             record = {
                   "dataset_name": dataset_name,
                   "rows_loaded": float(rows_loaded),
                   "rows_expected": float(rows_expected)

            }
         
             records.append(record) # Add the record dictionary to the list.

    return records



# Try to load the records from the records_file.txt.
try:
    records = load_records("records_file.txt")

# Handle the FileNotFoundError.
except FileNotFoundError:
    print("Error:records_file.txt was not found.")
    records = [] # Create an empty list to store the records.


over_limit_count = 0 # Start the count of OVER LIMIT by zero.

# Open the output_file.txt and write the results.
with open ("output_file.txt","w") as f:
   
    for record in records:        
        difference,percent = check_record(record) # Calculate the difference and percentage of the record.
        status = check_status_of(percent)  # Determine the status of the records based on the percentage.
        f.write(f"{record['dataset_name']},{status}\n") # Write the dataset name and the status to the output file.

        print_report(record,difference,percent,status) # Print a bordered report of the record.

        if status == "OVER LIMIT": # Check whether the status is OVER LIMIT.
            over_limit_count += 1  # Increase the count by one.

print(f"\nTotal OVER LIMIT: {over_limit_count}") # Print the total number of records that are OVER LIMIT.
print("Results saved to output_file.txt")
         

