# ---- String Methods and Data Types ----

num = 1001

# Throws an error:
#print(len(num))

# 1. Use type conversion to print the length (number of digits) of an integer.

num = str(1001)

# 2. Print the length of 'num'

print(len(num))

# 3. Print the number of digits in a FLOAT value (e.g. num = 123.45 has 5 digits but a length of 6).

float = str(123.45)

print(len(float)-1)

#from the book
num = 123.45
new_num = str(num).replace(".", "")
print(len(new_num))

# 4. Experiment! What if num could be EITHER an integer or a decimal?  Add an if/else statement so your code can handle both cases.

user_var = input("Enter a number (integer or decimal) to get a digit count.")

#input is a string
#print(type(user_var))

if "." in user_var:
	print(len(user_var) -1)
else:
	print(len(user_var))
