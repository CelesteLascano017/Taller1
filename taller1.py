import math

tol = 1e-1
n = 1
S = 0.0
term = 1.0

while True:
    S += term
    err = 2 - S
    if err < tol:
        break
    n += 1
    term *= 0.5
    