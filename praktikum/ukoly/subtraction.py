# Zopakujte si výpočet s přesností na šest destinných míst z přednášky,
# tentokrát ale s výrazem ln(x+1)−lnx.

import math

def f1(x):
    partial1 = math.log(x+1)
    dig = int(math.log(partial1, 10)) + 1
    partial1 = round(x + 1, 6 - dig)
    partial2 = math.log(x)
    dig = int(math.log(partial2, 10)) + 1
    partial2 = round(x, 6 - dig)
    res = partial1 - partial2
    dig = int(math.log(res, 10)) + 1
    return round(res, 6-dig)

def f1dec(x):
    partial1 = round(math.log(x+1), 6)
    partial2 = round(math.log(x), 6)
    return round(partial1 - partial2, 6)


def f2(x):
    partial1 = x+1
    dig = int(math.log(partial1, 10)) + 1
    partial1 = round(x+1, 6-dig)
    partial2 = x
    dig = int(math.log(partial2, 10)) + 1
    partial2 = round(x, 6-dig)
    res = math.log(partial1/partial2)
    dig = int(math.log(res, 10)) + 1
    return round(res, 6-dig)

def f2dec(x):
    partial1 = round((x + 1), 6)
    partial2 = round(x, 6)
    return round(math.log(partial1/partial2), 6)

print(f1(500))
print(f2(500))
print()
print(f1dec(500))
print(f2dec(500))

