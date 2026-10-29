print("Select your ride \n 1. Bike \n 2. Car ")
choiceVehicle = int(input("Enter you choice (1 or 2): "))

if choiceVehicle == 1:
    print("You have selected Bike ride")
    print("Enter the type of bike \n B1. Hero Splendor \n B2.Honda Shine ")
    choiceBike = input("Enter the type of vehicle : ")
    if choiceBike == "B1":
        print("You have selected Hero Splendor")
    elif choiceBike == "B2":
        print("You have selected Honda Shine")
    else:
        print("Invalid input")

elif choiceVehicle == 2:
    print("You have selected Car drive")
    print("Enter the type of vehicle \n C1. Indica \n C2. Xylo")
    choiceCar = input("Enter the type of vehicle")
    if choiceCar =="C1":
        print("You have selected Indica")
    elif choiceCar == "C2":
        print("You have selected Xylo")
    else:print("Invalid Input")
else:
    print("Invalid input")