#1
arr=[34, 45, 23, 56, 67, 68]
print(len(arr))

#2
names=["mari","nanu","lizi","rati","sashka"]
name=input("enter your name: ")
print(names.append(name))

#3
names.insert(3, "Tarieli")

#4
names.pop(4)

#5
names.remove("lizi")

#6
name = input("Enter a name: ")
if name in names:
    print(name, "is at index", names.index(name))
else:
    print("not index in list")

#7
numbers = [2, 3, 4, 5, 6]
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)
print(numbers)