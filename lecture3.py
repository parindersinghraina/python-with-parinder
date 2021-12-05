# Primitive Type

# Variables

student_count = 1000
rating = 4.99
is_published = False
course_name = "Python Programming"


print(student_count)

# Variable Name should be descriptive ^


# String

course_name = "Python Programming"

# Get Length of the String
print(len(course_name))

# Print Index
print(course_name[0])

print(course_name[-1])

print(course_name[0:3])

print(course_name[0:])

print(course_name[:3])

print(course_name[:])


# Escape Character
# \"
# \'
# \\
# \n

course = "I am \nCourse"
print(course)

# Formatting String

first_name = "Parinder"
last_name = "Raina"
full_name = first_name + " " + last_name

print(full_name)


first = "Parinder"
last = "Raina"
full = f"{first} {last}"

print(full)


# String Methods

country_name = "Canada"

country_name_with_whitespaces = "   I am Canada  "

print(country_name.upper())
print(country_name.lower())
print(country_name.title())
print(country_name_with_whitespaces.strip())
print(country_name_with_whitespaces.lstrip())
print(country_name_with_whitespaces.rstrip())
print(country_name_with_whitespaces.find("C"))
print(country_name_with_whitespaces.replace("Canada", "India"))
print("India" not in country_name_with_whitespaces)


# Numbers

print(10 + 3)

print(10 - 3)

print(10 * 3)

print(10 / 3)

print(10 // 3)

print(10 ** 3)

print(10 % 3)

print(round(2.9))

print(abs(-2.9))

# Type Conversion

x = input("x:")

#  Getting Error : TypeError: can only concatenate str (not "int") to str
#y = x + 1 

y = int(x)+1

print(f"x:{x}, y: {y}")