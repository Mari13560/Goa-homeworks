#1
numbers=[1, 2, 3, 4, 5, 6, 7]
sum=0
for i in numbers:
    print(i)
    sum+=i
print(sum)

#2
numbers=[1, 2, 3, 4, 5, 6, 7]
n=0
for i in numbers:
    if i % 2 == 0:
        n +=1
print(n)

#3
numbers=[23, 34, 45, 1, 3, 23]
min = numbers[0]
max = numbers[0]
for i in numbers:
    if i < min:
        min = i
    if i > max:
        max = i
print(min)
print(max)

#4
numbers=[1, 2, 3, 4, 5, 6, 7]
for i in numbers:
    if i % 2 != 0:
        print(i)

#5
total = 0
while True:
    num=int(input("enter your number: "))
    if num == 0:
        break
    total += num
print(total)
    
#6
while True:
    num=int(input("enter your number: "))
    if num < 0:
        break

#7
while True:
    num=int(input("enter your number: "))
    if num % 5 == 0:
        break

#8
total = 0
while True:
     num=int(input("enter your number: "))
     if num % 2 == 0:
      total += 1
      break
print(total)

     
#9
while True:
     num=int(input("enter your number: "))
     if num % 2 != 0:
         break

#10
while True:
    num = int(input("enter your number: "))
    if num < 0:
        continue
    if num == 0:
        break
print(num)

#11
while True:
    num = int(input("enter your number: "))
    if num < 0:
        continue
    if num == 100:
        break
print(num)