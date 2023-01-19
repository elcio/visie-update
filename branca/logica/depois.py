

def compara(a, b, vira):
    """Compara o valor de duas cartas do truco."""
    valor_a = valor(a, vira)
    valor_b = valor(b, vira)
    if valor_a > valor_b:
        return 1
    elif valor_a < valor_b:
        return -1
    return 0


def valor(carta, vira):
    """Calcula o valor de uma carta do truco para comparação."""
    cartas = '4567QJKA23'
    naipes = 'OECP'
    if cartas[cartas.index(carta[0])-1] == vira:
        return naipes.index(carta[1]) + 100
    return cartas.index(carta[0])


assert compara(('5', 'O'), ('5', 'E'), '4') == -1
assert compara(('5', 'O'), ('5', 'E'), '5') == 0
assert compara(('5', 'P'), ('5', 'E'), '4') == 1
assert compara(('K', 'P'), ('3', 'E'), '5') == -1
