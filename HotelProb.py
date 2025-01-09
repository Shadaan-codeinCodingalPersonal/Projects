# There are x children from a school. They can each stay in rooms of 5 or rooms of 6.
# There are 60 rooms in the hostel available. There have to be more rooms of 5 than rooms of 6.

children = int(input("How many children are there? "))
roomcount_total = 0
results = []

# Iterate over possible numbers of rooms of 5
for roomcount_five in range(1, 61):  # At least 1 room of 5
    # Calculate remaining children after assigning rooms of 5
    remaining_children = children - (roomcount_five * 5)
    
    if remaining_children < 0:
        break  # No need to continue if we exceed the total number of children

    # Check if the remaining children can be evenly divided into rooms of 6
    if remaining_children % 6 == 0:
        roomcount_six = remaining_children // 6
        roomcount_total = roomcount_five + roomcount_six

        # Ensure total rooms do not exceed 60 and rooms of 5 are more than rooms of 6
        if roomcount_total <= 60 and roomcount_five > roomcount_six:
            print(f"There is a possible combination of {roomcount_five} rooms of 5 and {roomcount_six} rooms of 6.")
            results.append([roomcount_five, roomcount_six])

# If no valid combinations were found
if not results:
    print("No possible combination.")