
# Control flow using if, elif, and else

projectStatus = "nothing" #"Suspended" #"Completed"

if projectStatus == "Completed":
    print("All team members did their jobs.")
elif projectStatus == "Suspended":
    print("Project is facing some problems.")
else:
    print("Project status is unknown!")

# Looping using While and For loops

# print index value from 1 to 10

index = 0
while index < 10:
    index += 1
    print(index)


for i in range(1,11):
    print(i)