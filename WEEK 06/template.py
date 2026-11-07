"""
RECORD CHECK  -  my version
===========================

Name  : Evelyn Franklin.
Lane  :  AI 
Date  : 29/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("my_record.csv") # Load dataset from csv file. 

df["percent"] = (df["rows_loaded"] / df["rows_expected"] * 100).round(1) # Calculate the percentage of the loaded rows to the rows expected.
print(df)

df["status"] = df["percent"]. apply(lambda p: # Apply lambda to the percentage to determine the status basing on the percentage.
                                    "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK") # Create a new status column based on the percentage levels.
print(df)

print(df[df["status"] != "OK"]) # Filter and display the rows whose status not "OK".

print(df.groupby("status")["dataset"].count()) # Count the number of datasets within each status.

df.to_csv("status_count.csv", index = False) # Save the dataframe to a new csv file without the index column.

df.groupby("status")["dataset"].count().plot(kind="bar", # Plot a bar chart of status count.
                                             color="yellow")


plt.title("STATUS COUNT")
plt.xlabel("Status")
plt.ylabel("Number of Datasets")
plt.savefig("status_counts.png") # Save the bar chart to a png format.
plt.show()
