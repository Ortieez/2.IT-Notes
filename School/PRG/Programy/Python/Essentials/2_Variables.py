"""
Variables are objects
"""

age = 36 # Whole number
bodyHeight = 1.76 # Float number
firstName, lastName = "John", "Doe"
fullname = firstName + " " + lastName # Putting together strings
fullname2 = "{1} {0}" # Brackets for formatting string
fullname2 = fullname2.format(firstName, lastName) # Function that formats fullname2 and puts firstName, lastName inside of brackets
born = str('Petach Tikva, Izrael') # Set a data type by putting it into a str() function
betsKnown = 'Some DC Character'

# And then you can print them.. wow
print(fullname2)
print(type(age))