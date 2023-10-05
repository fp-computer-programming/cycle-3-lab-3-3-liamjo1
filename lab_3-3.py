"""
Create a Python file named lab_3-3.py
Import the random module.

Use the randint() function to generate a random integer between 1 and 100.
Compare your result with another classmate. What do you notice about the results? Write your answers as a comment.

Use the seed() function to set the random seed to a value that you and a classmate agree on.

Use the randrange() function to generate an even number between 0 and 100. 
Compare your result with your classmate. What do you notice about the results? Write your answers as a comment.

"""
import random

x = random.randint(1, 100)
print(x)

#I got 68 and my classmate got 96

z = random.seed(30)
print(z)

y = random.randrange(0, 100, 2)
print(y)

#I got "None" for the seed function. I got 68 for my randrange output. The answer is always different everytime I run the program but is always between 0 and 100.