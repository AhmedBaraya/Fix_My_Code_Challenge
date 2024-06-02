def fizzbuzz(n):
  """
  This function prints the FizzBuzz sequence up to a given number.

  Args:
      n: An integer representing the upper limit of the sequence.
  """
  for i in range(1, n + 1):
    output = ""
    if i % 3 == 0:
      output += "Fizz"
    if i % 5 == 0:
      output += "Buzz"
    if not output:  # Check if output is empty string
      output = str(i)
    print(output)

# Example usage with n = 50
fizzbuzz(50)
