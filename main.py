from calculadora import soma

# print(soma(10, 20))
# print(soma(-10, 20))
# print(soma('1.5', 2.5))

try:
  print(soma('dez', 20))
except AssertionError as e:
  print(f'Conta inválida: {e}')