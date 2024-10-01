with open("data/sample_data.txt") as file:
    print(file.read())
print(f"File close status True if still open else False : {file.closed}")
