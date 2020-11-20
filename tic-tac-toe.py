# Diogo Torres Correia - ist199211

def eh_tabuleiro(tab):
    """
    Recebe um argumento de qualquer tipo e retorna True ou False,
    consoante esse argumento corresponda a um tabuleiro, isto eh,
    se eh um tuplo que contem 3 tuplos que conteem 3 posicoes.

    eh_tabuleiro: universal -> booleano
    """
    if not isinstance(tab, tuple) or len(tab) != 3:
        return False
    for linha in tab:
        if not isinstance(linha, tuple) or len(linha) != 3:
            return False
        for el in linha:
            # Usar type em vez de isinstance para filtrar boleanos
            if type(el) != int or not(-1 <= el <= 1):
                return False
    return True


def eh_inteiro_entre(valor, minimo, maximo):
    """
    Funcao auxiliar que retorna True se o valor for um inteiro
    entre min e max (inclusive)

    eh_inteiro_entre: universal X N X N -> booleano
    """
    # Usar type em vez de isinstance para filtrar boleanos
    if type(valor) != int:
        return False
    return minimo <= valor <= maximo


def eh_posicao(pos):
    """
    Recebe um argumento de qualquer tipo e retorna True ou False,
    consoante esse arugmento corresponda a uma posicao, isto eh,
    se eh um inteiro entre 1 e 9 (inclusive).

    eh_posicao: universal -> booleano
    """
    # Usar type em vez de isinstance para filtrar boleanos
    return eh_inteiro_entre(pos, 1, 9)


def eh_coluna_ou_linha(pos):
    """
    Recebe um argumento de qualquer tipo e retorna True ou False,
    consoante esse argumento corresponda ah posicao de uma linha
    ou coluna, isto eh, um inteiro entre 1 e 3 (inclusive).

    eh_coluna_ou_linha: universal -> booleano
    """
    # Usar type em vez de isinstance para filtrar boleanos
    return eh_inteiro_entre(pos, 1, 3)


def eh_diagonal(pos):
    """
    Recebe um argumento de qualquer tipo e retorna True ou False,
    consoante esse argumento corresponda ah posicao de uma diagonal,
    isto eh, um inteiro entre 1 e 2 (inclusive).

    eh_diagonal: universal -> booleano
    """
    # Usar type em vez de isinstance para filtrar boleanos
    return eh_inteiro_entre(pos, 1, 2)


def eh_jogador(jogador):
    """
    Recebe um argumento de qualquer tipo e retorna True ou False,
    consoante esse argumento corresponda a um inteiro que representa
    um jogador, isto eh, -1 ou 1.

    eh_jogador: universal -> booleano
    """
    # zero não é um jogador válido
    return eh_inteiro_entre(jogador, -1, 1) and jogador != 0


def eh_jogador_str(jogador):
    """
    Recebe um argumento de qualquer tipo e retorna True ou False,
    consoante esse argumento corresponda a uma string que representa
    um jogador, isto eh, O ou X.

    eh_jogador_str: universal -> booleano
    """
    if not isinstance(jogador, str):
        return False
    return jogador in ('X', 'O')


def eh_dificuldade(dificuldade):
    """
    Recebe um argumento de qualquer tipo e retorna True ou False,
    consoante esse argumento corresponda a uma dificuldade do jogo,
    isto eh, seja uma string igual a 'basico', 'normal' ou 'perfeito'.

    eh_dificuldade: universal -> booleano
    """
    if not isinstance(dificuldade, str):
        return False
    return dificuldade in ('basico', 'normal', 'perfeito')


def obter_coluna(tab, col):
    """
    Recebe um tabuleiro e uma posicao (inteiro) de uma coluna, e
    retorna o vetor que representa essa coluna.
    Levanta um ValueError caso algum dos arugmentos seja invalido.

    obter_coluna: tabuleiro X inteiro -> vetor
    """
    if not eh_tabuleiro(tab) or not eh_coluna_ou_linha(col):
        raise ValueError('obter_coluna: algum dos argumentos e invalido')

    return tuple(linha[col - 1] for linha in tab)


def obter_linha(tab, linha):
    """
    Recebe um tabuleiro e uma posicao (inteiro) de uma linha, e
    retorna o vetor que representa essa linha.
    Levanta um ValueError caso algum dos arugmentos seja invalido.

    obter_linha: tabuleiro X inteiro -> vetor
    """
    if not eh_tabuleiro(tab) or not eh_coluna_ou_linha(linha):
        raise ValueError('obter_linha: algum dos argumentos e invalido')

    return tab[linha - 1]


def obter_diagonal(tab, diag):
    """
    Recebe um tabuleiro e uma posicao (inteiro) de uma diagonal, e
    retorna o vetor que representa essa diagonal.
    Levanta um ValueError caso algum dos arugmentos seja invalido.

    obter_diagonal: tabuleiro X inteiro -> vetor
    """
    if not eh_tabuleiro(tab) or not eh_diagonal(diag):
        raise ValueError('obter_diagonal: algum dos argumentos e invalido')

    if diag == 1:
        return tuple(tab[i][i] for i in range(3))
    # diag == 2
    return tuple(tab[2 - i][i] for i in range(3))


def jogador_str(jogador):
    """
    Converte um inteiro que representa um jogador (-1 ou 1)
    numa string que representa um jogador (O ou X).
    O vazio (0), vai ser representado por um espaco.

    cell_str: jogador -> string
    """
    if jogador == -1:
        return 'O'
    if jogador == 1:
        return 'X'
    return ' '


def tabuleiro_str(tab):
    """
    Recebe um tabuleiro e retorna a cadeia de caracteres que o
    representa graficamente

    tabuleiro_str: tabuleiro -> cad. caracteres
    """

    if not eh_tabuleiro(tab):
        raise ValueError('tabuleiro_str: o argumento e invalido')

    resultado = ''
    for linha in range(3):
        for col in range(3):
            resultado += ' ' + jogador_str(tab[linha][col]) + ' '
            if col != 2:  # Adiciona separador exceto na ultima coluna
                resultado += '|'
        if linha != 2:  # Adiciona separador exceto na ultima linha
            resultado += '\n-----------\n'
    return resultado


def pos_humana_maquina(pos):
    """
    Funcao auxiliar que converte uma posicao humana (e.g. 1, 4, 9)
    numa posicao maquina (e.g. (0,0), (1, 0), (2, 2))

    pos_humana_maquina: posicao -> tuplo
    """
    if not eh_posicao(pos):
        raise ValueError('pos_humana_maquina: o argumento e invalido')

    pos -= 1
    return (pos // 3, pos % 3)


def pos_maquina_humana(linha, col):
    """
    Funcao auxiliar que converte uma posicao maquina
    (e.g. (0,0), (1, 0), (2, 2)) numa posicao humana (e.g. 1, 4, 9).
    As linhas e as colunas sao contadas a partir de zero.

    pos_maquina_humana: linha X coluna -> posicao
    """
    if not type(linha) == int or \
            not type(col) == int or \
            not eh_coluna_ou_linha(linha + 1) or \
            not eh_coluna_ou_linha(col + 1):
        raise ValueError('pos_maquina_humana: algum dos argumentos e invalido')

    return linha * 3 + col + 1


def eh_posicao_livre(tab, pos):
    """
    Recebe um tabuleiro e uma posicao e devolve True se a posicao
    correspondente no tabuleiro estiver livre.
    Devolve False caso contrario.

    eh_posicao_livre: tabuleiro X posicao -> booleano
    """
    if not eh_tabuleiro(tab) or not eh_posicao(pos):
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')

    linha, coluna = pos_humana_maquina(pos)
    return tab[linha][coluna] == 0


def obter_posicoes_livres(tab):
    """
    Recebe um tabuleiro e devolve o vetor ordenado com todas as posicoes
    livres do tabuleiro.

    obter_posicoes_livres: tabuleiro -> vetor
    """
    if not eh_tabuleiro(tab):
        raise ValueError('obter_posicoes_livres: o argumento e invalido')

    return tuple(pos for pos in range(1, 10) if eh_posicao_livre(tab, pos))


def jogador_ganhador(tab):
    """
    Recebe um tabuleiro e retorna o jogador vencedor (-1 ou 1).
    Se nao houver nenhum jogador que ganhou, retorna zero.

    jogador_ganhador: tabuleiro -> inteiro
    """

    def obter_todas_seccoes(tab):
        """
        Recebe um tabuleiro e retorna um tuplo que contem todas as
        possiveis seccoes de linhas, colunas ou diagonais.

        obter_todas_seccoes: tabuleiro -> tuplo de tuplos
        """
        seccoes = ((obter_linha, 3),
                   (obter_coluna, 3),
                   (obter_diagonal, 2))

        # i vai ate 3 na linha ou coluna e ate 2 na diagonal
        # executa a funcao adequada dependendo se eh linha, coluna ou diag
        return tuple(seccao[0](tab, i + 1)
                     for seccao in seccoes
                     for i in range(seccao[1]))

    def eh_tuplo_completo(tup):
        """
        Recebe uma linha/coluna/diagonal e retorna True se todos os valores
        do tuplo forem iguais.

        eh_tuplo_completo: linha/coluna/diagonal -> booleano
        """
        if not isinstance(tup, tuple) or len(tup) != 3:
            raise ValueError('eh_tuplo_completo: o argumento e invalido')

        if tup[0] == tup[1] == tup[2]:
            return tup[0]
        return 0

    if not eh_tabuleiro(tab):
        raise ValueError('jogador_ganhador: o argumento e invalido')

    for seccao in obter_todas_seccoes(tab):
        vencedor = eh_tuplo_completo(seccao)
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

    if not eh_posicao(pos) or not eh_posicao_livre(tab, pos):
        raise ValueError(
            'escolher_posicao_manual: a posicao introduzida e invalida')

    return pos


def obter_entrada(tab, pos):
    posMaquina = pos_humana_maquina(pos)
    return tab[posMaquina[0]][posMaquina[1]]


# Auxiliares estrategias de jogar auto

def escolher_lista(tab, posicoes):
    """
    Funcao auxiliar para escolher a primeira posicao vazia
    de uma lista de posicoes.
    """
    for pos in posicoes:
        if obter_entrada(tab, pos) == 0:
            return (pos, )
    return ()


def escolher_vazios(tuplo, jogador):
    """
    Recebe um tuplo e retorna um tuplo com o indice (0 a n) de
    todas as entradas nulas.
    Se alguma entrada nao nula nao pertercer ao jogador, retorna tuplo vazio.
    """
    vazios = ()
    for entrada in range(len(tuplo)):
        if tuplo[entrada] == 0:
            vazios += (entrada, )
        elif tuplo[entrada] != jogador:
            return ()
    return vazios


def converter_pos_relativa_absoluto(pos, tipo, i):
    """
        Recebe uma posicao relativa (0 a 2) e converte
        para a posicao absoluta do tabuleiro (1 a 9) consoante
        se eh linha, coluna ou diagonal
    """
    if tipo == 'linha':
        return (i * 3 + pos + 1,)
    elif tipo == 'coluna':
        return (pos * 3 + i + 1,)
    elif tipo == 'diagonal':
        if i == 0:
            return (pos_maquina_humana(pos, pos),)
        # if i == 1
        else:
            return (pos_maquina_humana(2 - pos, pos),)


def converter_seccao_relativa_absoluto(seccao, tipo, i):
    """
        Recebe uma seccao de indices relativos (0 a 2) e converte
        para as posicoes absolutas do tabuleiro (1 a 9) consoante
        se eh linha, coluna ou diagonal
    """
    res = ()
    for el in seccao:
        res += converter_pos_relativa_absoluto(el, tipo, i)
    return res


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

    seccoes = (('linha', obter_linha, 3), ('coluna', obter_coluna, 3),
               ('diagonal', obter_diagonal, 2))
    for tipo, obter_seccao, iteracoes in seccoes:
        for i in range(iteracoes):
            seccao = obter_seccao(tab, i + 1)
            vazios_rel = escolher_vazios(seccao, jogador)
            vazios_abs = converter_seccao_relativa_absoluto(
                vazios_rel, tipo, i)
            if len(vazios_abs) == 1:
                possiveis += vazios_abs

    return possiveis


def escolher_bloqueio(tab, jogador):
    # escolher_bloqueio eh o escolher_vitoria para o jogador contrario
    return escolher_vitoria(tab, -jogador)


def escolher_bifurcacao(tab, jogador):
    possiveis = ()

    for pos in range(1, 10):
        if not eh_posicao_livre(tab, pos):
            continue
        biforcacoes = obter_bifurcacoes(tab, pos)

        count = 0
        for bifurcacao in biforcacoes:
            # linha/coluna/diagonal apenas tem uma entrada do 'jogador'
            # e o resto vazio.
            # se tivesse duas entradas, a regra da vitoria impedia de chegar
            # ah bifurcacao
            if jogador in bifurcacao and -jogador not in bifurcacao:
                count += 1

        if count >= 2:
            possiveis += (pos, )

    return possiveis


def escolher_bloqueio_bifurcacao(tab, jogador):
    # Obter todas as bifurcacoes
    bifurcacoes = escolher_bifurcacao(tab, -jogador)

    # Se so houver uma bifurcacao, bloquear essa biforcacao
    # Se nao houver nenhuma, retornar um tuplo vazio, para passar
    # ah proxima estrategia
    if len(bifurcacoes) <= 1:
        return bifurcacoes

    possiveis = ()

    seccoes = (('linha', obter_linha, 3), ('coluna', obter_coluna, 3),
               ('diagonal', obter_diagonal, 2))
    for tipo, obter_seccao, iteracoes in seccoes:
        for i in range(iteracoes):
            seccao = obter_seccao(tab, i + 1)
            vazios_rel = escolher_vazios(seccao, jogador)
            vazios_abs = converter_seccao_relativa_absoluto(
                vazios_rel, tipo, i)
            if len(vazios_abs) == 2:
                vazios_bifurcacao = obter_entradas_no_tuplo(
                    vazios_abs, bifurcacoes)
                if len(vazios_bifurcacao) == 0:
                    # qualquer uma das posicoes eh segura
                    possiveis += vazios_abs
                elif len(vazios_bifurcacao) == 1:
                    # apenas uma das posicoes nao dah a vitoria ao oponente
                    possiveis += vazios_bifurcacao

    return possiveis


def escolher_centro(tab, jogador):
    if tab[1][1] == 0:
        return (5,)
    return ()


def escolher_canto_oposto(tab, jogador):
    possiveis = ()

    for diag in range(2):
        diagonal = obter_diagonal(tab, diag + 1)
        for canto in (0, 2):
            if diagonal[canto] == 0 and diagonal[2 - canto] == -jogador:
                possiveis += converter_pos_relativa_absoluto(
                    canto, 'diagonal', diag)

    return possiveis


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
        if len(pos) != 0:
            return sorted(pos)[0]

    raise ValueError('escolher_posicao_auto: tabuleiro cheio')


def jogo_do_galo(jogador, dificuldade):

    def jogador_str_para_int(jogador):
        if jogador == 'O':
            return -1
        return 1

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
    if ganhador == 0:
        return 'EMPATE'
    return jogador_str(ganhador)
