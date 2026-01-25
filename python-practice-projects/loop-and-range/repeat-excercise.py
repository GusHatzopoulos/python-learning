# times = input("How many times do I have to tell you? ")
# times = int(times)

# for time in range(times):
#     print(f"time {time+1} CLEAN UP YOUR ROOM!")

nums = input("Enter a numbr for lucky and unlucky: ")
nums = int(nums)

for num in range(nums):
    if num == 4 or num == 13:
        state = "unlucky!"
    elif num % 2 != 0:
        state = "odd!"
    else:
        state = "even!"
    print(f"{num} is {state}")