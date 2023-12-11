nome = str(input('Qual o seu nome? ')).strip()  # o strip retira espaços antes e depois

print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

# ou...

separa = nome.split()
print(separa)
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
