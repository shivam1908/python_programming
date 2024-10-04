print("--------------reading using read()----------------------------")

with open("data/fighters.csv") as file:
    print(file.read())



print("--------------reading using readline()----------------------------")

with open("data/fighters.csv") as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())

print("--------------reading using readlines()----------------------------")

with open("data/fighters.csv") as file:
    print(file.readlines())



print("--------------reading using for loop----------------------------")
with open("data/fighters.csv") as file:
    for line in file:
        print(line, end  ='')

print("--------------reading using for loop 2 ----------------------------")
with open("data/fighters.csv") as file:
    while True:
        line = file.readline()
        if  not line :
            break
        print(line)



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