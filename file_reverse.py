# function to reverse the content of file into new file

def rev_data(source, target):
    with open(source,"r") as source_file:
        data = source_file.read()
    with open(target,"w") as target_file:
        target_file.write(data[::-1])

rev_data("data/sample_data.txt","data/output/reverse_data.txt")