# Ask the user for their name
username = input("What is your name?")

# ask user for their favourite number
fav_num = int(input("Favourite Number?"))

# double, halve, and square the number
double = fav_num * 2 
half = fav_num / 2 
squared = fav_num * fav_num

# Empty print helps code look good
print()

# Greet user
print("Hi {}, your favourite number is {}.". format(username, fav_num, ))

# Tell the user their favourite number doubled, halved, and squared
print("Your favourite number doubled is {}". format(double))
print("Your favourite number halved is {}". format(half))
print("Your favourite number squared is {}". format(squared))