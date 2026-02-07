#1
name=input("enter your name:")
print(name.upper())

#2
name=input("enter your name:")
print(name.lower())

#3
name=input("enter your name:")
print(name.capitalize())

#4
word = "XEXEXEEXEXEXEX"
symbol = input("enter your symbol: ")

if symbol in word:
    print(symbol + " - " + word.index(symbol))
else:
    print("This symbol is not in word")

#5
my_name="Mari"
print(len(my_name))

#6
name=input("enter your name:")
print(name.startswith("g"))

#7
name = input("enter your name: ")
print(name.endswith("l"))