from navegador import bfs


def edmonds_karp(n, capacidade, s, t):
    """
    Implementação do algoritmo de Edmonds-Karp para fluxo máximo.

    n: total de nós
    capacidade: matriz n x n com as capacidades das arestas
    s: nó fonte
    t: nó sumidouro
    """
    # Inicializa a matriz de fluxo com zeros
    # f(u, v) representa o fluxo atual entre os nós
    fluxo = [[0] * n for _ in range(n)]
    fluxo_maximo = 0

    # Vetor para armazenar o caminho retornado pela BFS
    parent = [-1] * n

    # Loop principal: enquanto houver um caminho de aumento da fonte ao sumidouro
    while bfs(n, capacidade, fluxo, s, t, parent):

        # 1 Encontrar o "Gargalo" (Bottleneck)
        # É a menor capacidade residual ao longo do caminho encontrado pela BFS
        caminho_fluxo = float('Inf')
        v = t
        while v != s:
            u = parent[v]
            # Capacidade residual: c_f(u, v) = c(u, v) - f(u, v)
            capacidade_residual = capacidade[u][v] - fluxo[u][v]
            caminho_fluxo = min(caminho_fluxo, capacidade_residual)
            v = u

        # 2 Atualizar o fluxo nas arestas do caminho
        v = t
        while v != s:
            u = parent[v]
            # Adiciona o fluxo no sentido direto
            fluxo[u][v] += caminho_fluxo
            # Subtrai o fluxo no sentido inverso (aresta residual/reversa)
            fluxo[v][u] -= caminho_fluxo
            v = u

        # 3. Acumula o fluxo do caminho no total
        fluxo_maximo += caminho_fluxo

    return fluxo_maximo
