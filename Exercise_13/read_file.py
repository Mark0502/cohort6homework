

# 6 Use a loop to iterate over and print the contents of the file. Do not to include any blank lines in the output.

file = open('pelican.txt', 'r')             # This opens the pelican.txt as a readme file

print("the type of data is ", type(file))   # This returns the type of data that is in the file

print(" ")                                  # This prints a blank line
print(" ")                                  # This prints a blank line

print(file)                                 # This prints the contents of the open file

print(" ")                                  # This prints a blank line
print(" ")                                  # This prints a blank line

# What data type is the output?
print("the type of data is ", type(file))

pelican_list = open("pelican.txt").readlines()

print(" ")
print(" ")

print(type(pelican_list))
print("There are ", len(pelican_list), " items in this list")

print(" ")
print(" ")

with open("pelican.txt") as p:
    for line in p:
        print(line.strip())
