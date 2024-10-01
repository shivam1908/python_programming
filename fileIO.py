f = open("data/sample_data.txt")
print(f.read())

f.seek(0)
print(f.read())
f.seek(20)
print(f.read())
f.close()
print(f"file closed status : {f.closed}")