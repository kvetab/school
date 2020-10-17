import math

count = 1
sum = 1

for i in range(63):
    count = count * 2
    sum = sum + count
print(f"{sum} zrnek ryze")
# 18446744073709551615 zrnek ryze

# Prumerne 50000 zrnek v 1 kg ryze
# 1 kg ryze -> 1.24 L
V = ((sum / 50000) * 1.24) / 1000
print(f"Mame {V} m³ ryze")
# Mame 457479253027.99695 m³ ryze
# Objem nakladniho vagonu 82,5 m³ (CD Cargo Eanos II.)
vagonu = math.ceil(V / 82.5)
print(f"Potrebujeme {vagonu} vagonu")
# Potrebujeme 5545203068 vagonu
# Delka vagonu 15740 mm -> 15.740 m
delka = vagonu * 15.74 / 1000
print(f"Celkova delka {delka} km")
# Celkova delka 87281496.29032001 km
# Obvod zemekoule 40075 km
kolem = delka / 40075
print(f"Nakladni vlak by {kolem} krat obtocil zemekouli.")
# Nakladni vlak by 2177.953743988023 krat obtocil zemekouli.

# Vzdalenost k Mesici je 384400 km
mesic = delka / 384400
print(f"Vlak by {mesic} krat dosahl na Mesic.")
# Vlak by 227.05904341914675 krat dosahl na Mesic.
# Minimalni zdalenost k Marsu je 54.6 milionu km
mars = delka / 54600000
print(f"Vlak by {mars} krat dosahl na Mars (obcas)")
# Vlak by 1.598562203119414 krat dosahl na Mars (obcas)
