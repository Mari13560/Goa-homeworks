num = int(input("შეიყვანეთ რიცხვი: "))
if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

num  = int(input("enter the number: "))
while num:
    if num < 0:
        print("შეყვანილია უარყოფითი რიცხვი. პროგრამა დასრულდა.")
        break
    else:
        print("რიცხვი დადებითია ან ნულია")

correct_pin = "1234"
attempts = 3
while attempts > 0:
    pin = input("შეიყვანეთ PIN კოდი: ")
    if pin == correct_pin:
        print("Access Granted")
    else:
        attempts -= 1
if attempts == 0:
    print("Access Denied")

fruits = ["ვაშლი", "ბანანი", "ატამი", "მსხალი", "ალუბალი"]
print(fruits[2])

numbers = [10, 20, 30, 40, 50]
numbers[1] = 25
print(numbers)

colors = ["წითელი", "მწვანე", "ლურჯი", "ყვითელი", "იასამნისფერი"]
index = int(input("შეიყვანეთ ინდექსი (0-დან 4-მდე): "))
print(colors[index])

animals = ["ძაღლი", "კატა", "სპილო", "ვეფხვი", "ლომი"]
animals[-1] = "გემი"
print(animals)

colors = ["თეთრი", "შავი", "ნარინჯისფერი", "ვარდისფერი"]
index = int(input("შეიყვანეთ ინდექსი: "))
new_color = input("შეიყვანეთ ახალი ფერი: ")
colors[index] = new_color
print(colors)