# Question 1

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']  # This defines cheese as a list (a list is mutable, ordered, duplicates and a variety of all elements
cheese += 'Oke'                                  # This attempts to add Oke to the cheese list however adds each letter seperately
print(cheese)                                    # This prints the list cheese

print(' ')
print(' ')

# There are three ways we can add elements to a list - append, insert and extend
# append will only accept one paramater

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']  # This is the basic list
cheese.append('Oke')                             # Adds oke to the list using individual element option
print(cheese)                                    # Prints cheese

print(' ')
print(' ')

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']  # This is the basic list
cheese.extend(['Gruyer', 'Brie'])                # This accepts multiple elements and adds them to the end of the list
print(cheese)                                    # This prints the list

print(' ')
print(' ')

# Question 2

tup = 'Hello'
print(len(tup))
tup = 'Hello',
print(len(tup))
# the comma transforms this string in to a list with 1 item as a comma is used to separate items in a list or tuple.
# When a string ends with a comma, it is interpreted as a list with one item (adding 'Goodbye' would return 2)
# The length returned is 1 (item) rather than 5 characters.
tup = 'Hello', 'Goodbye'
print("The length is now ", len(tup))

