import csv
villains = [
    ["Doctor", "No"],
    ["Rosa", "Klebb"],
    ["Mister", "Big"],
    ["Auric", "GoldFinger"],
    ["Ernst", "Blofeld"],
]

with open('vlllains', 'wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(villains)