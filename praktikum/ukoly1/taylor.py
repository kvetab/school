import math
# x na 2n lomeno n!
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
        #print(clen)
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

# Ma smysl do 12, pak uz jsou hodnoty clenu tak male, ze se hodnota nezmeni (radove 10^-16)