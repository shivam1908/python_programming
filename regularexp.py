#import regex module
import  re

# #defint the pattern
# contact = re.compile(r'(\+91)*\d{10}')
# print(f"type of contact pattern is {type(contact)}")
#
# # searh for mobile number in the string  -- returting the match object
# contact_det = contact.search('My contact no is +919814447599')
# print(f"the contact no is : {contact_det.group()}")

contact = re.compile('do[gh]')
match = contact.fullmatch('doh')
print(f"the match  is : {match.group()}")
