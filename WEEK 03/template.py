"""
RECORD CHECK  -  my version
===========================

Name  : Evelyn Franklin
Lane  :  AI      
Date  : 08/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def check_record(rows_expected, rows_loaded):
    """Return the difference and the percentage of the expected and loaded rows."""
    difference = rows_expected - rows_loaded # Calculate the difference between the expected and loaded rows.
    percent = (rows_loaded / rows_expected)*100 # Calculate the percentage of the loaded rows compared to the expected rows.
    return difference,percent

def check_status_of(percent):
    """Return the status based on the percentage."""
    if percent >= 100: # Check if the percentage is greater than or equal to 100.
      return "OVER LIMIT"
    
    elif percent >= 90: # Check if the percentage is greater than or equal to 90.
      return "WARNING"
    
    else:
      return "OK"

def print_report():
    """Print the records of the report until the user types quit in any letter case"""
    over_limit_count = 0 # Start the count of OVER LIMIT at zero.

    while True:
        dataset_name= (input("Enter dataset_name :"))
        if dataset_name == "quit": # End loop when quit is input by the user.
            break

        rows_loaded = float(input("Enter rows_loaded :")) # Convert the input to a float.
        rows_expected = float(input("Enter rows_expected :")) # Convert the input to a float.
        

        difference,percent = check_record(rows_expected, rows_loaded)  # Calculate the difference and percentage of the expected and loaded rows.
        status = check_status_of(percent)  # Determine status of the record based on the percentage.

        # Print the output of the report until user types quit.
        print()
        print("=" * 34)
        print(f"  RECORD CHECK  -  {dataset_name}")
        print("=" * 34)
        print(f"  Rows_loaded:       {rows_loaded:>10.2f}") # Print the number of rows loaded with 2 decimal places and right aligned to 10 spaces.
        print(f"  Rows_expected:     {rows_expected:>10.2f}")
        print(f"  Percent:           {percent:>10.2f}%")
        print(f"  Free:              {difference:>10.2f}")
        print(f"  Status:            {status:>10}")
        print("=" * 34)

        if status == "OVER LIMIT":
            over_limit_count += 1 # Increase the over_limit_count by one.
        
    print(f"Total OVER LIMIT: {over_limit_count}") # Print the total number of records that are "OVER LIMIT".

print_report()




