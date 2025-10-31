#This is a strange .txt file. I think it looks like something different. I am not sure...
import random

def create_random_name(name):
  """
  Takes a string 'name' and appends a random number to it.
  
  Args:
    name: The input name (string).
    
  Returns:
    A new string in the format 'name_<random_number>'.
  """
  random_number = random.randint(0, 9999)
  return f"{name}_{random_number}"

# --- How to use the function ---

# 1. Provide the name you want to use
your_name = "Write Your name here"

# 2. Call the function and store the result
new_name = create_random_name(your_name)

# 3. Print the new name
print(new_name)