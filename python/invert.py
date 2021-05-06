from typing import Tuple
import time

def mktime():
    return round(time.time() * 1000000,3)

def xgcd(a: int, b: int) -> Tuple[int, int, int]:
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

start1 = mktime()

#x, y, z = xgcd(8877714060008732146078615118163023115262605038669773811450500348585762059351, 115792089237316195423570985008687907853269984665640564039457584007908834671663)
#print(x, y, z)

x = 8877714060008732146078615118163023115262605038669773811450500348585762059351
p = 115792089237316195423570985008687907853269984665640564039457584007908834671663

#x, y, z = xgcd(x, p)
#print(x, y, z)

y = pow(x, -1, p)

end1 = mktime()

print(y)
print("dT: ", end1-start1)
