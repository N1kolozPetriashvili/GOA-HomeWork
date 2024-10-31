name = input("სახელი: ")
res = " "
for i in name:
    res += i +" "
print(res)

print("----------")

num = int(input("number:"))

for i in range(num):
    if i % 2 == 0 and i % 3 == 0:
        print(i)

print("----------")

result = 0
for i in range(5):
     number = int(input("გთხოვთ შემოიტანოთ ციფრი: "))
     result += number
average = result / 5
print(average)

print("----------")

for i in range(-100, 100):
    if i > 0:
        print(i)

print("----------")

num = int(input("შემოიტანეთ ციფრი: "))
number = 0
while num > number:
     num = int(input("შემოიტანეთ ციფრი: "))
print(" ")

print("----------")

rows = 8
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i, end = "")
    print(" " * (rows + i) + "*" * i)