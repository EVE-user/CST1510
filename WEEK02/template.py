"""
RECORD CHECK  -  my version
===========================

Name  :EVELYN FRANKLIN RWEZIMULA
Lane  :AI AND DATA SCIENCE
Date  :01/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# Input the information entered by the user.
dataset_name = input("Dataset Name: ")    
rows_loaded = float(input("Rows Loaded: ")) # Convert input to float.
rows_expected = float(input("Rows Expected: "))  

difference = rows_expected - rows_loaded   # Calculate the difference of the loaded and expected rows.
percent = (rows_loaded / rows_expected) * 100  # Calculate the percentage of the loaded rows to the expected rows.
if percent >= 100: # Compare the percentage to the limit and provide status.
    status = "OVER LIMIT"

elif percent >= 90:
    status = "WARNING"

else:
    status = "OK"

# Print the record in a bordered report.
print("=" * 34)
print(f"  RECORD CHECK  -    {dataset_name}")
print("=" * 34)
print(f"  Rows_loaded:       {rows_loaded:>10.2f}")
print(f"  Rows_expected:     {rows_expected:>10.2f}")
print(f"  Percent:           {percent:>10.2f}%")
print(f"  Free:              {difference:>10.2f}")
print(f"  Status:            {status:>10}")
print("=" * 34)

