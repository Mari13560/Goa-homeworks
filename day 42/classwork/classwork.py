#1Write a function which converts the input string to uppercase.
def make_upper_case(s):
    return s.upper()

#2Write a program that finds the summation of every number from 1 to num (both inclusive). The number
# will always be a positive integer greater than 0. Your function only needs to return the result, what is 
# shown between parentheses in the example below is how you reach that result and it's not part of it, see the sample tests.
def summation(num):
    total = 0
    for i in range(1, num + 1):
        total += i
    return total

#3Define String.prototype.toAlternatingCase (or a similar function/method such as to_alternating_case/toAlternatingCase/ToAlternatingCase 
# in your selected language; see the initial solution for details) such that each lowercase letter becomes uppercase and each uppercase 
# letter becomes lowercase. For example:
def to_alternating_case(string):
    result = ""
    for i in string:
        if i == i.upper():
            result += i.lower()
        else:
            result += i.upper()
    return result


#4Can you find the needle in the haystack?
#Write a function findNeedle() that takes an array full of junk but containing one "needle"
#After your function finds the needle it should return a message (as a string) that says:
#"found the needle at position " plus the index it found the needle, so:
def find_needle(haystack):
    index = haystack.index("needle") 
    return f"found the needle at position {index}"

#5Your task is to create a function that does four basic mathematical operations.
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