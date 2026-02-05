def bfs(n, capacidade, fluxo, s, t, parent):
    
  # Fila simples sem biblioteca
    fila = [s]
    visitados = [False] * n
    visitados[s] = True
    
    while fila:
        u = fila.pop(0)
        for v in range(n):
            # Se não visitado e ainda tem capacidade residual
            if not visitados[v] and capacidade[u][v] - fluxo[u][v] > 0:
                fila.append(v)
                visitados[v] = True
                parent[v] = u
                if v == t:
                    return True
    return False
