# --- WEEKLY TIME CALCULATOR ---
# This program calculates how many weeks and days are hidden in any number of days.

print("--- Welcome to Weekly Time Calculator ---")

# User input (converting text to an integer)
total_days = int(input("Enter the total number of days to analyze: "))

# Calculation using floor division (//) and modulo (%)
weeks = total_days // 7       # Calculates full weeks
remaining_days = total_days % 7  # Calculates remaining days

print("-" * 35)
print(f"Result for {total_days} days:")
print(f"-> This equals {weeks} full week(s).")
print(f"-> Plus {remaining_days} day(s) remaining.")
print("-" * 35)

if weeks > 4:
    print("That's more than a month! Great planning.")
