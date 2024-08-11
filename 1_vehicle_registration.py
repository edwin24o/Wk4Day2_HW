# Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.
# Code Example: Provide a basic structure for the Vehicle class without methods. 
class Vehicle:
        def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner
#created function update.owner owner updating and linked it with the variable solf.owner to return new updated owner to self.owner.        
        def update_owners(self, update_owner):
              self.owner = update_owner
              print(f"Updated to {update_owner} for registration number {self.registration_number}.")
              
Tesla = Vehicle("A123", "Electric Car", "Elon Musk")
NinjaXR = Vehicle("A124", "Motorcycle", "Rod Kimble")
FordF150 = Vehicle("A125", "Truck", "Henry J")

print(f"Tesla: Reg Num: {Tesla.registration_number}, Type: {Tesla.type}, Owner: {Tesla.owner}")
print(f"NinjaXR: Reg Num: {NinjaXR.registration_number}, Type: {NinjaXR.type}, Owner: {NinjaXR.owner}")
print(f"FordF150 3: Reg Num: {FordF150.registration_number}, Type: {FordF150.type}, Owner: {FordF150.owner}")

print('='*80)
#calling back function update_owners..
Tesla.update_owners("Joe Rogan")
NinjaXR.update_owners("Evel Knievel")
FordF150.update_owners("Elvis P")

print('='*80)

print(f"This is the updated Tesla owner {Tesla.owner} with registration number: {Tesla.registration_number}")
print(f"This is the updated NinjaXR owner {NinjaXR.owner} with registration number: {NinjaXR.registration_number}")
print(f"This is the updated Tesla owner {FordF150.owner} with registration number: {FordF150.registration_number}")