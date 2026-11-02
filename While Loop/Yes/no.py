activities = 4
print(f"You have {activities} chores to complete today")

completed_count  = 0
activity_num = 1
activity_name = ""


while activity_num <= activities:


    if activity_num == 1:
        activity_name = "Did you make your bed ?"
    elif activity_num == 2:
        activity_name = "Did you feed the pet ?"
    elif activity_num == 3:
        activity_name = "Did you take out the trash ?"
    elif activity_num == 4:
        activity_name = "Did you wash the dishes ?"
    else:
        print("Okay, finish it and check again !")
    answer = input(f"{activity_name} yes/no : ")
    answer = answer.lower()

    if answer == "yes":
        completed_count += 1 
        activity_num += 1
        print("Great job! Chore comepleted")

    print("Chores remaining: ", activities - completed_count)
    print()