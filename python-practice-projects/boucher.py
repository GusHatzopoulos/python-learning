# Ask for age
age = int(input("How old are you? "))

# 18-21 wear wristband
if age >= 18 and age <= 21:
# if int(age) >= 18 and int(age) <= 21:
    print("You can enter, but need a wristband.")
# 21+ drink, normal entry
elif age >= 21:
    print("You can enter and can drik")
# Too young - sorry
else:
    print("You are too young to enter.")