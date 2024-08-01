# Nested list Comprehension
nested_list = [[1,2,3,4],[5,6],[7,8,9]]

[[print(val) for val in inner_list] for inner_list in nested_list]


# #---------------- different method  output is  [1,2,3,4,5,6,7,8,9]------
# listt = [val for inner_list in nested_list for val in inner_list] 
# print(f"the list is : {listt}")   


# ------------CREATE  NESTED LIST------
# nested_list = [[val for val in range(0,3)] for inner_list in range(0,3)]
# print(nested_list)