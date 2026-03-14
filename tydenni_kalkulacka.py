# --- KALKULAČKA TÝDNŮ A DNŮ ---
# Tento program vypočítá, kolik týdnů a dnů se skrývá v libovolném počtu dní.

print("--- Vítej v týdenní kalkulačce ---")

# Vstup od uživatele (převádíme text na celé číslo)
pocet_dni = int(input("Zadej celkový počet dní pro analýzu: "))

# Výpočet pomocí // a %
tydny = pocet_dni // 7      # Zjistí celé týdny
zbytek = pocet_dni % 7      # Zjistí zbývající dny

print("-" * 30)
print(f"Výsledek pro {pocet_dni} dní:")
print(f"-> To jsou přesně {tydny} celé týdny.")
print(f"-> A k tomu ti zbývá {zbytek} dní.")
print("-" * 30)

if tydny > 4:
    print("To už je víc než měsíc! Dobrá práce.")
