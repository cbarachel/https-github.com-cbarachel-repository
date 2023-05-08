# Follow the instructions for how to code this application
guest_list = []
while True:
    guest_name = input("Enter a guest's name or type 'end' to stop: ")
    if guest_name.lower() == 'end':
        break
    guest_list.append(guest_name)

print("List of invited guests:")
for guest in guest_list:
    print(guest)

guest_count = len(guest_list)
food_cost = guest_count * 12
print(
    f"You have invited {guest_count} guests at a cost of ${food_cost:.2f} for food.")
