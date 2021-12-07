# Control Flow

# Comaprison Operators

number_one = 20
number_two = 10

print(number_one == number_two)

print(number_one > number_two)

print(number_one < number_two)

print(number_one != number_two)


# Conditional Statement:

if number_one > number_two:
    print("If is True Statement")
elif number_one == number_two:
    print("elif is True this time")
else:
    print("else is True here")

print("Out from Control Statement")


# Ternary Operators

age = 22
age_adv = 18


if age >= 18:
    print("Eligible-low")
else:
    print("Not Eligble-low")

if age >= 20:
    message = "Eligible-med"
else:
    message = "Not Eligble-med"

print(message)


advance_message = "Eligible-ADV" if age_adv >= 22 else "Not Eligible-ADV"

print(advance_message)
