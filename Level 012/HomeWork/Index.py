for i in range (1, 50, 2):
    print('number' + str(i))

i = 1
while i < 50:
    print( i )
    i = i + 2

print('----------')

size = 5
for i in range (size):
    print("*" * size)

print('----------')

i = 0
while i < 3:
    print("*" * 6)
    i = i + 1

print('----------')

num1 = 17
num = 16
for i in range(num1):
    print(num1)
for i in range(num):
    print(num)

print('----------')

password = 1234
password1 = input("password: ")

while password != password1:
    password1 = input("try again: ")
    if password == password1:
        print("welcome")