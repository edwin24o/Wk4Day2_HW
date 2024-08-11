# Task 2: Event Management System Enhancement

# Problem Statement: Use the existing Event class by adding an attribute to keep track of the number of participants. Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.
# Code Example: Basic Event class without participant tracking.
class Event:
    def __init__(self, name, date, count= 0):
        self.name = name
        self.date = date
        self.count_participants = count # added attribute to track num of participants
    
    #Implement a method add_participant that increases the count
    def add_participants(self):     
        self.count_participants += 1

    #Implement a method get_participant_count to retrieve the current count.
    def get_participant_count(self):
        return self.count_participants

Hard_Summer = Event("Music Festival", "8-3-2023")
Nocturnal_Wonder_Land = Event("Music Festival", "9-14-2023")
Escape_Halloween = Event("Music Festival", "10-25-2023")

print(f"Hard Summer {Hard_Summer.name} on {Hard_Summer.date} had around {Hard_Summer.count_participants}.") 
print(f"Nocturnal Wonder Land {Nocturnal_Wonder_Land.name} on {Nocturnal_Wonder_Land.date} had around {Nocturnal_Wonder_Land.count_participants}.")
print(f"Escape Halloween {Escape_Halloween.name} on {Escape_Halloween.date} had around {Escape_Halloween.count_participants}.")

print('='*80)

# addding data for the code
Hard_Summer.add_participants()
Hard_Summer.add_participants()
Nocturnal_Wonder_Land.add_participants()
Nocturnal_Wonder_Land.add_participants()
Nocturnal_Wonder_Land.add_participants()
Escape_Halloween.add_participants()
Escape_Halloween.add_participants()

print('='*80)

print(f"Hard_Summer {Hard_Summer.name}: {Hard_Summer.get_participant_count()} participants. Date: {Hard_Summer.date}")

print(f"Nocturnal Wonder Land {Nocturnal_Wonder_Land.name}: {Nocturnal_Wonder_Land.get_participant_count()} participants. Date: {Nocturnal_Wonder_Land.date}")

print(f"Escape Halloween {Escape_Halloween.name}: {Escape_Halloween.get_participant_count()} participants. Date: {Escape_Halloween.date}")


