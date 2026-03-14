# --- MOJE PRVNÍ APLIKACE V PYTHONU: PALACINKÁTOR 3000 ---
# Tento skript vypočítá suroviny a rozdělení palačinek mezi lidi.

print("--- Vítej v Palacinkátoru ---")

# 1. VSTUPY OD UŽIVATELE
#input() vrací text, proto ho musíme převést na int (celé číslo)
pocet_palacinek = int(input("Kolik palačinek jsi dneska nasmažil? "))
pocet_lidi = int(input("Mezi kolik lidí je chceš rozdělit? "))

print("-" * 30)

# 2. VÝPOČTY 
# Kolik dostane každý celých kusů
na_osobu = pocet_palacinek // pocet_lidi

# Kolik zbude pro kuchaře jako bonus (zbytek po dělení)
bonus_pro_kuchare = pocet_palacinek % pocet_lidi

# 3. VÝSTUP DO KONZOLE (f-stringy pro hezký text)
print(f"Výsledek dnešního pečení:")
print(f"-> Každý dostane: {na_osobu} celé palačinky")
print(f"-> Pro tebe (pro kuchaře) zbylo: {bonus_pro_kuchare} ks")

# Malý logický bonus (if/else)
if bonus_pro_kuchare > 0:
    print("\nGratuluji! Jako kuchař máš něco navíc. Dobrou chuť!")
else:
    print("\nRozděleno přesně! Příště jich musíš udělat víc, aby zbylo na kuchaře.")

print("-" * 30)
