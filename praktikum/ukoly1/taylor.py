import math

def taylor(x, n):
    s = 0
    for i in range(n):
        clen = x ** (2*i) / math.factorial(i)
        s += clen
    return s

def taylor_integral(x, n):
    s = 0
    for i in range(n):
        clen = x ** (2*i + 1) / (math.factorial(i) * (2*i + 1))
        s += clen
    return s


soucet = taylor_integral(0.5, 10)
print(soucet)
soucet = taylor_integral(0.5, 11)
print(soucet)
soucet = taylor_integral(0.5, 12)
print(soucet)
soucet = taylor_integral(0.5, 13)
print(soucet)
soucet = taylor_integral(0.5, 14)
print(soucet)

# Má smysl 12 kroků, pak už jsou hodnoty členů tak malé, že se hodnota nezmění (řádově 10^-16)