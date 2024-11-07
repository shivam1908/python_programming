def read_line():
    return input("Enter a line (or 'stop' to end): ")

# Create an iterator that reads lines until 'stop' is entered
iterator = iter(read_line, 'stop')

# Iterate through input lines
for line in iterator:
    print(f"You entered: {line}")
