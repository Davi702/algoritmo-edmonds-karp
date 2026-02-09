from modelador import montar_grafo_eliminacao
from algoritmo import edmonds_karp

def main():
    print("--- Sistema de Eliminação de Torneios ---")
    # 1 - Receber dados dos times (Vitórias, Jogos Restantes)
    # 2 - Loop para testar cada time (ou um específico)
    # 3 - Chamar montar_grafo_eliminação
    # 4 - Chamar edmonds_karp
    # 5 - Se fluxo_maximo < total_jogos_restantes: "Eliminado!"
    
    times = [
        {'nome': 'Alvo', 'v': 80, 'r': 3, 'jogos': {}},  # ID 0
        {'nome': 'Time 1', 'v': 82, 'r': 4, 'jogos': {2: 2, 3: 2}},  # ID 1
        {'nome': 'Time 2', 'v': 82, 'r': 4, 'jogos': {1: 2, 3: 2}},  # ID 2
        {'nome': 'Time 3', 'v': 82, 'r': 4, 'jogos': {1: 2, 2: 2}}  # ID 3
    ]

    alvo_idx = 3
    print(f"Testando eliminação para: {times[alvo_idx]['nome']}")

    # 1 Monta o objeto Grafo
    grafo_obj, fluxo_req = montar_grafo_eliminacao(times, alvo_idx)

    if grafo_obj is None:
        print("Resultado: ELIMINADO (Trivialmente)")
        return

    # 2 Roda o Algoritmo usando o objeto
    s, t = 0, grafo_obj.n - 1   
    fluxo_max = edmonds_karp(grafo_obj.n, grafo_obj.capacidade, s, t)

    # 3 Veredito
    print(f"Fluxo Máximo Alcançado: {fluxo_max}")
    print(f"Fluxo Necessário para não ser eliminado: {fluxo_req}")

    if fluxo_max < fluxo_req:
        print("Resultado: MATEMATICAMENTE ELIMINADO")
    else:
        print("Resultado: AINDA POSSUI CHANCES")

if __name__ == "__main__":
    main()
    pass

if __name__ == "__main__":
    main()
