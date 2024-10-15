# Task 1: Define the Largest Function
def largest(a, b):
    """
    This function returns the largest number between two given numbers.
    """
    return a if a > b else b


# Task 2: Define the Smallest Lambda Function
smallest = lambda a, b: a if a < b else b


# Task 3: Define the Sorting Function
def sorting(lst, order):
    """
    This function sorts a list of numerical values.

    Parameters:
    lst (list): List of numerical values.
    order (str): Sorting order - "ASC" for ascending, "DES" for descending.

    Returns:
    list: Sorted list in the specified order.
    """
    if order == "ASC":
        # Sort using the largest function for ascending order
        sorted_list = sorted(lst, reverse=False)
    elif order == "DES":
        # Sort using the smallest function for descending order
        sorted_list = sorted(lst, reverse=True)
    else:
        print("Invalid sorting order. Please use 'ASC' or 'DES'.")
        return []

    return sorted_list


# Import functions for Map and Reduce
from functools import reduce

#Task 4
# Function to sort in ascending order using largest and map/reduce
def sort_asc(lst):
    return sorted(lst, key=lambda x: reduce(largest, map(lambda y: y, [x])))


# Function to sort in descending order using smallest and map/reduce
def sort_des(lst):
    return sorted(lst, key=lambda x: reduce(smallest, map(lambda y: y, [x])), reverse=True)


# Testing the functions
if __name__ == "__main__":
    # Sample inputs
    a = 10
    b = 20
    lst = [34, 23, 67, 100, 88, 2, 45, 10]

    # Using Largest function
    print("Largest of", a, "and", b, "is:", largest(a, b))

    # Using Smallest function
    print("Smallest of", a, "and", b, "is:", smallest(a, b))

    # Using the custom sorting function for comparison
    print("List sorted in ascending order using custom function:", sorting(lst, "ASC"))
    print("List sorted in descending order using custom function:", sorting(lst, "DES"))

    # Using Sorting function
    print("List sorted in ascending order using map and reduce:", sort_asc(lst))
    print("List sorted in descending order using map and reduce:", sort_des(lst))

    # Substantiating with inbuilt sort function
    print("List sorted in ascending order using inbuilt sort():", sorted(lst))
    print("List sorted in descending order using inbuilt sort():", sorted(lst, reverse=True))
