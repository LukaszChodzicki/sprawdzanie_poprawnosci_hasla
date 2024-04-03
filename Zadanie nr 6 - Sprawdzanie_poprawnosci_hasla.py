czy_jest_cyfra = int == 0
czy_jest_znak_specjalny = int == 0
haslo = ""
while (czy_jest_cyfra == 0 or czy_jest_znak_specjalny == 0) or len(haslo) < 8:
    czy_jest_cyfra = int == 0
    czy_jest_znak_specjalny = int == 0
    print("Wprowadź hasło")
    print("Hasło powinno się składać z minimum 8 znaków, zawierać co najmniej jedną cyfrę i jeden znak specjalny")
    haslo =(input("Hasło: "))
    for i in range(len(haslo)):
        if haslo[i].isdigit() == True:
            czy_jest_cyfra += 1
        elif haslo[i].isalnum() == False:
            czy_jest_znak_specjalny += 1
        elif czy_jest_cyfra and czy_jest_znak_specjalny > 0:
            break
    if (czy_jest_cyfra == 0 or czy_jest_znak_specjalny == 0) or len(haslo) < 8:
        print("Wprowadzone hasło nie spełnia określonych kryteriów\n") 
    elif (czy_jest_cyfra >= 1 and czy_jest_znak_specjalny >= 1) and len(haslo) > 8:
        print("Wprowadzone hasło spełnia określone kryteria")
