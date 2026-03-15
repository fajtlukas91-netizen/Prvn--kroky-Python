# --- PANCAKE CALCULATOR 3000 ---
# This script calculates the distribution of pancakes among people.

print("--- Welcome to the Pancake Calculator ---")

# 1. USER INPUTS
# Converting input (text) to integer
pancake_count = int(input("How many pancakes did you fry today? "))
people_count = int(input("How many people are sharing them? "))

print("-" * 35)

# 2. CALCULATIONS 
# How many full pancakes each person gets
per_person = pancake_count // people_count

# How many are left for the chef as a bonus (remainder)
chef_bonus = pancake_count % people_count

# 3. CONSOLE OUTPUT (using f-strings)
print(f"Baking Day Results:")
print(f"-> Each person gets: {per_person} full pancake(s)")
print(f"-> Leftover for the chef: {chef_bonus} piece(s)")

# Logical bonus
if chef_bonus > 0:
    print("\nCongratulations! As the chef, you get a bonus. Enjoy!")
else:
    print("\nPerfectly split! Next time, make more so the chef gets a bonus too.")

print("-" * 35)
