def soma (x, y):
  # assert serve para validar condições
  # se a condição for falsa, uma exceção do tipo AssertionError será levantada
  # Verifica se x e y são números
  assert isinstance(x, (int, float)), "x deve ser um número"
  assert isinstance(y, (int, float)), "y deve ser um número"
  return x + y