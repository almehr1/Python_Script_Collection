def is_prime(n):
  """
  This function checks whether a given number n is a prime number.

  Args:
    n (int): The number to be checked.

  Returns:
    bool: True if n is a prime number, False otherwise.
  """
  if n <= 1:
    return False
  elif n <= 3:
    return True
  elif n % 2 == 0 or n % 3 == 0:
    return False
  i = 5
  while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0:
      return False
    i += 6
  return True

def find_primes(up_to):
  """
  This function finds all prime numbers up to a given limit 'up_to'.

  Args:
    up_to (int): The upper limit to find prime numbers up to.

  Returns:
    list: List of all prime numbers up to 'up_to'.
  """
  primes = []
  for num in range(2, up_to + 1):
    if is_prime(num):
      primes.append(num)
  return primes

# Example calls
print(is_prime(17))  # Output: True
print(is_prime(15))  # Output: False
print(find_primes(100))  # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
