"""
*Spēles pārskats*

1. Mērķis - Uzminēt nezināmu doto vārdu, ievadot burtus. 
2. Spēles gaita - Spēlētājs izvēlas vienu burtu ko minēt. Ja dotajā vārda ir tas burts, tad tas parādīsies attiecīgajā vietiņā, ja nav, 
tad tas burts neparādīsies un spēlētājam minējumu skaits samazināsies.
3. Uzvaras nosacījumi - Spēlētājs uzvar, ja uzmin doto vārdu.
4. Zaudēšanas nosacījumi - Spēlētājs zaudē, ja neuzmin doto vārdu nosacītajā minējumu skaitā.

*Komponentes*

1. Vārdu saraksts, izvēle - Viss saraksts ar vārdiem atrodas failā vardu_saraksts.py
"""

from vardu_saraksts import vardi
import random

vards = vardi
random.choice(vards)

minejums = input("Ievadiet savu minējumu: ")
minejumi = ""
minejumu_skaits = 8
while minejumu_skaits > 0:
    nepareizi = 0
    for burts in vards:
        if burts in minejums:
            print(burts, end="")
        else:
            print("_", end="")
            nepareizi += 1
            break
    minejumi += minejums
    if minejums not in vards:
        minejumu_skaits -= 1
        print("Vārdā neatrodas šis burts")
    if minejumu_skaits == 0:
        print("Jūs zaudējāt")
    if nepareizi == 0:
        print("Jūs uzvarējāt")
