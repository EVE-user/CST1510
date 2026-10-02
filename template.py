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

dataset_name= input("dataset name: ")      
rows_loaded= float(input("rows loaded: "))     
rows_expected= float(input("rows expected: "))   

record_id="survey_2026"
rows_loaded=float("1187")
rows_expected=float("1200")

free=(float(rows_expected) - float(rows_loaded))
percent=(float(rows_loaded)/float(rows_expected))*100 
print("="*34)
print(f"RECORD CHECK     -     {record_id}")
print("="*34)
print(f"Rows_loaded:          {rows_loaded:>10.2f}")
print(f"Rows_expected:        {rows_expected:>10.2f}")
print(f"Percent:              {free:>10.2f}")
print(f"Free:                 {percent:>10.2f} %")
print("="*34)



