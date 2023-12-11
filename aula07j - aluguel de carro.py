print()

dias = int(input('Quantos dias de aluguel? '))

kms = float(input('Quantos kms rodou? '))

total = (dias * 60) + (kms * 0.15)

print('Sabendo que cada dia custa R$60,00 e cada km custa R$0,15, vc deverá pagar R${:.2f}'.format(total))
