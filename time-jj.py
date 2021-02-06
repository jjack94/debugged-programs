# asks for current time and how many hours user wants to wait in 24 hour time (0-23)
# outputs time calculated after waiting
# debugged and edited by James Jack 2/6/21

currentTimeStr = input("What is the current time (in hours 0-23)?")
waitTimeStr = input("How many hours do you want to wait?")

currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)

FinalTimeInt = currentTimeInt + waitTimeInt

FinalOutput = FinalTimeInt % 24
print("Your time after waiting is: ", FinalOutput)
