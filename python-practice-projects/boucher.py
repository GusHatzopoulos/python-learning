# Ask for age
age = input("How old are you? ")
if age:
    age = int(age)
    if age >= 18 and age <= 21:
    # if int(age) >= 18 and int(age) <= 21:
            # 18-21 wear wristband
            print("You can enter, but need a wristband.")
    elif age >= 21:
        # 21+ drink, normal entry
        print("You can enter and can drik")
    else:
        # Too young - sorry
        print("You are too young to enter.")
else:
    print("Please enter an age: ")