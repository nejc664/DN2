d = {
    "mačka": "Micka",
    "pes": "Fido",
    "volk": "Rex",
    "medved": "Žan",
    "slon": "Jan",
    "žirafa": "Helga",
    "lev": "Gašper",
    "tiger": "Anže",
    "papagaj": "Črt",
    "ribica": "Elena",
    "krokodil": "Kasper",
    "zajec": "Lars",
    "kamela": "Manca" 
}

kljuci_s_Rr = []

for name, values in  d.items():
    if  'r' in values or 'R' in values:
        kljuci_s_Rr.append(name)
        
print(kljuci_s_Rr)