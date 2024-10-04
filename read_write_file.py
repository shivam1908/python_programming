

#Read the file

from csv import reader, writer
with open("data/fighters.csv", "r") as file:
    data = reader(file)
    with open("data/output/fighters_data.csv", "w") as out_data_file:
        file_writer = writer(out_data_file)
        for record in data:
            print(record)
            file_writer.writerow(record)




