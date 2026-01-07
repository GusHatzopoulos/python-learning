ask_kilometers = input("Enter a value for kilometers to convert to miles: ")
miles = round(float(ask_kilometers) / 1.60934, 2)
#miles = round(miles, 2)

print(f"{ask_kilometers} kilometers, is: {miles} miles.")
# print(f"Entered value in kilometers, is: {round(miles, 2)} miles.")


'''
print("How many kilometers did you cycle today?")
kms = input() #get user input
miles = float(kms)/1.60934 #convert from string to float and divide
miles = round(miles, 2) #round the result
print(f"Your {kms}km ride was {miles}mi ")  

# ROUND SYNTAX:
# round(thing to round, how many decimal points)
'''