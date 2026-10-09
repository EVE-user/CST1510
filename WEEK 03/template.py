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
dataset_name="survey_2026"    
rows_loaded=float(1187)   
rows_expected=float(1200)   

def check(rows_expected,rows_loaded):
    """Returns the difference and percent of the rows_expected and the rows_loaded"""
    difference = rows_expected - rows_loaded  
    percent=(rows_loaded/rows_expected)*100
    return difference,percent

def check_status_of(percent):
    """Returns the status based on the percent"""
    if percent >= 100:
      return "OVER LIMIT"
    elif percent >= 90:
      return "WARNING"
    else:
      return "OK"

def print_report():
    """Provides the output of the report and keeps providing output until quit is typed"""
    over_count = 0

    while True:
        rows_loaded=(input("Enter rows_loaded:"))
        if rows_loaded.lower() == "quit":
            break

        rows_expected = float(input("Enter rows_expected:"))
        dataset_name = input("Enter data_set name:")
        rows_loaded = float(rows_loaded)

        difference,percent=check(rows_expected,rows_loaded)
        status=check_status_of(percent)

    
        print()
        print("=" * 34)
        print(f"  RECORD CHECK  -  {dataset_name}")
        print("=" * 34)
        print(f"  Rows_loaded:       {rows_loaded:>10.2f}")
        print(f"  Rows_expected:     {rows_expected:>10.2f}")
        print(f"  Percent:           {percent:>10.2f}%")
        print(f"  Free:              {difference:>10.2f}")
        print(f"  Status:            {status:>10}")
        print("=" * 34)

        if status == "OVER LIMIT":
                    over_count += 1
        
    print(f"Total OVER LIMIT: {over_count}")

print_report()




