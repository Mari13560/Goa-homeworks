#1Write a method, that will get an integer array as parameter and will process every number from this array.
#Return a new array with processing every number of the input-array like this:
#If the number has an integer square root, take this, otherwise square the number.
def square_or_square_root(arr):
    result = []
    for x in arr:
        if (x ** 0.5) % 1 == 0:
            result.append(int(x ** 0.5))
        else:
            result.append(x * x)
    return result

#2Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
#Return your answer as a number.
def sum_mix(arr):
    sum = 0
    for i in arr:
        sum += int(i)
    return sum

#3Given an array of Boolean values and a logical operator, return a Boolean result based on sequentially applying
#  the operator to the values in the array.
def logical_calc(array, op):
    res = array[0]
    for i in array[1:]:
        if op == 'AND':
            res = res and i
        elif op == 'OR':
            res = res or i
        elif op == 'XOR':
            res = res != i
    return res

#4You should return the result of applying the given operation to these numbers.
#Note: In dynamically typed languages (JS, PHP, Python), the first and second arguments can be not numbers. In that case, return "unknown value".
#If the given operation to perform on the two numbers is not one of the four mentioned above, you should:
def calculator(x, y, op):
    if type(x) == type(0) and type(y) == type(0):
        if op == '+':
            return x + y
        elif op == '-':
            return x -y
        elif op == '*':
            return x * y
        elif op == '/':
            return x / y
        else:
            return "unknown value"
    else:
        return "unknown value"
#5Given a non-negative integer, 3 for example, return a string with a murmur:
#  "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.
def count_sheep(n):
    result = ''
    for i in range(1, n + 1):
        result += f"{i} sheep..."
    return result