list_of_names = ["დავით", "მარიამი", "ნინო", "დავით", "გიორგი", "დავით"]

name_to_count = "დავით"
count = list_of_names.count(name_to_count)

print("სახელი {name_to_count} მეორდება {count} ჯერ.")

print("----------")

numbers = [1, 2, 3, 4, 5]

numbers.reverse()

print(numbers)

print("----------")

arr = [1, 2, 3]
list = arr * len(arr)
print(list)

print("----------")

arr = ["python", "java", "java script"]
arr.insert(1, "დავითი")
print(arr)

print("----------")

list = ["python", "java", "python", "java script", "python"]
count = list.count("python")
list.remove("python")
print(count)
print(list)