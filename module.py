### Exercise 2 - Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case

class someString():
    def __init__(self):
        self.str = ""
    
    def get_String(self):
        self.str = input()

    def print_String(self):
        print(self.str.upper())

str = someString()
str.get_String()
str.print_String()