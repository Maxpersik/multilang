import time

start = time.time()
i = 0
N = 100000000
n = 10000000

while True:
    if i % n  == 0:
        print("=", end = "", flush = True)

    if i > N:
        break
        
    i += 1

end = time.time()
print("\nВремя выполнения:", end - start)
