# times = input("How many times do I have to tell you? ")
# times = int(times)

# for time in range(times):
#     print(f"time {time+1} CLEAN UP YOUR ROOM!")

nums = input("Enter a numbr for lucky and unlucky: ")
nums = int(nums)

for num in range(nums):
    if num % 2 != 0:
        print(f"{num} is odd!")
    if num % 2 == 0:
        print(f"{num} is even!")
else:
    print(f"{num} is unlucky!")