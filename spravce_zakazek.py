import datetime

# Databáze zakázek (seznam slovníků - v praxi se to takhle dělá)
zakazky = [
    {"klient": "Autoservis Libeň", "prace": "Webová vizitka", "cena": 4500},
    {"klient": "Pekárna u lva", "prace": "Správa Facebooku", "cena": 2000},
    {"klient": "Instalatér Marek", "prace": "Čištění databáze", "cena": 3000},
    {"klient": "kanál na YouTube", "prace": "Nahrávání videí", "cena": 7000},
    {"klient": "E-shop s oblečením", "prace": "SEO optimalizace", "cena": 3500 }
]

def vytvor_report(seznam_zakazek):
    datum = datetime.date.today()
    soubor_jmeno = f"report_prijmu_{datum}.txt"
    
    celkovy_prijem = 0
    
    with open(soubor_jmeno, "w", encoding="utf-8") as f:
        f.write(f"--- FINANČNÍ REPORT ZE DNE {datum} ---\n\n")
        
        for z in seznam_zakazek:
            radek = f"Klient: {z['klient']:20} | Práce: {z['prace']:20} | Cena: {z['cena']} Kč\n"
            f.write(radek)
            celkovy_prijem += z['cena']
            
        f.write(f"\n" + "-"*50 + "\n")
        f.write(f"CELKOVÝ POTENCIÁLNÍ VÝDĚLEK: {celkovy_prijem} Kč\n")
        f.write(f"CHYBÍ DO CÍLE (20 000 Kč): {20000 - celkovy_prijem} Kč\n")

    return soubor_jmeno, celkovy_prijem

# Spuštění programu
soubor, castka = vytvor_report(zakazky)
print(f"Hotovo! Report vytvořen v souboru: {soubor}")
print(f"Aktuálně máš rozpracováno za {castka} Kč.")
