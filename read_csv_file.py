
with open("data/fighters.csv") as file:
    data = file.readline()
    print(data)

print("--------------reading using for loop----------------------------")
with open("data/fighters.csv") as file:
    for line in file:
        print(line, end  ='')


from csv import reader
with open("data/fighters.csv") as file:
    csv_reader = reader(file)
    print("---------------Print using reader-----")
    for row in csv_reader:
        print(row)

from csv import DictReader
with open("data/fighters.csv") as file:
    csv_reader = DictReader(file)
    print("---------------Print using DictReader-----")
    for row in csv_reader:
        print(row)