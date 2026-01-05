task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        msg = f"Reminder: '{task}' is a high priority task"
    case "medium":
        msg = f"Reminder: '{task}' is a medium priority task"
    case "low":
        msg = f"Note: '{task}' is a low priority task"
    case _:
        msg = f"'{task}' has an undefined priority"

if time_bound == "yes" and priority in ["high", "medium"]:
    msg += " that requires immediate attention today!"
elif time_bound == "no" and priority == "low":
    msg += ". Consider completing it when you have free time."

print(msg)
