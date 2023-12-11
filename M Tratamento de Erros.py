try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que vc digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um numero por zero')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')
except Exception as erro:
    print(f'Infelizmente tivemos um problema, foi {erro.__class__} {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre.  Obrigado.')
