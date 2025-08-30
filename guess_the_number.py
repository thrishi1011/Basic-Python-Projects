# Guess the number 

while True:
    try:
        n = int(input("Plzz select a number between (1-100): "))
    
    except ValueError:
        print("Invalid input!")
        continue  # ask again

    if n > 27:
        print("The number is too large!")
        continue
    elif n < 27:
        print("The number is too small!")
        continue
    else:
        print("You have guessed the correct number!")
        print("Thanks for playing :)")
        break

