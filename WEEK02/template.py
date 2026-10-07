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


dataset_name="survey_2026"    
rows_loaded=float(1187)   
rows_expected=float(1200)   

dataset_name = input("Dataset Name: ")    
rows_loaded = float(input("Rows Loaded: "))    
rows_expected = float(input("Rows Expected: "))  

difference = rows_expected - rows_loaded  
percent=(rows_loaded/rows_expected)*100
if percent >= 100:
    status="OVER LIMIT"
elif percent >= 90:
    status="WARNING"
else:
    status="OK"
print("=" * 34)
print(f"  RECORD CHECK  -    {dataset_name}")
print("=" * 34)
print(f"  Rows_loaded:       {rows_loaded:>10.2f}")
print(f"  Rows_expected:     {rows_expected:>10.2f}")
print(f"  Percent:           {percent:>10.2f}%")
print(f"  Free:              {rows_expected-rows_loaded:>10.2f}")
print(f"  Status:            {status:>10}")
print("=" * 34)

