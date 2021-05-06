#!/usr/bin/python3

import sys

rA = sys.argv[1:]

S = 0
for r in rA:
    S += 1/int(r)
R = 1/S 

print("Общее сопротивление равно:", round(R, 2), "Ом")



