import math

# Get an integer number from the user (handle potential errors)
while True:
  try:
    number = int(input("Please enter a positive integer: "))
    if number <= 0:
      print("Please enter a positive number.")
    else:
      break
  except ValueError:
    print("Please enter a valid integer number.")

# Calculate the factorial of the number
factorial = math.factorial(number)

# Calculate the natural logarithm (ln) and logarithm to base 10 (log10)
natural_logarithm = math.log(number)
logarithm_base_10 = math.log10(number)

# Print the results
print(f"The factorial of {number} is: {factorial}")
print(f"The natural logarithm (ln) of {number} is: {natural_logarithm}")
print(f"The logarithm to base 10 (log10) of {number} is: {logarithm_base_10}")
