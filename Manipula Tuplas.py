lanche = ('hamburguer','suco','pizza','pudim','batata frita')

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.count(5))
print(c.index(2,1))

pessoa = ('vitorino', '60', 'M', 99.98)
print(pessoa)
del(pessoa)

print(pessoa)
