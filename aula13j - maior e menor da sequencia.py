"""Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos."""
pesomaior = 0
pesomenor = 10000

for c in range(1,6):
    peso = float(input(f'Qual o peso da {c}a pessoa? '))
    if peso > pesomaior:
        pesomaior = peso
    if peso < pesomenor:
        pesomenor = peso

print('O peso maior foi {}kg e o menor foi {}kg.'.format(pesomaior, pesomenor))
