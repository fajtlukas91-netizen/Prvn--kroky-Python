# Egg Carton & Packaging Calculator
# This script calculates how many cartons are needed for a total number of eggs.

total_eggs = int(input("Enter the total number of eggs: "))

carton_size = 6
total_cartons = total_eggs // carton_size
remaining_eggs = total_eggs % carton_size

print(f"\n--- Inventory Report ---")
print(f"Total eggs: {total_eggs}")
print(f"Full cartons (size {carton_size}): {total_cartons}")
print(f"Eggs remaining: {remaining_eggs}")
print(f"------------------------")
