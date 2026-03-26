# Robot Interaction Program using OOP

class Robot:
    # Constructor (initializing robot properties)
    def __init__(self, name, model, purpose):
        self.name = name
        self.model = model
        self.purpose = purpose

    # Method to introduce the robot
    def introduce(self):
        print(f"Hello! My name is {self.name}.")
        print(f"I am a {self.model} model robot.")
        print(f"My purpose is to {self.purpose}.")

    # Method for interaction
    def interact(self):
        print("\nLet's interact!")
        user_name = input("What is your name? ")
        print(f"Nice to meet you, {user_name}!")

        feeling = input("How are you feeling today? ")
        print(f"I am glad you are feeling {feeling}!")

    # Method to perform a task
    def perform_task(self):
        print("\nI can perform some tasks:")
        print("1. Say a joke")
        print("2. Give motivation")
        
        choice = input("Choose an option (1/2): ")

        if choice == "1":
            print("Why did the robot go on vacation? Because it needed to recharge!")
        elif choice == "2":
            print("Keep going! You are doing great!")
        else:
            print("Invalid choice!")


# Creating an object of Robot class
robot1 = Robot("RoboX", "AI-2026", "assist humans and make life easier")

# Calling methods
robot1.introduce()
robot1.interact()
robot1.perform_task()