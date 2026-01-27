# times = input("How many times do I have to tell you? ")
# times = int(times)

# for time in range(times):
#     print(f"time {time+1} CLEAN UP YOUR ROOM!")

'''
nums = input("Enter a number for lucky and unlucky: ")
nums = int(nums)

for num in range(nums):
    if num == 4 or num == 13:
        print(f"{num} is unlucky!")
    elif num % 2 == 0:
        print(f"{num} is even!")
    else:
        print(f"{num} is odd!")

for num in range(nums): 
    if num == 4 or num == 13: 
        state = "unlucky!" 
    elif num % 2 != 0:
        state = "odd!"
    else:
        state = "even!"
    print(f"{num} is {state}")
'''
msg = input("Whats the secret password? ")
while msg != "bananans":
    print("WRONG!")
    msg = input("Whats the secret password? ")
print("CORRECT!")

for num in range(1,11):
    print(num)

num = 1
while num < 11:
    print(num)
    num += 2