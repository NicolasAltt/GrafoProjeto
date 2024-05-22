# GrafoProjeto
## Resolução problema caminhos bicicletas de alguel em São Paulo
### Transporte Sustentável SobRodas (nome provisório da aplicação)
_____________________________________________________________________
Aluno: Nicolas Alteia Telles
RA: 10381629
_____________________________________________________________________
## Link para video explicativo:
[https://youtu.be/Z5D62DMbQpk](https://youtu.be/_HhO1ENNRv8)
## Relatório
### Explicação Proposta
O projeto foi criado para solucionar um problema de logística de outro aplicativo cujo foi criado para juntar todos os aluguéis de bicicleta em São Paulo. Ele tem como base mapear todos os pontos de bicicletas e caminhos  entre eles (para devolução e aluguel), sejam de serviços públicos como os  fornecidos pela prefeitura de SP e privadas como as fornecidas pelo banco Itaú,  para facilitar e incentivar o transporte saudável e sustentável pela cidade de São  Paulo, de forma que as bicicletas estejam melhor localizadas e o usuário consiga  acessar a mais próxima assim como as empresas posicioná-las melhor. Nesta primeira etapa foi feito um grafo baseado no arquivo  
"estações_nomes.txt" que mapea 73 pontos diferentes (com a intenção de mapear  mais no futuro), e seus respectivos caminhos entre si. Feito de forma simplificada, cada aresta e vértice corresponde ao número do primeiro vértice, portanto se o primeiro endereço da lista presente em “estações_nomes.txt” é igual ao primeiro vértice do grafo e assim por diante.
Os algoritmos foram feitos com base nos códigos presentes no site “https://www.geeksforgeeks.org/”.
### Grafo Modelado
Disponibilizado um grafo  abaixo na imagem 1(a partir do site https://graphonline.ru/pt/), juntamente com o  arquivo graphml "grafo.xml" Link para acesso:  
http://graphonline.ru/pt/?graph=LMMgxyYJerOgqbpl . 

![image](https://github.com/NicolasAltt/GrafoProjeto/assets/101070201/497d7c96-1396-4080-94bf-ec2cf17db063)
Figura 1: Grafo modelado

### Objetivos ODS
O projeto foi escolhido também com base nos seguintes objetivos ODS: 1:  "Saúde e bem-Estar", 2: "Cidades e Comunidades Sustentáveis" e, 3: "Ação contra  a mudança Global do Clima". Justificativa de cada um deles: 1: influenciar um estilo  de vida melhor, promovendo atividades físicas no dia a dia; 2: promover a ultilização  de meio de transporte sustentável; 3: A partir da utilização de um meio de transporte  que polui menos o ambiente em escala maior, cada vez menos carros e transportes  que poluem o meio ambiente serão utilizados, e uma mudança dessas em uma  metrópole, muda o ritmo que o aquecimento global ocorre. 
### Implementações
Foram implementados nessa segunda fase: Algoritmo do caixeiro viajante; funções que indicam a presença de caminhos eulerianos; função que diz que o grafo é euleriano ou não; Função que diz se existe caminho Hamiltoniano.
### Obs e bugs:
OBS:
-Os itens h e j do menu de opções estão incompletos nessa versão. Foi utilizado o arquivo indice.zip disponibilizado em aula para realizar esse  projeto, além disso foi utilizado a linguagem Python. 
-Existe um bug com o algoritmo do caixeiro viajante em que ele retorna o melhor caminho como vazio, não foi possível resolvê-lo no tempo da entrega.
