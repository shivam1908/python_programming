# this program is to apppend the content to already existing file

with open("data\\output\\sample_output.txt", mode = "a") as file:
    file.write("\n This is new line appended to the end of previous data\n")

with open("data/output/sample_output.txt") as file:
    print(file.read())
