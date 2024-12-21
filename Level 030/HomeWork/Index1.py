def positive_sum(arr):
    return sum(x for x in arr if x > 0)
arr = [1 , 4 , -1, -10 , 12 , -13]
print(positive_sum(arr))