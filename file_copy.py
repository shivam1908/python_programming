# Function to copy file data to another file
def copy(copyFrom, copyTo):
    data = ""
    with open(copyFrom, "r") as source:
        data = source.read()
    with open(copyTo,"a") as target:
        target.write(data)

copy("data/sample_data.txt", "data/output/samplecopied1.txt")