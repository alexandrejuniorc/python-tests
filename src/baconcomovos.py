"""
1 -  Receber um número inteiro
2 - Saber se o número é multiplo de 3 e 5:
    Bacon com ovos
3 - Saber se o número NÃO é multiplo de 3 e 5:
    Passa fome
4 - Saber se o número é multiplo de 3:
    Bacon
5 - Saber se o número é multiplo de 5:
    Ovos

"""


def bacon_com_ovos(n):
    assert isinstance(n, int), "n deve ser int"

    # Verifica se é múltiplo de 3 e 5
    # O símbolo % (módulo) retorna o resto da divisão
    if n % 3 == 0 and n % 5 == 0:
        return "Bacon com ovos"
    elif n % 3 == 0:
        return "Bacon"
    elif n % 5 == 0:
        return "Ovos"
    else:
        return "Passar fome"
