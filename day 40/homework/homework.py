#1This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.
def simple_multiplication(number) :
    if number %2 ==0:
        return number *8
    else:
        return number*9

#2In this Kata we are passing a number (n) into a function Your code will determine if the number
#  passed is even (or not).The function needs to return either a true or false.Numbers may be positive or negative,
#  integers or floats.Floats with decimal part non equal to zero are considered UNeven for this kata.
def is_even(n): 
    return n % 2 == 0

#3Your task is to create a function that does four basic mathematical operations.
#The function should take three arguments - operation(string/char), value1(number), value2(number).
#The function should return result of numbers after applying the chosen operation.
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    if operator == '-':
        return value1 - value2
    if operator == '*':
        return value1 * value2
    if operator == '/':
        return value1 / value2
    
#4Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
def bool_to_word(boolean):  
    if boolean == True:
        return "Yes"
    elif boolean == False:
        return "No"

#5Write a function which calculates the average of the numbers in a given array. Note: Empty arrays should return 0.
def find_average(numbers):
    if len(numbers) == 0:
        return 0    
    total = 0
    for i in numbers:
        total += i    
    return total / len(numbers)
   
