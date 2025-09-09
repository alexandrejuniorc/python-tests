def soma (x, y):
  # Docstring com exemplos de uso
  """ Soma x e y
  >>> soma(10, 20)
  30
  >>> soma(-10, 20)
  10
  >>> soma('10',20)
  Traceback (most recent call last):
  ...
  AssertionError: x precisa ser int ou float
  """
  
  # assert serve para validar condições
  # se a condição for falsa, uma exceção do tipo AssertionError será levantada
  # Verifica se x e y são números
  assert isinstance(x, (int, float)), "x precisa ser int ou float"
  assert isinstance(y, (int, float)), "y precisa ser int ou float"
  return x + y

def subtrai (x, y):
  """Subtrai x e y
  >>> subtrai(10,5)
  5
  >>> subtrai('10',5)
  Traceback (most recent call last):
  ...
  AssertionError: x precisa ser int ou float
  """
  assert isinstance(x, (int, float)), "x precisa ser int ou float"
  assert isinstance(y, (int, float)), "y precisa ser int ou float"
  return x - y

# Esse bloco só será executado se o arquivo for executado diretamente
if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)  # Executa os testes embutidos no docstring