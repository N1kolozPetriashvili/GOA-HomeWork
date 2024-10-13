age = input("ასაკი: ")
for i in range(1):
        print(age)

print("----------")

temperature_C = int(input("ტემპერატურა: "))
temperature_F = temperature_C * 9/5 + 32
print(temperature_F)

print("----------")

print(True or False)
print(True and False)
presence = True
temperature = 32
ac_on = (temperature > 30) and presence
print(ac_on)
print( 30 == 32 )
print( 54 > 60 )
print( 45 < 70)

print("----------")

rows = 3
for i in range(1, rows + 1):
        print("*" * i)

print("----------")

age = int(input("ასაკი: "))
print( age == 20)