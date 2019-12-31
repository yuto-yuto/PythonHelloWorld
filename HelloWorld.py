"""
This is comment section
"""
from TestClass import *

def display_hello_world():
    """
    This is a function to display "Hello World!"
    :return: void
    """
    print("Hello World!")


display_hello_world()


# Set text
texts = ["Hello", "World", "!"]
for text in texts:
    print(text)

numberString = "917254"
for char in numberString:
    number = int(char, 10)
    if number > 5:
        print("The number ", number, " is greater than 5.")
    elif 5 == number:
        print("The number is 5.")
    else:
        print("The number ", number, " is less than 5.")

testClass = TestClass()
testClass.greet()

print("End")