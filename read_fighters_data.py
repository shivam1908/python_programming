
from csv import DictReader
with open("data/fighters.csv","r") as csv_file:
    csv_reader = DictReader(csv_file)
    for row in csv_reader:
        print(f"{row['Name']} | {row['Country']} | {row['Height (in cm)']}")



