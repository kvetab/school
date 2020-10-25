#!/usr/bin/env python3
import numpy as np
import time

def zarovnej(s1, s2):
    # jeden z řetězců se vyčerpal (nebo oba)
    if s1 == '':
        l = len(s2)
        return -1 * l, [['-' * l, s2]]
    elif s2 == '':
        l = len(s1)
        return -1 * l, [[s1, '-' * l]]
    # z obou řetězců ještě něco zbývá
    else:
        # možnost 1: ABC nebo ABC
        #            AEF      DEF
        m1_ohodnocení, m1_ss = zarovnej(s1[1:], s2[1:])
        # print(m1_ss)
        if s1[0] == s2[0]:
            m1_ohodnocení += 1
        else:
            m1_ohodnocení -= 1
        m1 = m1_ohodnocení, [[s1[0] + seq1, s2[0] + seq2] for seq1, seq2 in m1_ss]
        # možnost 2: ABC
        #            -DEF
        m2_ohodnocení, m2_ss = zarovnej(s1[1:], s2)
        m2 = -1 + m2_ohodnocení, [[s1[0] + seq1, '-' + seq2] for seq1, seq2 in m2_ss]
        # možnost 3: -ABC
        #            DEF
        m3_ohodnocení, m3_ss = zarovnej(s1, s2[1:])
        m3 = -1 + m3_ohodnocení, [['-' + seq1, s2[0] + seq2] for seq1, seq2 in m3_ss]
        # výběr lepší větve výpočtu
        xs = [m1, m2, m3]
        maximum = max(xs)[0]
        kandidáti = [x for x in sorted(xs) if x[0] == maximum]
        kolekce = []
        for x in kandidáti:
            kolekce.extend(x[1])
        return maximum, kolekce


def zarovnej_memo(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    # jeden z řetězců se vyčerpal (nebo oba)
    if s1 == '':
        l = len(s2)
        return -1 * l, [['-' * l, s2]]
    elif s2 == '':
        l = len(s1)
        return -1 * l, [[s1, '-' * l]]
    # z obou řetězců ještě něco zbývá
    else:
        # možnost 1: ABC nebo ABC
        #            AEF      DEF
        if tabulka[l1 - 1, l2 - 1]:
            m1_ohodnoceni, m1_ss = tabulka[l1 - 1, l2 - 1]
        else:
            m1_ohodnoceni, m1_ss = zarovnej_memo(s1[1:], s2[1:])
            tabulka[l1 - 1, l2 - 1] = (m1_ohodnoceni, m1_ss)
        # print(m1_ss)
        if s1[0] == s2[0]:
            m1_ohodnoceni += 1
        else:
            m1_ohodnoceni -= 1

        m1 = m1_ohodnoceni, [[s1[0] + seq1, s2[0] + seq2] for seq1, seq2 in m1_ss]
        # možnost 2: ABC
        #            -DEF
        if tabulka[l1 - 1, l2]:
            m2_ohodnoceni, m2_ss = tabulka[l1 - 1, l2]
        else:
            m2_ohodnoceni, m2_ss = zarovnej_memo(s1[1:], s2)
            tabulka[l1 - 1, l2] = (m2_ohodnoceni, m2_ss)
        m2 = -1 + m2_ohodnoceni, [[s1[0] + seq1, '-' + seq2] for seq1, seq2 in m2_ss]
        # možnost 3: -ABC
        #            DEF

        if tabulka[l1, l2 - 1]:
            m3_ohodnoceni, m3_ss = tabulka[l1, l2 - 1]
        else:
            m3_ohodnoceni, m3_ss = zarovnej_memo(s1, s2[1:])
            tabulka[l1, l2 - 1] = (m3_ohodnoceni, m3_ss)
        m3 = -1 + m3_ohodnoceni, [['-' + seq1, s2[0] + seq2] for seq1, seq2 in m3_ss]
        # výběr lepší větve výpočtu
        xs = [m1, m2, m3]
        maximum = max(xs)[0]
        kandidati = [x for x in sorted(xs) if x[0] == maximum]
        kolekce = []
        for x in kandidati:
            kolekce.extend(x[1])
        return maximum, kolekce
tabulka = None

def test_time(str1, str2):
    print("Zarovnavame: ", str1, str2)
    global tabulka
    tabulka = np.zeros((len(str1) + 1, len(str2) + 1), dtype=object)
    start = time.perf_counter()
    xs = zarovnej(str1, str2)
    print(xs)
    end = time.perf_counter()
    print("Bez memoizace:", end - start)

    start = time.perf_counter()
    xs = zarovnej_memo(str1, str2)
    print(xs)
    end = time.perf_counter()
    print("S memoizaci: ", end - start)
    print()


test_time('nos', 'osa')  # 0.00018; 7.7e-05
test_time('abc', 'acb')  # 0.00015; 5.9e-05
test_time('YSPTSPS', 'YSPPTSPS')    # 0.34; 0.00036
test_time("Mama mele maso", "Ema ma misu")  # 1605; 0.002


