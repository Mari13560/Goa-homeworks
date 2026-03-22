#1
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(11,21):
    nums.append(i)
for i in range(5):
    nums.pop(i)
print(nums)

#2
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(11,21):
    num.append(i)
for i in range(1, 6):
    num.remove(i)
print(num)

#3
numi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(11, 21):
    numi.append(i)
for i in range(1, 6):
    numi.remove(i)
for i in range(5):
    numi.pop()
print(numi)

#4
colors = ["red", "green", "blue", "yellow", "purple"]
colors.pop()
print(colors)

#5
nums = [10, 20, 30, 40]
nums.append(50)
print(nums)