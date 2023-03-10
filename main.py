# Ask the user for their current age
age = input("What is your current age?\n ")

# Convert the age to int
age = int(age)

# Calculate how many days, weeks and months are left until 90 years old
days = (90 - age) * 365
weeks = (90 - age) * 52
months = (90 - age) * 12

# Account for leap years by adding one day for every four years
leap_years = (90 - age) // 4
days += leap_years

# Use f-strings to format the output message with the time left
message = f"You have\n{days} days\n{weeks} weeks\nand {months} months left."

# Print the message
print(message)