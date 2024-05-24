# ProjetoGrafos Versão 2
#Implementaçao de metodos e algoritmos para solucionar o problema dos caminhos de bibcletas de aluguel em Sao Paulo
# Nicolas Alteia Telles RA: 10381629
import itertools
from collections import defaultdict

class Grafo:
    def __init__(self):
        self.tipo = None
        self.vertices = {}
        self.arestas = []

    def ler_grafo(self, nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            self.tipo = int(arquivo.readline().strip())
            num_vertices = int(arquivo.readline().strip())
            for _ in range(num_vertices):
                linha = arquivo.readline().strip().split()
                if len(linha) >= 3:
                    id_vertice = int(linha[0])
                    rotulo_vertice = linha[1]
                    peso_vertice = float(linha[2])
                    self.vertices[id_vertice] = {'rotulo': rotulo_vertice, 'peso': peso_vertice}

            num_arestas = int(arquivo.readline().strip())
            for _ in range(num_arestas):
                linha = arquivo.readline().strip().split()
                if len(linha) >= 3:
                    id_origem = int(linha[0])
                    id_destino = int(linha[1])
                    peso_aresta = float(linha[2])
                    self.arestas.append((id_origem, id_destino, peso_aresta))

    def gravar_grafo(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(str(self.tipo) + '\n')
            arquivo.write(str(len(self.vertices)) + '\n')
            for id_vertice, dados_vertice in self.vertices.items():
                linha = f"{id_vertice} {dados_vertice['rotulo']} {dados_vertice['peso']}\n"
                arquivo.write(linha)

            arquivo.write(str(len(self.arestas)) + '\n')
            for aresta in self.arestas:
                linha = f"{aresta[0]} {aresta[1]} {aresta[2]}\n"
                arquivo.write(linha)

    def inserir_vertice(self, id_vertice, rotulo, peso):
        if id_vertice not in self.vertices:
            self.vertices[id_vertice] = {'rotulo': rotulo, 'peso': peso}

    def inserir_aresta(self, id_origem, id_destino, peso):
        if (id_origem, id_destino, peso) not in self.arestas:
            self.arestas.append((id_origem, id_destino, peso))

    def remover_vertice(self, id_vertice):
        if id_vertice in self.vertices:
            self.vertices.pop(id_vertice)
            self.arestas = [(origem, destino, peso) for origem, destino, peso in self.arestas
                            if origem != id_vertice and destino != id_vertice]

    def remover_aresta(self, id_origem, id_destino):
        self.arestas = [(origem, destino, peso) for origem, destino, peso in self.arestas
                        if origem != id_origem or destino != id_destino]

    def mostrar_conteudo_arquivo(self):
        print("Tipo do Grafo:", self.tipo)
        print("Vértices:")
        for id_vertice, dados_vertice in self.vertices.items():
            print(f"{id_vertice} - {dados_vertice['rotulo']} - Peso: {dados_vertice['peso']}")
        print("Arestas:")
        for aresta in self.arestas:
            print(f"{aresta[0]} -> {aresta[1]} - Peso: {aresta[2]}")

    def mostrar_grafo(self):
        print("Vértices:")
        count_vertices = 0
        for id_vertice, dados_vertice in self.vertices.items():
            print(f"{id_vertice} - {dados_vertice['rotulo']} - Peso: {dados_vertice['peso']}")
            count_vertices += 1
        print(f"Total de Vértices: {count_vertices}")

        print("Arestas:")
        count_arestas = 0
        for aresta in self.arestas:
            print(f"{aresta[0]} -> {aresta[1]} - Peso: {aresta[2]}")
            count_arestas += 1
        print(f"Total de Arestas: {count_arestas}")

    def caixeiro_viajante(self):
        vertices = list(self.vertices.keys())
        if len(vertices) < 2:
            return 0, []

        def peso_aresta(v1, v2):
            for (origem, destino, peso) in self.arestas:
                if (origem == v1 and destino == v2) or (origem == v2 and destino == v1):
                    return peso
            return float('inf')

        min_peso = float('inf')
        melhor_caminho = []
        for permutacao in itertools.permutations(vertices):
            peso_total = 0
            for i in range(len(permutacao) - 1):
                peso = peso_aresta(permutacao[i], permutacao[i + 1])
                if peso == float('inf'):
                    break  #se não há aresta, interrompe esta permutação
                peso_total += peso
            else:
                #adiciona a volta ao ponto inicial
                peso = peso_aresta(permutacao[-1], permutacao[0])
                if peso != float('inf'):
                    peso_total += peso
                    if peso_total < min_peso:
                        min_peso = peso_total
                        melhor_caminho = permutacao

        return min_peso, melhor_caminho
    def grau_vertice(self, id_vertice):
        grau = 0
        for origem, destino, _ in self.arestas:
            if origem == id_vertice or destino == id_vertice:
                grau += 1
        return grau

    def coloracao_minima(self):
        cores = defaultdict(int)
        for vertice in self.vertices.keys():
            vizinhos = set()
            for origem, destino, _ in self.arestas:
                if origem == vertice:
                    vizinhos.add(destino)
                elif destino == vertice:
                    vizinhos.add(origem)
            cor = 1
            while any(cores[vizinho] == cor for vizinho in vizinhos):
                cor += 1
            cores[vertice] = cor
        return max(cores.values())

    def grafo_euleriano(self):
        for vertice in self.vertices.keys():
            if self.grau_vertice(vertice) % 2 != 0:
                return False
        return True

    def percurso_euleriano(self):
        if not self.grafo_euleriano():
            return False
        return len(self.arestas) > 0

    def ciclo_hamiltoniano(self):
        if len(self.vertices) < 3:
            return False
        for vertice in self.vertices:
            visitados = {vertice}
            if self._hamiltoniano_recursivo(vertice, visitados):
                    return True
            return False

    
    def _hamiltoniano_recursivo(self, vertice_atual, visitados):
        if len(visitados) == len(self.vertices):
            for origem, destino, _ in self.arestas:
                if origem == vertice_atual and destino == list(visitados)[0]:
                    return True
            return False
        for origem, destino, _ in self.arestas:
            if origem == vertice_atual and destino not in visitados:
                visitados.add(destino)
                if self._hamiltoniano_recursivo(destino, visitados):
                    return True
                visitados.remove(destino)
            elif destino == vertice_atual and origem not in visitados:
                visitados.add(origem)
                if self._hamiltoniano_recursivo(origem, visitados):
                    return True
                visitados.remove(origem)
        return False


# criar obj grafo
grafo = Grafo()
print("\n Transporte Sustentável SobRodas")
print("\n Resoluçao do problema de Caminhos Sustentavel Bicicletas Sao paulo")
# menu de opcoes
while True:
    print("\nCaminho Sustentavel Bicicletas Sao paulo")
    print("\nMenu de Opções:")
    print("a) Ler dados do arquivo grafo.txt")
    print("b) Gravar dados no arquivo grafo.txt")
    print("c) Inserir vértice")
    print("d) Inserir aresta")
    print("e) Remover vértice")
    print("f) Remover aresta")
    print("g) Mostrar conteúdo do arquivo")
    print("h) Mostrar grafo")
    print("i) Apresentar a conexidade do grafo e o reduzido")
    print("j) Resolver problema do caixeiro viajante")
    print("k) Mostrar numero colarao de vertices")
    print("l) Mostrar se o grafo é euleriano:o")
    print("m) Mostrar se o grafo possui percurso euleriano")
    print("n) Mostrar se o grafo possui ciclo hamiltoniano")
    print("o) Encerrar a aplicação")

    opcao = input("Digite a opção desejada: ").strip().lower()

    if opcao == 'a':
        grafo.ler_grafo('grafo.txt')
    elif opcao == 'b':
        grafo.gravar_grafo('grafo.txt')
    elif opcao == 'c':
        id_vertice = int(input("Digite o ID do vértice: "))
        rotulo = input("Digite o rótulo do vértice: ")
        peso = float(input("Digite o peso do vértice: "))
        grafo.inserir_vertice(id_vertice, rotulo, peso)
    elif opcao == 'd':
        id_origem = int(input("Digite o ID do vértice de origem: "))
        id_destino = int(input("Digite o ID do vértice de destino: "))
        peso = float(input("Digite o peso da aresta: "))
        grafo.inserir_aresta(id_origem, id_destino, peso)
    elif opcao == 'e':
        id_vertice = int(input("Digite o ID do vértice a ser removido: "))
        grafo.remover_vertice(id_vertice)
    elif opcao == 'f':
        id_origem = int(input("Digite o ID do vértice de origem da aresta a ser removida: "))
        id_destino = int(input("Digite o ID do vértice de destino da aresta a ser removida: "))
        grafo.remover_aresta(id_origem, id_destino)
    elif opcao == 'g':
        grafo.mostrar_conteudo_arquivo()
    elif opcao == 'h':
        grafo.mostrar_grafo()
    elif opcao == 'i':
        grafo.verificar_conexidade()
        grafo.grafo_reduzido()
    elif opcao == 'j':
        custo, caminho = grafo.caixeiro_viajante()
        print("Custo mínimo:", custo)
        print("Melhor caminho:", " -> ".join(map(str, caminho)))
    elif opcao == 'k':
        print("Número mínimo de cores para colorir os vértices:", grafo.coloracao_minima())
    elif opcao == 'l':
        print("O grafo é euleriano:", grafo.grafo_euleriano())
    elif opcao == 'm':
        print("O grafo possui percurso euleriano:", grafo.percurso_euleriano())
    elif opcao == 'n':
        print("O grafo possui ciclo hamiltoniano:", grafo.ciclo_hamiltoniano())
    elif opcao == 'o':
        break
    else:
        print("Opção inválida. Por favor, digite uma opção válida.")
