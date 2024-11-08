from csv import reader,writer

with open("../data/fighters.csv",'r') as file:
    csv_reader = reader(file)
    fighters = [[field.upper() for field in fighter ] for fighter in csv_reader]
    for fighter in fighters:
        print(fighter)

with open("../data/output/upper_fighters_data.csv",'w') as file:
    csv_writer = writer(file)
    for fighter in fighters:
        csv_writer.writerow(fighter)