#1Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
def remove_exclamation_marks(s):
    res = ''
    for i in s:
        if i != '!':
            res += i
    return res

#2You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.
#Considering these factors, write a function that tells you if it is possible to get to the pump or not.
#Function should return true if it is possible and false if not.
def zero_fuel(distance_to_pump, mpg, fuel_left):
    max_distance = mpg* fuel_left
    if max_distance>= distance_to_pump:
        return True
    else:
        return False

#3Define a function that removes duplicates from an array of non negative numbers and returns it as a result.
#The order of the sequence has to stay the same.
def distinct(seq):
    result = []
    for item in seq:
        if item not in result:
            result.append(item)
    return result

#4Two players - "black" and "white" are playing a game. The game consists of several rounds.
#  If a player wins in a round, he is to move again during the next round. If a player loses a round,
#  it's the other player who moves on the next round. Given whose turn it was on the previous round
#  and whether he won, determine whose turn it is on the next round.
def whoseMove(lastPlayer, win):
    if lastPlayer=='black' and win:
        return 'black'
    elif lastPlayer=='white' and win:
        return 'white'
    elif lastPlayer=='white' and not win:
        return 'black'
    return 'white'




#5Write function bmi that calculates body mass index (bmi = weight / height2).
#if bmi <= 18.5 return "Underweight"
#if bmi <= 25.0 return "Normal"
#if bmi <= 30.0 return "Overweight"
#if bmi > 30 return "Obese"
def bmi(weight, height):
    bmi = weight / (height * height)
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    else:
        return "Obese"