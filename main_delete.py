#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.file_storage import FileStorage
from models.state import State
from models.city import City
fs = FileStorage()

# All States
all_states = fs.all(City)
print("All City: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Create a new State
new_state = City()
new_state.name = "Imo"
fs.new(new_state)
fs.save()
print("New City: {}".format(new_state))

# All States
all_states = fs.all(City)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Create another State
another_state = City()
another_state.name = "Lagos"
fs.new(another_state)
fs.save()
print("AnotherCity: {}".format(another_state))

# All States
all_states = fs.all(City)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])        

# Delete the new State
fs.delete(new_state)

# All States
all_states = fs.all(City)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

