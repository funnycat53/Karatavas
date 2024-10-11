"""
*Spēles pārskats*

1. Mērķis - Uzminēt nezināmu doto vārdu, ievadot burtus. 
2. Spēles gaita - Spēlētājs izvēlas vienu burtu ko minēt. Ja dotajā vārda ir tas burts, tad tas parādīsies attiecīgajā vietiņā, ja nav, 
tad tas burts neparādīsies un spēlētājam minējumu skaits samazināsies.
3. Uzvaras nosacījumi - Spēlētājs uzvar, ja uzmin doto vārdu.
4. Zaudēšanas nosacījumi - Spēlētājs zaudē, ja neuzmin doto vārdu nosacītajā minējumu skaitā.

*Komponentes*

1. Meklētā vārda izvēle - Vārdus randomā izvēlas no vārdu saraksta, kas atrodas failā vardu_saraksts.py. Vārdu izvēlas ar funkciju random.choice, 
kas importēta no "random"
2. Lietotāja informācijas ievadīšana - Līnijā 202 tiek izveidots mainīgais, kas saglabā lietotāja minēto burtu. Ja nu lietotājs ievada burtu ko jau ir 
minējis programma to lietotājam pasaka un prasa, lai ievada kādu citu burtu.
3. Iegūtās informācījas salīdzināšana ar vārdu - Darbība "if minejums in vards" pārbauda vai lietotāja minētais burts atrodas vārdā, ja tas atrodas,
tad attiecīgajā svītriņas vietā tiek ievietots minētajā vārdā. Ja minētais burts neatrodas vārdā, tad tiek izvadīts, ka minētais burts neatrodas vārdā,
nepareizo minējumu skaits palielinās un atjauninās zimējums.
4. Informācijas attēlojums - Ja burts, kas atrodas vārdā tiek uzminēts, attiecīgi tam, kurā vietā vārda tas burts atrodas, tā svītriņa tiek aizvietota
ar minēto burtu. Ja burts nav vārdā, tad tiek attēlota nākamā zīmējuma stadija.
5. Spēles beigas un atkārtošana - Ja lietotājs uzvarēja, tiek izprintēts "Apsveicu jūs uzvarējāt". Ja lietotājs zaudēja, pēdējā zīmējuma stadija tiek 
izvadīta, kā arī tiek izvadīts pareizais vārds. Visa spēle ir ielikta lielā while loop, lai to varētu atkārtot, ja lietotājs ievada "y", spēle
beidzas, ja lietotājs ievada "n", tad spēle beidzas.
"""

from vardu_saraksts import vardi
import random

zimejums = (
    """
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   ---
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /---
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /---
 | /  
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /---/
 | /     
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /---/
 | /     /
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /---/
 | /  |  /
 |    
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /---/
 | /  |  /
 |    |
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /---/
 | /  |  /
 |    |
 |   | 
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /---/
 | /  |  /
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /---/
 | /  |  /
 |    |
 |   | |
 |   | 
 |  
----------
""",
"""
 ------
 |    |
 |    O
 |  /---/
 | /  |  /
 |    |
 |   | |
 |   | |
 |  
----------
""")

def karatavas():
    while True:
        vards = random.choice(vardi)
        # print(vards) (testēšanas nolūkiem)
        minejumu_skaits = len(zimejums) - 1
        svitras = "-" * len(vards)
        nepareizie_minejumi = 0
        izmantotie_burti = [] 

        while nepareizie_minejumi < minejumu_skaits and svitras != vards:
            print(zimejums[nepareizie_minejumi])
            print("Sveicināti karātavās. Ja neuzminēsiet vārdu, zaudēsiet. Vārds ir angļu valodā.")
            print("\nJūs jau minējāt šos burtus: ", izmantotie_burti)
            print("\n", svitras)

            minejums = input("\nIevadiet savu minējumu: ")

            while minejums in izmantotie_burti:
                print("\nJūs jau minējāt šo burtu, lūdzu izvēlieties citu.")
                minejums = input("\nMiniet vēlreiz: ")


            izmantotie_burti.append(minejums)

            if minejums in vards:
                svitras_vieta = ""

                for i in range(len(vards)):
                    if vards[i] == minejums:
                        svitras_vieta += minejums
                    else:
                        svitras_vieta += svitras[i]
                svitras = svitras_vieta
            else:
                print("\nBurts,", minejums, "nav vārdā.")
                nepareizie_minejumi += 1

        if nepareizie_minejumi == minejumu_skaits:
            print(zimejums[minejumu_skaits])
            print("\nJūs zaudējāt")
            print("\nVārds bija: ", vards)
        else:
            print("\nApsveicu jūs uzvarējāt")
            print("\nVārds bija: ", vards)

        spelet_velreiz = input("\nVai vēlaties spēlēt vēlreiz? (y/n): ")
        if spelet_velreiz != 'y':
            print("\nPaldies par spēli!")
            break

karatavas()