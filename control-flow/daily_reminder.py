Task = input("Enter your task: ")
Priority = input("priority(high/medium/low):")
Time_Bound = input(" is time-bound? (yes/no): ")
match Priority:
    case "high":
        reminder = f"'{Task}' is a high priority task"
    case "meduim":
        reminder = f"'{Task}' is a medium priority task"
    case "low":
        reminder = f"'{Task}' is a low priority task"
    case _:
        print("invalid priority selected.")

if Time_Bound == "yes":        
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

print(f"Reminder: {reminder}")
