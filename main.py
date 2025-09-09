from calculadora import soma

try:
  print(soma('dez', 20))
except AssertionError as e:
  print(f'Conta inválida: {e}')