times = ('Botafogo','Grêmio','Flamengo','Bragantino','Palmeiras','Fluminense','São Paulo','Internacional','Fortaleza',
         'Athletico - PR','Atlético - MG','Cruzeiro','Santos','Bahia','Corinthians','Cuiabá','Goiás','Vasco',
         'América - MG','Coritiba')
print(25 * '-')
print('Os 5 primeiros times:')

print(times[0:5])

for i in range(0,5):
    print(f'{i+1}o lugar {times[i]}')

print(25 * '-')
print('Os últimos 4 colocados:')

print(times[-4:])

colocados = len(times)
for i in range(colocados-4, colocados):
    print(times[i])

print(25 * '-')
print('Times em ordem alfabética:')
print(sorted(times))

print(25 * '-')
print(f'O Santos está em {times.index("Santos")+1}o lugar!')
