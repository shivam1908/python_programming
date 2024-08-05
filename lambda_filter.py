
numbers = list(range(1,101))

evens =list(filter(lambda num: num%2 ==0,numbers))
odds =list(filter(lambda num: num%2 !=0,numbers))

print(f"Even number are : {evens}\nOdd numbers are : {odds}")
