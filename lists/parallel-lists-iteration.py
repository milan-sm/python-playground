prezimena = ['Pljakic', 'Zonfic', 'Serafimovic']
starost = [24, 34, 55]
pozicija = 0

while pozicija < len(prezimena):
    lica =  prezimena[pozicija]
    god = starost[pozicija]
    print(lica, god)
    pozicija = pozicija + 1

# Pljakic 24
# Zonfic 34
# Serafimovic 55

# Better

# prezimena = ['Pljakic', 'Zonfic', 'Serafimovic']
# starost = [24, 34, 55]

# for prezime, godina in zip(prezimena, starost):
#     print(prezime, godina)


