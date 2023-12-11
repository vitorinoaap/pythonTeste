'''
num = int(input('Digite o número para calcular seu fatorial: '))
fat = num

print('Fatorial de {}! = '.format(num), end='')
while num > 0:
    print(num, end=' x ' if num - 1 > 0 else ' = ')
    num -= 1
    if num > 0:
        fat = fat * num
print(fat)
'''

num = int(input('Digite o número para calcular seu fatorial: '))
fat = num
print('Fatorial de {}! = '.format(num), end='')
for c in range(num, 0, -1):
    print(num, end=' x ' if num - 1 > 0 else ' = ')
    num -= 1
    if num > 0:
        fat = fat * num
print(fat)