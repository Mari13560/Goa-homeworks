#True
print(9 > 3)
print(True and True)
print("cool" == "cool")
print(9 >= 9)
print(9 < 12)
#False
print(9 > 12)
print("co" == "fghj")
print(12 <= 2)
print(False or False)
print(4567 <3)
#sequencing - ინსტრუქციების თანამდევრობა რომელსაც კიმპიუტერი მიჰყვება  ნაბიჯ-ნაბიჯ 
#iteration - მოქმედება რომელიც სრულდება მანამდე სანამ გარკვეული პირობა არ შესრულდება 
#selection - არჩევანი რომელსაც პროგრამა აკეთებს რაღაცა პირობის გამომდინარე
#ეს არის sepuencing კოდი სრულდება ზედიზედ ჯერ პირველი ხაზი მერე მეორე და ბოლოს მესამე.
x="Hello"
y="world"
print(x + " " + y)
#for loop - ციკლი რომელსაც ვიყენებთ როცა გვინდა რამდენჯერმე გავიმეოროთ ერთი და იგივე რაღაცა
#range() ფუნქციას გადაეცება ის ინფორმაცია თუ რამდენჯერ გვინდა დავბეჭდოთ რაღაცა
#for loop კი იღებს range()-დან რიცხვს და ბჭდავს მაგდენჯერ
for i in range(1):
    print("mercedes")
for i in range(100):
    print("Dekanosidze")
for i in range(46):
    print("brown")
for i in range(32):
    print("M")
name=input("enter your name: ")
surname=input("enter your surname: ")
age=int(input("enter your age: "))
g=input("enter i am: ")
age=str(age)
print(g + " " + name + " " + surname + " " + "and" + " " + g + " "+ age)
name="Mari"
age=23
bib=12.0
f=False
print(type(name))
print(type(f))
print(type(age))
print(type(bib))
num1=int(input("enter your number: "))
num2=int(input("enter your number: "))
num3=int(input("enter your number: "))
num4=int(input("enter your number: "))
print(num1 + num2 + num3 + num4)
