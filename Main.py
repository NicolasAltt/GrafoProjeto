#ProjetoGrafos Versão 1
#Nicolas Alteia Telles RA: 10381629
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
      for id_vertice, dados_vertice in self.vertices.items():
          print(f"{id_vertice} - {dados_vertice['rotulo']} - Peso: {dados_vertice['peso']}")
      print("Arestas:")
      for aresta in self.arestas:
          print(f"{aresta[0]} -> {aresta[1]} - Peso: {aresta[2]}")
        
#Dois ultimos metodos a implementar.
  def verificar_conexidade(self):
      if self.tipo in [0, 1, 2, 3]:  #Grafo não direcionado
          pass 
      elif self.tipo in [4, 5, 6, 7]:  #Grafo direcionado
          pass  

  def grafo_reduzido(self):
      if self.tipo in [0, 1, 2, 3]:  #Grafo não direcionado
          pass  
      elif self.tipo in [4, 5, 6, 7]:  #Grafo direcionado
          pass  


#criar obj grafo
grafo = Grafo()

#menu de opcoes
while True:
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
  print("j) Encerrar a aplicação")

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
      break
  else:
      print("Opção inválida. Por favor, digite uma opção válida.")
