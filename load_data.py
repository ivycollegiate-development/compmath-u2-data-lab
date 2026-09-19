"""Starter: load a CSV into Python and look at it.

csv.DictReader turns each row into a dict: column name -> value.
Every value is a STRING. Converting to numbers is your job.
"""
import csv

with open("data/u2_student_performance_data.csv") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print("rows loaded:", len(rows))
print("first row:", rows[0])

# Common gotchas to try in the lesson:
#  - rows[0]["Math Score"] is the string "53", not the number 53
#  - some rows may have blank values
print("type of Math Score:", type(rows[0]["Math Score"]).__name__)
