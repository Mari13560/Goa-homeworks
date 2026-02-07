#2
#append() — ამატებს ელემენტს სიის ბოლოში
#insert() — ამატებს ელემენტს მითითებულ ინდექსზე
#pop() — შლის ელემენტს მითითებული ინდექსიდან

#3
arr=[12, 23, 34,"maru"]
print(len(arr))

#4
numbers = []
for i in range(5):
    num = int(input("enter your nymber: "))
    numbers.append(num)
print(numbers)

#5
colors = ["red", "green", "blue", "yellow", "purple"]
colors.pop()
print(colors)

#6
animals = ["dog", "cat", "elephant", "lion"]
animals.insert(2,"monkey")
print(animals)

#7
students = []
for i in range(3):
    name = input("enter students name: ")
    students.append(name)
students.insert(0, "Teacher")
students.pop()
print(len(students))
print(students)