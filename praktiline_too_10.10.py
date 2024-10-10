"""Matemaatilised tehted"""

import math
# küsime kasutajalt ujuvkomaarvu kujul kolmnurga kaatetid a ja b

# koosta muutuja a, lisa võimalus kasutajal sisestada arv, muuda see ujuvkomaarvuks

# koosta muutuja b, lisa võimalus kasutajal sisestada arv, muuda see ujuvkomaarvuks

# meie ülesandeks on leida hüpoteenus c, kolmnurga ümbermõõt ja pindala NB(vastused peavad olema ümardatud sajandikeni)

# Küsime kasutajalt kaatetid ja teisendame need ujuvkomaarvudeks

a = float(input("Sisesta kaatet a: "))
b = float(input("Sisesta kaatet b: "))

c = math.sqrt(a ** 2 + b ** 2)

p = a + b + c

s = (a * b) / 2

print(f"Kolmnurga hüpotenuus c={round(c, 2)}")
print(f"Kolmnurga ümbermõõt p={round(p, 2)}")
print(f"Kolmnurga pindala s={round(s, 2)}")




