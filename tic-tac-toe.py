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


def eh_jogador(jogador):
    # Usar type em vez de isinstance para filtrar boleanos
    if type(jogador) != int:
        return False
    return jogador == -1 or jogador == 1


def eh_jogador_str(jogador):
    if not isinstance(jogador, str):
        return False
    return jogador == 'X' or jogador == 'O'


def eh_dificuldade(dificuldade):
    if not isinstance(dificuldade, str):
        return False
    return dificuldade == 'basico' or dificuldade == 'normal' or dificuldade == 'perfeito'


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


def obter_todas_combinacoes(tab):
    """
    Obter todas as possiveis combinacoes: linha, coluna ou diagonal
    """
    resultado = ()
    combinacoes = ((obter_linha, 3), (obter_coluna, 3), (obter_diagonal, 2))
    for combinacao in combinacoes:
        # i vai ate 3 na linha ou coluna e ate 2 na diagonal
        for i in range(combinacao[1]):
            resultado += (combinacao[0](tab, i + 1), )
    return resultado


def eh_tuplo_completo(tup):
    if not isinstance(tup, tuple) or len(tup) != 3:
        raise ValueError('eh_tuplo_completo: o argumento e invalido')

    # TODO better checking
    primeiro_el = tup[0]
    for i in range(1, 3):
        if primeiro_el != tup[i]:
            return 0
    return primeiro_el


def jogador_ganhador(tab):
    if not eh_tabuleiro(tab):
        raise ValueError('jogador_ganhador: o argumento e invalido')

    for combinacao in obter_todas_combinacoes(tab):
        vencedor = eh_tuplo_completo(combinacao)
        if vencedor != 0:
            return vencedor

    return 0


def marcar_posicao(tab, jogador, pos):
    if not eh_tabuleiro(tab) or not eh_jogador(jogador) or not eh_posicao(pos):
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')

    posMaquina = pos_humana_maquina(pos)

    if tab[posMaquina[0]][posMaquina[1]] != 0:
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')

    # TODO more explicit
    linha = tab[posMaquina[0]]
    nova_linha = linha[:posMaquina[1]] + \
        (jogador, ) + linha[posMaquina[1] + 1:]

    return tab[:posMaquina[0]] + (nova_linha, ) + tab[posMaquina[0] + 1:]


def escolher_posicao_manual(tab):
    if not eh_tabuleiro(tab):
        raise ValueError('escolher_posicao_manual: o argumento e invalido')

    pos = eval(input('Turno do jogador. Escolha uma posicao livre: '))

    if not eh_posicao_livre(tab, pos):
        raise ValueError(
            'escolher_posicao_manual: a posicao introduzida e invalida')

    return pos


def obter_entrada(tab, pos):
    posMaquina = pos_humana_maquina(pos)
    return tab[posMaquina[0]][posMaquina[1]]


# Auxiliares estrategias de jogar auto

def escolher_lista(tab, posicoes):
    """
    Funcao auxiliar para escolher a primeira posicao vazia de uma lista de posicoes.
    """
    for pos in posicoes:
        if obter_entrada(tab, pos) == 0:
            return pos
    return 0


def escolher_vazios(tuplo, jogador):
    """
    Recebe um tuplo e retorna um tuplo com o indice (0 a n) de todas as entradas nulas.
    Se alguma entrada nao nula nao pertercer ao jogador, retorna tuplo vazio.
    """
    vazios = ()
    for entrada in range(len(tuplo)):
        if tuplo[entrada] == 0:
            vazios += (entrada, )
        elif tuplo[entrada] != jogador:
            return ()
    return vazios


def obter_bifurcacoes(tab, pos):
    bifurcacoes = ()

    # TODO usar row e col para identificar diagonais
    # posicoes impares teem diagonais
    if pos % 2 == 1:
        # posicoes 1, 5 e 9 teem diagonal 1
        if pos % 4 == 1:
            bifurcacoes += (obter_diagonal(tab, 1),)
        # posicoes 3, 5 e 7 teem diagonal 2
        if pos % 4 == 3 or pos == 5:
            bifurcacoes += (obter_diagonal(tab, 2),)

    (row, col) = pos_humana_maquina(pos)

    bifurcacoes += (obter_linha(tab, row + 1),)
    bifurcacoes += (obter_coluna(tab, col + 1),)

    return bifurcacoes


def escolher_todas_bifurcacoes(tab, jogador):
    possiveis = ()

    for pos in range(1, 10):
        if not eh_posicao_livre(tab, pos):
            continue
        biforcacoes = obter_bifurcacoes(tab, pos)

        count = 0
        for bifurcacao in biforcacoes:
            # linha/coluna/diagonal apenas tem uma entrada do 'jogador' e o resto vazio
            # se tivesse duas entradas, a regra da vitoria impedia de chegar ah bifurcacao
            if jogador in bifurcacao and -jogador not in bifurcacao:
                count += 1

        if count >= 2:
            possiveis += (pos, )

    return possiveis


def obter_entradas_no_tuplo(entradas, tuplo):
    """
    Recebe dois tuplos, retorna os valores de 'entradas' que estao em 'tuplo'.
    """
    resultado = ()
    for entrada in entradas:
        if entrada in tuplo:
            resultado += (entrada,)
    return resultado


# Estrategias de jogar auto

def escolher_vitoria(tab, jogador):
    """
    Edge case: duas posicoes possiveis, retornar a menor de acordo com a fig
    """
    possiveis = ()
    for row in range(3):
        linha = obter_linha(tab, row + 1)
        vazios = escolher_vazios(linha, jogador)
        if len(vazios) == 1:
            possiveis += (row * 3 + vazios[0] + 1,)

    for col in range(3):
        coluna = obter_coluna(tab, col + 1)
        vazios = escolher_vazios(coluna, jogador)
        if len(vazios) == 1:
            possiveis += (vazios[0] * 3 + col + 1,)

    for diag in range(2):
        diagonal = obter_diagonal(tab, diag + 1)
        vazios = escolher_vazios(diagonal, jogador)
        if len(vazios) == 1:
            if diag == 0:
                possiveis += (pos_maquina_humana(vazios[0], vazios[0]), )
            else:  # diag == 1
                possiveis += (pos_maquina_humana(2 - vazios[0], vazios[0]), )

    if len(possiveis) == 0:
        return 0
    return sorted(possiveis)[0]


def escolher_bloqueio(tab, jogador):
    # escolher_bloqueio eh o escolher_vitoria para o jogador contrario
    return escolher_vitoria(tab, -jogador)


def escolher_bifurcacao(tab, jogador):
    possiveis = escolher_todas_bifurcacoes(tab, jogador)

    if len(possiveis) == 0:
        return 0
    return sorted(possiveis)[0]


def escolher_bloqueio_bifurcacao(tab, jogador):
    bifurcacoes = escolher_todas_bifurcacoes(tab, -jogador)

    if len(bifurcacoes) == 0:
        return 0
    if len(bifurcacoes) == 1:
        return bifurcacoes[0]

    bifurcacoes = tuple(x - 1 for x in bifurcacoes)
    possiveis = ()

    for row in range(3):
        linha = obter_linha(tab, row + 1)
        vazios = escolher_vazios(linha, jogador)
        # nunca devera ser 1 porque escolher_vitoria ja verifica isso
        if len(vazios) == 2:
            vazios_bifurcacao = obter_entradas_no_tuplo(vazios, bifurcacoes)
            if len(vazios_bifurcacao) == 0:
                for vazio in vazios:
                    possiveis += (row * 3 + vazio + 1,)
            elif len(vazios_bifurcacao) == 1:
                possiveis += (row * 3 + vazios_bifurcacao[0] + 1,)

    for col in range(3):
        coluna = obter_coluna(tab, col + 1)
        vazios = escolher_vazios(coluna, jogador)
        # nunca devera ser 1 porque escolher_vitoria ja verifica isso
        if len(vazios) == 2:
            vazios_bifurcacao = obter_entradas_no_tuplo(vazios, bifurcacoes)
            if len(vazios_bifurcacao) == 0:
                for vazio in vazios:
                    possiveis += (vazio * 3 + col + 1,)
            elif len(vazios_bifurcacao) == 1:
                possiveis += (vazios_bifurcacao[0] * 3 + col + 1,)

    for diag in range(2):
        diagonal = obter_diagonal(tab, diag + 1)
        vazios = escolher_vazios(diagonal, jogador)
        # nunca devera ser 1 porque escolher_vitoria ja verifica isso
        if len(vazios) == 2:
            vazios_bifurcacao = obter_entradas_no_tuplo(vazios, bifurcacoes)
            if len(vazios_bifurcacao) == 0:
                for vazio in vazios:
                    if diag == 0:
                        possiveis += (pos_maquina_humana(vazio, vazio), )
                    else:  # diag == 1
                        possiveis += (pos_maquina_humana(2 - vazio, vazio), )
            elif len(vazios_bifurcacao) == 1:
                possiveis += (row * 3 + vazios_bifurcacao[0] + 1,)
                if diag == 0:
                    possiveis += (pos_maquina_humana(
                        vazios_bifurcacao[0], vazios_bifurcacao[0]), )
                else:  # diag == 1
                    possiveis += (pos_maquina_humana(2 -
                                                     vazios_bifurcacao[0], vazios_bifurcacao[0]), )

    if len(possiveis) == 0:
        return 0
    return sorted(possiveis)[0]


def escolher_centro(tab, jogador):
    if tab[1][1] == 0:
        return 5
    return 0


def escolher_canto_oposto(tab, jogador):
    possiveis = ()

    for diag in range(2):
        diagonal = obter_diagonal(tab, diag + 1)
        for canto in (0, 2):
            if diagonal[canto] == 0 and diagonal[2 - canto] == -jogador:
                if diag == 0:
                    possiveis += (pos_maquina_humana(canto, canto), )
                else:  # diag == 1
                    possiveis += (pos_maquina_humana(2 - canto, canto), )

    if len(possiveis) == 0:
        return 0
    return sorted(possiveis)[0]


def escolher_canto(tab, jogador):
    cantos = (1, 3, 7, 9)
    return escolher_lista(tab, cantos)


def escolher_lateral(tab, jogador):
    laterais = (2, 4, 6, 8)
    return escolher_lista(tab, laterais)

# (Acabar) Estrategias de jogar auto


def escolher_posicao_auto(tab, jogador, dificuldade):
    if not eh_tabuleiro(tab) or not eh_jogador(jogador) or not eh_dificuldade(dificuldade):
        raise ValueError(
            'escolher_posicao_auto: algum dos argumentos e invalido')

    if dificuldade == 'basico':
        estrategias = (escolher_centro, escolher_canto, escolher_lateral)
    if dificuldade == 'normal':
        estrategias = (escolher_vitoria, escolher_bloqueio, escolher_centro,
                       escolher_canto_oposto, escolher_canto, escolher_lateral)
    if dificuldade == 'perfeito':
        estrategias = (escolher_vitoria, escolher_bloqueio, escolher_bifurcacao, escolher_bloqueio_bifurcacao,
                       escolher_centro, escolher_canto_oposto, escolher_canto, escolher_lateral)

    for estrategia in estrategias:
        pos = estrategia(tab, jogador)
        if pos != 0:
            return pos

    raise ValueError('escolher_posicao_auto: tabuleiro cheio')


def jogador_str_para_int(jogador):
    if jogador == 'O':
        return -1
    return 1


def jogo_do_galo(jogador, dificuldade):
    if not eh_jogador_str(jogador) or not eh_dificuldade(dificuldade):
        raise ValueError('jogo_do_galo: algum dos argumentos e invalido')

    print('Bem-vindo ao JOGO DO GALO.')
    print("O jogador joga com '{}'.".format(jogador))

    humano = jogador_str_para_int(jogador)
    jogador_atual = 1

    tab = ((0, 0, 0), (0, 0, 0), (0, 0, 0))

    while (jogador_ganhador(tab) == 0 and len(obter_posicoes_livres(tab)) > 0):
        if jogador_atual == humano:
            pos_escolhida = escolher_posicao_manual(tab)
        else:
            pos_escolhida = escolher_posicao_auto(
                tab, jogador_atual, dificuldade)
            print('Turno do computador ({}):'.format(dificuldade))
        tab = marcar_posicao(tab, jogador_atual, pos_escolhida)
        print(tabuleiro_str(tab))

        # se jogador atual = -1, vai alterar para 1 e vice-versa
        jogador_atual = -jogador_atual

    ganhador = jogador_ganhador(tab)
    if ganhador == 1:
        return 'X'
    if ganhador == -1:
        return 'O'
    return 'EMPATE'


jogo_do_galo('X', 'perfeito')
