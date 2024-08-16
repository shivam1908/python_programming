def count_up_to(max):
    count =1
    while count<=max:
        print('before yield')
        yield count
        print('after yield')
        count += 1
        print('after count')

counts= count_up_to(20)
print('before calling next')
print(next(counts))
print("calling 2nd next")
print(next(counts))
print(next(counts))
