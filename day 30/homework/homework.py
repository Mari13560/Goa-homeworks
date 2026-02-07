#2) 
# .upper() — სტრინგს გადააქცევს მთლიანად დიდ ასოებად
# .lower() — სტრინგს გადააქცევს მთლიანად პატარა ასოებად
# .capitalize() — სტრინგის პირველ ასოს გაადიდებს, დანარჩენს დააპატარავებს
# .find() — ეძებს კონკრეტულ სიმბოლოს ან სიტყვას სტრინგში და აბრუნებს მის პირველ ინდექსს თუ ვერ იპოვა აბრუნებს -1

#3)
sentence = input("unter your sentence: ")
print(sentence.lower())

#4)
email = input("enter your email: ")
result = "@" in email
print(str(result).upper())

#5)
book = input("enter your book name: ")
print(book.capitalizetle())

#6)
text = input("enter your sentence: ")
char = input("enter your symbol: ")
count = text.count(char)

#7)
word=input("enter your word: ")
if word.isupper():
    print("სიტყვა უკვე დიდია!")
else:
    print(word.upper())