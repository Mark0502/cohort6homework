#!/usr/bin/python

# string formatting is concatenation using the f' (formatted string using f and curly braces {} \ place holders)
#. function is methods in a function (i.e course.upper changes a variable as uppercase) - doesnt modify or change creates a new string

belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

belgium_length = len(belgium)    # This will check length of belgium and store it as a integer
#print(belgium_length)           # This will print the length of the integer

# Question 1 section 3a
for x in range(belgium_length):  # This will while x in range belgium (81)
    output = '-'                 # This converts the range belgium_length and output each return as a hypthen
    #print(output)                    # This will print 0 -80 (81)
    print(output, end="")        # This prints the 80 hypthens in a single line (the end"" is used to print on same line - keeping double quotes merges all elements on same line)
#hyphens = (output.end="")       # tring to define all hyphens as a single line and holding as variable

print(" ")
print(" ")

# Question 1 section 3b
replace = belgium.replace(',', ':')     # This changes the comma with colons

print(replace)                          # This is the changed return
#three_b_test =  # attempting formatted string long code
#three_b_answer = f'{hyphens} [{replace}]' # attempting formatted string
#print(three_b_answer)

print(" ")
print(" ")

# Question 1 section 3c
# Math addition with 1 and 3 from belgium

belgium_list = belgium.split(",")
print(belgium_list)

print(" ")
print(" ")

#total_population = f'{int(belgium_list[1])} + {int(belgium_list[3])}' # attempting formatted string

belgium_population = int(belgium_list[1])
print(belgium_list[1])

print(" ")
print(" ")

capital_population = int(belgium_list[3])
print(belgium_list[3])

print(" ")
print(" ")

total_population = belgium_population + capital_population
print(total_population)
