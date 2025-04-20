n1 = int(input('digite um numero: '))
n2 = input('digite outro valor: ')

s = n1 + int(n2)

print(f'a soma entre {n1} e {n2} vale {s}')

print(f" o tipo primitivo da soma é: {s.__class__.__name__}")
print(f" o tipo primitivo da soma é: {type(s.__class__.__name__)}")
