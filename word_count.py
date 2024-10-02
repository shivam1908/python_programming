def statistics(file_name):
    with open(file_name) as file:
        lines = file.readlines()
    return {
        "lines": len(lines),
        "words": sum(len(line.split(" ")) for line in lines),
        "characters": sum(len(line) for line in lines)
    }


stats = statistics("data/sample_data.txt")
print(stats)