# Diogo Torres Correia - ist199211

tab = ((1, 0, 0), (-1, 1, 0), (1, -1, -1))


def eh_tabuleiro(tab):
    if not isinstance(tab, tuple) or len(tab) != 3:
        return False
    for row in tab:
        if not isinstance(row, tuple) or len(row) != 3:
            return False
        for cell in row:
            # Usar type em vez de isinstance para filtrar boleanos
            if type(cell) != int or not(-1 <= cell <= 1):
                return False
    return True


def eh_posicao(pos):
    # Usar type em vez de isinstance para filtrar boleanos
    if type(pos) != int:
        return False
    return 1 <= pos <= 9


def eh_coluna_ou_linha(pos):
    # Usar type em vez de isinstance para filtrar boleanos
    if type(pos) != int:
        return False
    return 1 <= pos <= 3


def eh_diagonal(pos):
    # Usar type em vez de isinstance para filtrar boleanos
    if type(pos) != int:
        return False
    return 1 <= pos <= 2


def obter_coluna(tab, col):
    if not eh_tabuleiro(tab) or not eh_coluna_ou_linha(col):
        raise ValueError('obter_coluna: algum dos argumentos e invalido')

    result = ()
    for i in range(3):
        result += (tab[i][col - 1], )
    return result


def obter_linha(tab, row):
    if not eh_tabuleiro(tab) or not eh_coluna_ou_linha(row):
        raise ValueError('obter_linha: algum dos argumentos e invalido')

    return tab[row - 1]


def obter_diagonal(tab, diag):
    if not eh_tabuleiro(tab) or not eh_diagonal(diag):
        raise ValueError('obter_diagonal: algum dos argumentos e invalido')

    result = ()
    for i in range(3):
        if diag == 1:
            result += (tab[i][i], )
        else:  # diag == 2
            result += (tab[2 - i][i], )
    return result
