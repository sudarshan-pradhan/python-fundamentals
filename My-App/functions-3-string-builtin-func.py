####################################################

# a_string.find(substring, start, end)

random_string = "This is a string"
print(random_string.find("is"))  # First instance of 'is' occurs at index 2
print(random_string.find("is", 9, 13))  # No instance of 'is' in this range

####################################################

# a_string.replace(substring_to_be_replaced, new_string)

a_string = "Welcome to Educative!"
new_string = a_string.replace("Welcome to", "Greetings from")
print(a_string)
print(new_string)

####################################################

print("UpperCase".upper())
print("LowerCase".lower())

####################################################

llist = ['a', 'b', 'c']
print('>>'.join(llist)) # joining strings with >>
print('<<'.join(llist)) # joining strings with <<
print(', '.join(llist)) # joining strings with comma and space

####################################################

string1 = "Learn Python {version} at {cname}".format(version = 3, cname = "Educative")
string2 = "Learn Python {0} at {1}".format(3, "Educative")
string3 = "Learn Python {} at {}".format(3, "Educative")

print(string1)
print(string2)
print(string3)

####################################################