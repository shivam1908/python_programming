# to combine the map() and filter() using lambda

names = ['lassie','Colt','Rusty']

#Return a new list with the string
# "Your instructor i s" + each value in list,
# but only if the value is less than 5 characters

print(list(map(lambda name: f"Your instructor is {name}",filter(lambda value: len(value) < 5, names))))

