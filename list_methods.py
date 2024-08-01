data = list(range(0,4))
print(f"original list is as follows :  {data}")

data.append(5)
# data.append(5,6)  ERROR appendcan insert one element at a time

#data.extend(2)   ERROR - extendcan add values from iterables like list, tuple string,etc

data.extend((7,8))

data.insert(4,(12,13))
print(f"List after insertion: {data}")

#clear() delete all the items from list
data.clear()
print(f"list after clear(): {data} ")

data =list(range(1,5))

print("items in list before pop() : {}".format(data))
# pop() -- TO delete and return the last element of the list
popped_value= data.pop()
print("popped_value  : {}".format(popped_value))

print("items in list after pop() : {}".format(data))

#remove() -- search the item in the list DELETE IT
print("items in list after pop() : {}".format(data))


#list.index(item) returns the index of the item in the list
data.extend(range(5,10))
print(f"List after insertion: {data}")
print(f"index of the item:6 is: {data.index(6)}")

#list.count(x)  -- return the no of occurences of x in the list
print(f"value in the liST Are : {data.extend([5,5,5,6])}{data}")
print(f"theno of occurences of 5 in list are : {data.count(5)}")

#list.sort() to sort the list
data.sort();
print(f"The sorted values of the list are: {data}")

# to print the list element in reverse
data= ["abcd",1234]
print(data[::-1])  
data.reverse()
print(data)


