# user_module.py

def greet(name):
    print("Hello, {}!".format(name))

# main.py

# Importing user-defined module
import user_module

# Importing built-in module
import random

# Using user-defined module
user_module.greet("Alice")

# Using built-in module
print("Random number:", random.randint(1, 100))
