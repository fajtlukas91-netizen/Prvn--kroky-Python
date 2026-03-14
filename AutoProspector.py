firmy = [
    {"osoba": "Petr", "firma": "Autobazar Libeň", "obor": "prodej aut"},
    {"osoba": "Jana", "firma": "Květiny u věže", "obor": "rozvoz květin"},
    {"osoba": "Marek", "firma": "Top Truhlář", "obor": "zakázkový nábytek"},
    {"osoba": "Štěpán", "firma": "Malíři s.r.o.", "obor": "malování pokojů"},
    {"osoba": "Lukáš", "firma": "Programo", "obor": "tvorba webových stránek"}
]

for firma in firmy:
    # Vytažení dat ze slovníku do proměných
    jmeno = firma["osoba"]
    podnik = firma["firma"]
    zamereni = firma["obor"]
    
   
    uvod = f"Zdravím, {jmeno}, našel jsem vaši firmu {podnik}."
    nabidka = f"Zaujal mne váš obor {zamereni} a rád bych vám nabídl automatizaci."
    
    # 3. KROK: Vytiskni to do konzole
    print(uvod)
    print(nabidka)
    print("Ozvěte se mi, pokud máte zájem o spolupráci.")
    print("-" * 40)
