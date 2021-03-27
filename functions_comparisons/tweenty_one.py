from random import randrange

number_of_points = 0
print("You have", number_of_points, "points")

while True: 
    confirmation = input("Do you wanna a card?: ")

    if confirmation == "no":
        print("You loose! You have", number_of_points, "points. It is missing",(21-number_of_points), "points to reach 21 points")
        break

    random_number = randrange(2,10)
    number_of_points += random_number
    print("You got", random_number)
    print("You have", number_of_points, "points!")

    if number_of_points > 21:
        print("You loose! You have", number_of_points, "points")
        break
    elif number_of_points == 21:
        print("You win! You have", number_of_points, "points")
        break




    




 







