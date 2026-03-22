#Make a simple function called greet that returns the most-famous "hello world!".
def greet ():
    return "hello world!"

#In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?
def make_negative(number):
    if number > 0:
        return number * -1
    elif number < 0:
        return number
    elif number == 0:
        return 0
    
#This code does not execute properly. Try to figure out why.
def multiply(a, b):
  return  a * b

#Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
def even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
    
#Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.
def quarter_of(month):
    if month <= 3:
        return 1
    elif month <= 6:
        return 2
    elif month <= 9:
        return 3
    else:
        return 4