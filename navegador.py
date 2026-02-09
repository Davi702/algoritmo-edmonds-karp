def bfs(n, capacidade, fluxo, s, t, parent):
    """
    Realiza uma busca em largura para encontrar um caminho de aumento.

    n: Número total de nós no grafo
    capacidade: Matriz de adjacência com as capacidades originais
    fluxo: Matriz de adjacência com o fluxo atual
    s: Índice do nó fonte (source)
    t: Índice do nó sumidouro (sink)
    parent: Lista para armazenar o caminho percorrido
    """
    # Inicializa todos os nós como não visitados
    visitados = [False] * n

    # Fila para a BFS (usando lista simples para evitar bibliotecas)
    fila = [s]
    visitados[s] = True

    while fila:
        # Remove o primeiro elemento (comportamento de fila FIFO)
        u = fila.pop(0)

        for v in range(n):
            # condição mágica:
            # 1 O nó 'v' ainda não foi visitado nesta busca
            # 2 A capacidade residual (Capacidade - Fluxo) é maior que zero
            if not visitados[v] and capacidade[u][v] - fluxo[u][v] > 0:
                fila.append(v)
                visitados[v] = True
                parent[v] = u  # Registra que chegamos em 'v' vindo de 'u'

                # Se alcançamos o sumidouro, encontramos um caminho!
                if v == t:
                    return True

    # Se a fila esvaziar e não chegarmos em 't', não há mais caminhos de aumento
    return False
