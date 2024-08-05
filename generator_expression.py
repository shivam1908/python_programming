import sys
list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))

print(f"List Comprehension memory consumption : {list_comp} bytes")
print(f"Generator Expression memory consumption : {gen_exp} bytes")
