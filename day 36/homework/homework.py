#2
#return- იგი წყვეტს ფუნქციას და აბრუნებს მნიშვნელობას ფუნქციის სახელთან
def numbers(a, b):
    sum = a+b
    return sum 
#ვქმნით ფუნქციას სახელად numbers მას გადაეცემა ორი პარამეტრი: a და b ვქმნით ცვლადს sum მასში ვინახავთ a და b-ის ჯამს
#ფუნქცია აბრუნებს result-ის მნიშვნელობას

#3
def list(numbers):
    pr = 1
    for i in numbers:
        pr = pr * i
    return pr
mylist = [2, 4, 5, 3, 4]
print(list(mylist))

#4
def xexe(a):
    return a
def gege(b):
     return b
result=gege(xexe(5))
print(result)