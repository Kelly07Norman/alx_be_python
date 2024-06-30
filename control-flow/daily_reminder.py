# Prompt the user for the task description
task = input("Enter your task: ")

# Prompt the user for the task's priority
priority = input("Priority (high/medium/low): ").lower()

# Prompt the user if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Generate the reminder based on the priority and time-bound status
reminder = f"'{task}' is a {priority} priority task."

# Use Match Case for priority levels
match priority:
    case "high":
        reminder += " This task should be your top priority."
    case "medium":
        reminder += " This task is important but can be scheduled appropriately."
    case "low":
        reminder += " This task can be done at your leisure."

# Check if the task is time-bound
if time_bound == "yes":
    reminder += " It requires immediate attention today!"

# Print the customized reminder
print("Reminder:", reminder)