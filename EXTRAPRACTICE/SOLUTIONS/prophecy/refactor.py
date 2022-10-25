"""
Add students and houses to database after applying updated schema
"""

from cs50 import SQL
import csv

HOUSES = [
    {"house": "Slytherin", "head": "Severus Snape"},
    {"house": "Ravenclaw", "head": "Filius Flitwick"},
    {"house": "Gryffindor", "head": "Minerva McGonagall"},
    {"house": "Hufflepuff", "head": "Pomona Sprout"},
]

# Open connection to database
db = SQL("sqlite:///roster.db")

# Add houses
for house in HOUSES:
    db.execute("INSERT INTO houses (house, head) VALUES (?, ?)", house["house"], house["head"])

# Add students
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        
        # Add student to table
        student_id = db.execute("INSERT INTO students (student_name) VALUES (?);", row["student_name"])

        # Get house ID
        house_id = db.execute("SELECT id FROM houses WHERE house = ?", row["house"])[0]['id']

        # Add house assignment
        db.execute("INSERT INTO assignments (student_id, house_id) VALUES (?, ?);", student_id, house_id)
        print(f"Added {row['student_name']} to database.")
