"""
RECORD CHECK  -  my version
===========================

Name  :EVELYN FRANKLIN
Lane  :  AI 
Date  :29TH SEPTEMBER 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
# Input the record provided by the user.
dataset_name = input("Dataset name: ")      
rows_loaded = float(input("Rows loaded: "))     
rows_expected = float(input("Rows expected: "))   

# Calculate the difference(free) and the percentage of the loaded and the expected rows.
free = (float(rows_expected) - float(rows_loaded))
percent = (float(rows_loaded) / float(rows_expected)) * 100 

# Print the report in a bordered format.
print("=" * 34)
print(f"RECORD CHECK     -    {dataset_name}")
print("=" * 34)
print(f"Rows_loaded:          {rows_loaded:>10.2f}")
print(f"Rows_expected:        {rows_expected:>10.2f}")
print(f"Percent:              {percent:>10.2f}")
print(f"Free:                 {free:>10.2f} %")
print("=" * 34)



