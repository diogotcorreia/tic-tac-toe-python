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


def cell_str(cell):
    if cell == -1:
        return 'O'
    if cell == 1:
        return 'X'
    return ' '


def tabuleiro_str(tab):
    if not eh_tabuleiro(tab):
        raise ValueError('tabuleiro_str: o argumento e invalido')

    result = ''
    for row in range(3):
        for col in range(3):
            result += ' ' + cell_str(tab[row][col]) + ' '
            if col != 2:
                result += '|'
        if row != 2:
            result += '\n-----------\n'
    return result


def pos_humana_maquina(pos):
    """
    Converte uma posicao humana (e.g. 1, 4, 9) numa posicao
    maquina (e.g. (0,0), (1, 0), (2, 2))
    """
    if not eh_posicao(pos):
        raise ValueError('pos_humana_maquina: o argumento e invalido')

    pos -= 1
    return (pos // 3, pos % 3)


def pos_maquina_humana(row, col):
    """
    Converte uma posicao maquina (e.g. (0,0), (1, 0), (2, 2))
    numa posicao humana (e.g. 1, 4, 9)
    """
    # TODO improve checking
    if not eh_coluna_ou_linha(row + 1) or not eh_coluna_ou_linha(col + 1):
        raise ValueError('pos_maquina_humana: algum dos argumentos e invalido')

    return row * 3 + col + 1


def eh_posicao_livre(tab, pos):
    if not eh_tabuleiro(tab) or not eh_posicao(pos):
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')

    posMaquina = pos_humana_maquina(pos)
    return tab[posMaquina[0]][posMaquina[1]] == 0


def obter_posicoes_livres(tab):
    if not eh_tabuleiro(tab):
        raise ValueError('obter_posicoes_livres: o argumento e invalido')

    # TODO: consider using eh_posicao_livre
    result = ()
    for row in range(3):
        for col in range(3):
            if tab[row][col] == 0:
                result += (pos_maquina_humana(row, col), )
    return result
