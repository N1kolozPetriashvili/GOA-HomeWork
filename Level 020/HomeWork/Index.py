arr =["ა" , "ბ" ,"გ" , "დ"]
is_count ="ა"

for i in range(len(arr)):
    if arr[i] == is_count:
        print(arr[i])

print("----------")

new_arr = [5,15,60,75,12,32,14,30,12]

for i in range(len(new_arr)):
    if new_arr[i] % 5 ==0 and new_arr[i] % 3 ==0:
        print(new_arr[i])

print("----------")



print("----------")

arr =["******   " , " ******  " , "  ****** " , "   ******"]

print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])

print("----------")

age = int(input("age: "))

if age > 12:
    print("შენ არ ხარ 12 წლის")