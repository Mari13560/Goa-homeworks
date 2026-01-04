#2
secret_number = 34
while True:
    user_number = int(input("შეიყვანეთ რიცხვი: "))
    if user_number == secret_number:
        print("თქვენ სწორად გამოიცანით რიცხვი!")
        break  
    else:
        print("არასწორია, სცადეთ კიდევ")
        continue

#3
number = int(input("შეიყვანეთ რიცხვი: "))
while True:
    if number % 2 == 0:
        print("შეყვანილია ლუწი რიცხვი!")
        break  
    else:
        print("კენტი რიცხვია, სცადეთ კიდევ")

#1
numbers = [1, 2, 3, 4, 5, 6,]
total = 0
for i in numbers:
    total += i

print(total)
print(total/6)