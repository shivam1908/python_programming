from csv import DictWriter , reader

with open("../data/fighters.csv",'r') as file:
    csv_reader = reader(file)
    field_names = list(next(csv_reader))
    fighters = [[field.upper() for field in fighter ] for fighter in csv_reader]
    for fighter in fighters:
        print(fighter)

with open("../data/output/csv_fighters_using_dictwriter.csv",'w') as file:
     headers = field_names
     csv_writer = DictWriter(file,fieldnames= headers)
     csv_writer.writeheader()
     for fighter in fighters:
         csv_writer.writerow({
             "Name" : fighter[0],
             "Country" : fighter[1],
             "Height (in cm)" : fighter[2]
         })
