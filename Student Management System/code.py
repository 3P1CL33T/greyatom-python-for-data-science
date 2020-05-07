# --------------
# Code starts here

# Create the lists 
class_1 = ['Geoffrey Hinton','Andrew Ng', 'Sebastian Raschka', 'Yoshua Bengio']
class_2 = ['Hilary Mason', 'Carlo Gentry', 'Corinna Cortes']
# Concatenate both the strings
new_class = class_1 + class_2

# Append the list
new_class.append('Peter Warden')
# Print updated list

print(new_class)
# Remove the element from the list
new_class.remove('Carlo Gentry')

# Print the list
print(new_class)


# Create the Dictionary

courses ={}

# Slice the dict and stores  the all subjects marks in variable

courses['Math'] = 65
courses['English'] = 70
courses['History'] = 80
courses['French'] = 70
courses['Science'] = 60
print(courses)
# Store the all the subject in one variable `Total`
total = (courses.get('Math') + courses.get('English') + courses.get('History') + courses.get('French') + courses.get('Science'))
# Print the total
print(total)
# Insert percentage formula
percentage = total*100/500

# Print the percentage
print(percentage)



# Create the Dictionary
 
mathematics = {'Geoffrey Hinton': 78, 'Andrew Ng': 95, 'Sebastian Raschka': 65,
'Yoshua Benjio': 50, 'Hilary Mason': 70, 'Corinna Cortes': 66, 'Peter Warden': 75}


# Given string
topper = 'andrew ng'

# Create variable first_name 

first_name = topper.split()[0]


# Create variable Last_name and store last two element in the list
last_name = topper.split()[1]
# Concatenate the string
full_name = last_name + " " + first_name
# print the full_name
certificate_name = full_name.upper()
# print the name in upper case

print(certificate_name)

# Code ends here


