from time import sleep
for c in range(10, -1, -1):
    sleep(0.5)
    print(c)

print('BUM!!!')

# OU.......

for c in range(10, -1, -1):
    sleep(0.5)
    print(c, end=" - " if c > 0 else " - BUMMMM")
