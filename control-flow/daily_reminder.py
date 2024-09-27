task = input("Enter your task: ")
priority = input("high, meduim, low: ")
time_bound = input(" is time-bound (yes or no): ")
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "meduim":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        print("invalid priority selected.")

if time_bound == "yes":        
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

print(f"Reminder: {reminder}")
