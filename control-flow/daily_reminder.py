task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
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