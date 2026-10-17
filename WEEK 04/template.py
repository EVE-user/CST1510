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

def check_record(record):
    """Return the difference and percent of the rows_expected and the rows_loaded"""
    difference =record['rows_expected'] - record['rows_loaded']
    percent=(record['rows_loaded']/record['rows_expected'])*100
    return difference,percent

def check_status_of(percent):
    """Return the status based on the percent"""
    if percent >= 100:
      return "OVER LIMIT"
    elif percent >= 90:
      return "WARNING"
    else:
      return "OK"
  
def print_report(record,difference,percent,status):
    """Print the output of the reports"""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -    {record['dataset_name']}")
    print("=" * 34)
    print(f"  Rows_loaded:       {record['rows_loaded']:>10.2f}")
    print(f"  Rows_expected:     {record['rows_expected']:>10.2f}")
    print(f"  Percent:           {percent:>10.2f}%")
    print(f"  Free:              {difference:>10.2f}")
    print(f"  Status:            {status:>10}")
    print("=" * 34)
    
        
def load_records(path):
    """Open the  file and return a list of dictionaries"""
    records=[]
    
    #open the file using the given path.
    with open(path) as f:
         for line in f:
             line =line.strip()
             dataset_name,rows_loaded,rows_expected=line.split(",")

             record={
                   "dataset_name":dataset_name,
                   "rows_loaded":float(rows_loaded),
                   "rows_expected":float(rows_expected)

            }
         
             records.append(record)

    return records



#try to load the records from the file.
try:
    records=load_records("records_file.txt")

except FileNotFoundError:
    print("Error:records_file.txt was not found.")
    records=[]

#open the output file and write the results.
over_count=0
with open ("output_file.txt","w") as f:
    for record in records:
        
        difference,percent=check_record(record)
        status=check_status_of(percent)
        f.write(f"{record['dataset_name']},{status}\n")
        print_report(record,difference,percent,status)

        if status == "OVER LIMIT":
            over_count +=1

print(f"\nTotal OVER LIMIT:{over_count}")
print("Results saved to output_file.txt")
         

