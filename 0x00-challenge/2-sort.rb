# Function to sort arguments, handling both numbers and strings
def sort_arguments(args)
  """
  Sorts a list of arguments, handling both numbers and strings.

  Args:
      args: A list of arguments (numbers and strings).

  Returns:
      A new list with the arguments sorted numerically (numbers) and alphabetically (strings).
  """

  # Separate numbers and strings
  numbers = []
  strings = []
  for arg in args
    try
      # Attempt conversion to float for numerical sorting
      num = float(arg)
      numbers.append(num)
    rescue ValueError
      # If conversion fails, treat as string
      strings.append(arg)
    end
  end

  # Sort numbers and strings separately
  numbers.sort!
  strings.sort!

  # Combine sorted lists, preserving numerical order
  return numbers + strings
end

# Example usage
arguments = ["12", 41, 2, "C", 9, "-9", 31, "fun", "-1", 32]
sorted_args = sort_arguments(arguments)

# Print the sorted arguments
for arg in sorted_args
  print arg, " "
end
