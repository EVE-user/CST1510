"""
RECORD CHECK  -  my version
===========================

Name  : Evelyn Franklin Rwezimula.
Lane  :  AI 
Date  : 23/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
# Create a class to store the records.
class Record:
    def __init__ (self, dataset_name, rows_loaded, rows_expected):
        """Create a record with dataset_name, loaded and expected rows."""
        self.dataset_name = dataset_name
        self.rows_loaded = rows_loaded
        self.rows_expected = rows_expected


    def percent(self):
        """Return the loaded and expected rows."""
        return(self.rows_loaded / self.rows_expected)*100 # Calculate the percentage of the loaded rows to the expected rows.

    def difference(self):
        """Return the difference of the expected and loaded rows."""
        return(self.rows_expected - self.rows_loaded) # Calculate difference between the expected rows and the loaded rows.
    
    def status(self):
        """Return the status based on the percentage of the expected and loaded rows."""
        x = self.percent() # Assign x as the percentage.
        if x >= 100: # Compare the percentage to the given limit and return the status.
         return "OVER LIMIT"
        
        elif x >= 90:
         return "WARNING"
        
        else:
         return "OK"


    def print_report(self, difference, percent, status):
           """Print the record in a bordered report."""
           print()
           print("=" * 34)
           print(f"  RECORD CHECK  -  {self.dataset_name}")
           print("=" * 34)
           print()
           print(f"  Rows_loaded:       {self.rows_loaded:>10.2f}")
           print(f"  Rows_expected:     {self.rows_expected:>10.2f}")
           print(f"  Percent:           {percent:>10.2f}%")
           print(f"  Free:              {difference:>10.2f}")
           print(f"  Status:            {status:>10}")
           print("=" * 34)

def load_records(path):
    """Load the records from the given file."""
    records = [] # Create an empty list to store the records.

    with open (path) as f: # Open the path of the file given.
        for line in f:# Loop through each line in the file.
             line = line.strip() # Remove the white spaces at the beginning and end of the line.
             dataset_name,rows_loaded,rows_expected = line.split(",")
             records.append(Record(dataset_name, float(rows_loaded), float(rows_expected)))
    return records

# Load records from the given file.    
records = load_records("records_set.txt")

over_limit_count = 0 # Start count of OVER LIMIT at zero.


# Loop through each record and print the bordered report.
for record in records:
    difference = record.difference()
    percent = record.percent()
    status = record.status()

    record.print_report(difference, percent, status) # Print the difference, percentage and status to the report.

    if status == "OVER LIMIT":
        over_limit_count += 1 # Increase the count by one.

print(f"\nTotal OVER LIMIT : {over_limit_count}")
       