numero = int(input('Digite um número: '))
print('=' * 15)
for c in range(0, 10):
    print('{} X {} = {}'.format(numero, c + 1, numero * (c + 1)))
print('=' * 15)

