favorite_movies = ("Squid Game", "The Dark Knight", "Nabeglavi", "The Matrix", "the flash", "kill bill")

first_two_movies = favorite_movies[:2]  
print(first_two_movies)

print("----------")

numbers = (2, 56, 99, 22, 15, 23, 66, 11, 134, 23, 66, 91, 22, 2, 23)

count_23 = numbers.count(23)
print(count_23)

print("----------")

aura = (10, 25, 5, 80, 70, 20)
for number in aura:
    if number > 10:
        print(number)

print("----------")
