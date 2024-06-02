class User:
  """
  A User class to represent a user with a username and password.
  """

  def __init__(self, username, password):
    """
    Initializes a User object with a username and password.

    Args:
        username: The username for the user.
        password: The password for the user.
    """
    self.username = username
    self.password = password

  def __str__(self):
    """
    Returns a string representation of the User object.

    Returns:
        A string containing the username.
    """
    return self.username

  def is_valid_password(self, password):
    """
    Checks if the provided password matches the user's password.

    Args:
        password: The password to be validated.

    Returns:
        True if the password matches the user's password, False otherwise.
    """
    # Implement password validation logic here (e.g., compare passwords)
    return self.password == password  # Example validation (replace with your logic)

# Example usage
user = User("Test User", "correct_password")

# Test is_valid_password (replace with your actual test cases)
if user.is_valid_password("correct_password"):
  print("Valid password")  # Print success message if valid
else:
  print("Invalid password")  # Print error message if invalid

print(user)  # Print username using __str__
