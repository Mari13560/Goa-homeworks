num = 15
if num > 10:
    print("more than 10")
else:
    print("less than 10")
num1 =int(input("enter your number:"))
if num1 == 15:
    print("equal to 15")
else:
    print("not equal to 15")
si =input("enter your word: ")
if si == "group 84":
    print("you are correct")
else:
    print("you are wrong")
for i in range(50, 100, 5):
    print(i)
for i in range(1):
    print("მარიამ დეკანოსიძე")
num = 20
while num <= 50:
    print(num)
    num += 1
for i in range(0, 100):
    print(i)
num = 20
while num <= 50:
    print(num)
    num += 1
for i in range(10, 20):
    print(i)
i = 10
while i <= 20:
    print(i)
    i += 1
for i in range(100, 201, 5):
    print(i)
i = 100
while i <= 200:
    print(i)
    i += 5
for i in range(10, -1, -1):
    print(i)
i = 10
while i >= 0:
    print(i)
    i -= 1
num = float(input("Enter a number: "))
if num > 0:
    print("ეს რიცხვი დადებითი რიცხვია")
elif num < 0:
    print("ეს რიცხვი უარყოფითი რიცხვია")
else:
    print("ეს რიცხვი ნულია")
age = int(input("enter your number: "))
if age <= 12:
    print("ბავშვი ხარ")
elif age <= 19:
    print("მოზარდი/თინეიჯერი ხარ")
elif age <= 64:
    print("ზრდასრული ხართ")
elif age <= 120:
    print("ხანში შესული ხართ")
elif age >= 120:
    print("გურუ ან ჯადოქარი")
elif age < 0:
    print("არასწორი ინფო")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c) 
day = int(input("Enter a number: "))
if day == 1:
    print("ორშაბათი")
elif day == 2:
    print("სამშაბათი")
elif day == 3:
    print("ოთხშაბათი")
elif day == 4:
    print("ხუთშაბათი")
elif day == 5:
    print("პარასკევი")
elif day == 6:
    print("შაბათი")
elif day == 7:
    print("კვირა")
else:
    print("არ ვიცი ეგ რა დღეა")
num = float(input("Enter a number: "))
if num > 50: 
    print(num * 5)
else:
    print(num * num)
password = input("Enter password: ")
if password == "goa123":
    print("Password is correct!")
else:
    print("Incorrect password!")
num = int(input("Enter a number: "))
total = 0
for i in range(1, num + 1):
    total += i
print( "sum:", total)