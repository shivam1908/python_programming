#Program to list the non vowel in the string
user_input = input("Please Enter the string to evaluate: ")
non_vowels = [char for char in user_input.lower() if char not in "aeiou "]
print(non_vowels)

