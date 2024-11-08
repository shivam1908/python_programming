from csv import writer
with open("../data/output/filewriter.csv", "w") as f_writer:
    csv_writer = writer(f_writer)
    csv_writer.writerow(["Name","Profession","Age"])
    csv_writer.writerow(["Shivam","Data Engineer","28"])
    csv_writer.writerow(["Sourav","DevOps Engineer","26"])
