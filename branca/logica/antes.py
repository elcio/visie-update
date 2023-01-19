

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
    if vira == '4' and carta[0] == '5':
        return valor_naipe(carta[1])
    if vira == '5' and carta[0] == '6':
        return valor_naipe(carta[1])
    if vira == '6' and carta[0] == '7':
        return valor_naipe(carta[1])
    if vira == '7' and carta[0] == 'Q':
        return valor_naipe(carta[1])
    if vira == 'Q' and carta[0] == 'J':
        return valor_naipe(carta[1])
    if vira == 'J' and carta[0] == 'K':
        return valor_naipe(carta[1])
    if vira == 'K' and carta[0] == 'A':
        return valor_naipe(carta[1])
    if vira == 'A' and carta[0] == '2':
        return valor_naipe(carta[1])
    if vira == '2' and carta[0] == '3':
        return valor_naipe(carta[1])
    if vira == '3' and carta[0] == '4':
        return valor_naipe(carta[1])
    if carta[0] == '4':
        return 0
    if carta[0] == '5':
        return 1
    if carta[0] == '6':
        return 2
    if carta[0] == '7':
        return 3
    if carta[0] == 'Q':
        return 4
    if carta[0] == 'J':
        return 5
    if carta[0] == 'K':
        return 6
    if carta[0] == 'A':
        return 7
    if carta[0] == '2':
        return 8
    if carta[0] == '3':
        return 9


def valor_naipe(naipe):
    """Calcula o valor de uma manilha para comparação"""
    if naipe == 'O':
        return 100
    elif naipe == 'E':
        return 200
    elif naipe == 'C':
        return 300
    elif naipe == 'P':
        return 400


assert compara(('5', 'O'), ('5', 'E'), '4') == -1
assert compara(('5', 'O'), ('5', 'E'), '5') == 0
assert compara(('5', 'P'), ('5', 'E'), '4') == 1
assert compara(('K', 'P'), ('3', 'E'), '5') == -1
