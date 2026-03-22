#1Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
#The output should be two capital letters with a dot separating them.
def abbrev_name(name):
    name = name.split()
    name1 = name[0]
    lastname = name[1]
    name1 = name1[0]
    lastname = lastname[0]
    return f"{name1}.{lastname}".upper()

#2Nathan loves cycling.
#Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
#You get given the time in hours and you need to return the number of litres Nathan will drink, rounded down.
def litres(time):
    return int(time*0.5)

#3Write a function which calculates the average of the numbers in a given array.
#Note: Empty arrays should return 0.
def find_average(numbers):
    if len(numbers) == 0:
        return 0    
    total = 0
    for i in numbers:
        total += i    
    return total / len(numbers)

#4Create a function that checks if a number n is divisible by two numbers x AND y. All inputs are positive, non-zero numbers.
def is_divisible(n,x,y):
    if n%x ==0 and n%y == 0:
        return True
    else:
        return False
    
#5Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all
#  of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number
#  is prime return the string '(integer) is prime' (null in C#, empty table in COBOL) (use Either String 
# a in Haskell and Result<Vec<u32>, String> in Rust).
def divisors(integer):
    res=[]
    for i in range(2,integer):
        if integer % i == 0:
            res.append(i)
    if len(res)==0:
        return str(integer) + " is prime"
    else:
        return res