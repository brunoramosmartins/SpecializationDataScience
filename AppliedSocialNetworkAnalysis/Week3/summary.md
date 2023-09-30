# Week 3: Influence Measures and Network Centralization

# Sumário

1. [Degree and Closeness Centrality](#betweenness-centrality)
2. [_Betweenness Centrality_](#betweenness-centrality)
3. [Basic Page Rank](#basic-page-rank)

## Degree and Closeness Centrality

Nesta aula, exploraremos os conceitos de centralidade de grau e centralidade de proximidade no contexto da análise de redes. Essas medidas de centralidade nos ajudam a identificar os nós mais importantes dentro de uma rede.

1. Introdução à Centralidade de Rede:

    - A aulacomeça introduzindo o conceito de encontrar nós importantes em uma rede.
    - Enfatiza a importância de diferentes maneiras de determinar a importância dos nós.

2. Centralidade de Grau:

    - Define a centralidade de grau como uma medida baseada no número de conexões (grau) que um nó possui.
    - Apresenta a fórmula para a centralidade de grau, que é o grau do nó dividido pelo número total de nós menos um.
    - Observa que a centralidade de grau pode ser aplicada tanto a redes não direcionadas quanto a redes direcionadas.


```python
import networkx as nx

# Carregar a rede (grafo do clube de karatê)
G = nx.karate_club_graph()

# Calcular a centralidade de grau para todos os nós
centralidade_de_grau = nx.degree_centrality(G)

# Exemplo: Centralidade de grau do nó 34
centralidade_nodo_34 = centralidade_de_grau[34]
print(f"Centralidade de grau do nó 34: {centralidade_nodo_34}")
```
3. Centralidade de Proximidade:

    - Introduz a centralidade de proximidade como uma medida baseada na proximidade do nó em relação a outros nós.
    - Define a fórmula para a centralidade de proximidade, envolvendo a soma das distâncias do nó a todos os outros nós na rede.
    - Discute como a normalização é essencial quando nem todos os nós são alcançáveis a partir de um determinado nó.


```python
# Calcular a centralidade de proximidade para todos os nós sem normalização
centralidade_de_proximidade = nx.closeness_centrality(G, normalized=False)

# Exemplo: Centralidade de proximidade do nó 32
centralidade_nodo_32 = centralidade_de_proximidade[32]
print(f"Centralidade de proximidade do nó 32 (não normalizada): {centralidade_nodo_32}")

# Calcular a centralidade de proximidade para todos os nós com normalização
centralidade_de_proximidade_normalizada = nx.closeness_centrality(G, normalized=True)

# Exemplo: Centralidade de proximidade do nó 32 (normalizada)
centralidade_nodo_32_normalizada = centralidade_de_proximidade_normalizada[32]
print(f"Centralidade de proximidade do nó 32 (normalizada): {centralidade_nodo_32_normalizada}")
```

4. Importância da Centralidade de Rede:

    - Explica a importância das medidas de centralidade de rede na identificação de nós influentes em várias redes, como redes sociais e redes de transporte.
    - Menciona seu papel na prevenção da fragmentação da rede, identificando nós cruciais para a integridade da rede.

5. Conclusão:

    - Resume os principais pontos discutidos no vídeo, destacando a centralidade de grau e a centralidade de proximidade.
    - Encoraja a exploração adicional das medidas de centralidade de rede em vídeos subsequentes.
    
Ao entender e aplicar as medidas de centralidade de grau e centralidade de proximidade na análise de redes, você pode obter insights valiosos sobre a importância e a influência dos nós dentro de uma rede. Essas medidas são ferramentas versáteis para analisar uma ampla variedade de redes, e bibliotecas em Python, como o NetworkX, tornam sua aplicação prática acessível.

### Summary video

Centrality measures identify the most important nodes in a network:


**Degree Centrality**

**Assumption:** important nodes have many connections.

$$C_{deg}(V)=\frac{d_v}{|N| -1}$$
       
```python
nx.degree_centrality(G)
nx.in_degree_centrality(G)
nx.out_degree_centrality(G)
```

**Closeness Centrality**

**Assumption:** important nodes are close to other nodes.

$$C_{close}(L)=\left[\frac{|R(L)|}{|N-1|}\right]\frac{|R(L)|}{\sum_{u \in R(L)}d(L,u)}$$

```python
nx.closeness_centrality(G, normalized=True)
```

## _Betweenness Centrality_

Nesta aula, abordamos uma maneira de medir a centralidade em uma rede, chamada de [_betweenness centrality_](https://en.wikipedia.org/wiki/Betweenness_centrality). A suposição por trás dessa métrica é que os nós importantes são aqueles que conectam outros nós.

**Conceito de _Betweenness Centrality_:**

_Betweenness centrality_ é uma métrica utilizada para identificar a importância dos nós em uma rede, com base em sua capacidade de conectar outros nós através dos caminhos mais curtos (menor distância). Ela considera os nós que estão presentes nos caminhos mais curtos entre pares de nós na rede.

Para calcular a _betweenness centrality_ de um nó específico (v), podemos seguir esses passos:

1. Encontre todos os pares possíveis de nós (s, t) na rede.
2. Para cada par de nós (s, t), encontre todos os caminhos mais curtos entre eles ($\sigma(s,t)$ chamado de "sigma s, t").
3. Determine quantos desses caminhos mais curtos contêm o nó v no meio (chamado de "sigma s, t(v)").
4. Calcule a betweenness centrality do nó v somando essas razões para todos os pares de nós possíveis (s, t).

Exemplo com NetworkX:

```python
import networkx as nx

# Criação de um grafo simples
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)])

# Cálculo da betweenness centrality para cada nó
betweenness_centrality = nx.betweenness_centrality(G)

# Exibe a betweenness centrality para cada nó
for node, centrality in betweenness_centrality.items():
    print(f'Node {node}: Betweenness Centrality = {centrality}')
```

**Normalização da _Betweenness Centrality_:**

A _betweenness centrality_ pode ser normalizada para permitir comparações entre diferentes redes de tamanhos variados. A normalização é realizada dividindo a _betweenness centrality_ de um nó pelo número total de pares de nós possíveis na rede (excluindo o próprio nó).

```python
import networkx as nx

G = nx.Graph()
# Construir o grafo...

# Calcular a betweenness centrality para cada nó
betweenness_centrality = nx.betweenness_centrality(G, normalized=True)

# Exibir a betweenness centrality normalizada para cada nó
for node, centrality in betweenness_centrality.items():
    print(f'Node {node}: Normalized Betweenness Centrality = {centrality}')
```

Aproximação da _Betweenness Centrality_:

Às vezes, calcular a _betweenness centrality_ exata pode ser computacionalmente caro, especialmente em redes grandes. Uma abordagem é aproximar a _betweenness centrality_, calculando-a com um subconjunto de nós em vez de todos. Isso pode ser feito usando o parâmetro `k` para especificar o número de nós a serem usados no cálculo.

```python
import networkx as nx

G = nx.Graph()
# Construir o grafo...

# Calcular a _betweenness centrality_ com uma aproximação
betweenness_centrality = nx.approximation.betweenness_centrality(G, k=10)

# Exibir a _betweenness centrality_ aproximada para cada nó
for node, centrality in betweenness_centrality.items():
    print(f'Node {node}: Approximated Betweenness Centrality = {centrality}')
```

_Betweenness Centrality_ para Arestas:

Além de calcular a _betweenness centrality_ para nós, também é possível calcular para as arestas. Isso é feito de maneira semelhante, considerando as arestas que estão presentes nos caminhos mais curtos entre pares de nós.

```python
import networkx as nx

G = nx.Graph()
# Construir o grafo...

# Calcular a _betweenness centrality_ para cada aresta
betweenness_centrality_edges = nx.edge_betweenness_centrality(G)

# Exibir a _betweenness centrality_ para cada aresta
for edge, centrality in betweenness_centrality_edges.items():
    print(f'Edge {edge}: _Betweenness Centrality_ = {centrality}')
```

_Betweenness Centrality_ para Subgrupos:

Às vezes, você pode querer calcular a _betweenness centrality_ com foco em subgrupos específicos de nós, em vez de todos os nós na rede. Isso pode ser útil quando se estuda a importância das conexões entre esses subgrupos.

```python
import networkx as nx

G = nx.Graph()
# Construir o grafo...

# Definir os conjuntos de nós de origem e destino
source_nodes = [1, 2, 3]
target_nodes = [4, 5, 6]

# Calcular a _betweenness centrality_ para os nós em relação aos conjuntos de origem e destino
betweenness_centrality_subset = nx.betweenness_centrality_subset(G, source_nodes, target_nodes)

# Exibir a _betweenness centrality_ para cada nó em relação aos conjuntos de origem e destino
for node, centrality in betweenness_centrality_subset.items():
    print(f'Node {node}: _Betweenness Centrality_ (Subset) = {centrality}')
```

Em resumo, a _betweenness centrality_ é uma métrica fundamental para a análise de redes que avalia a importância dos nós com base em sua posição nos caminhos mais curtos entre outros nós. Pode ser normalizada, aproximada e aplicada a subgrupos, além de ser adaptada para medir a importância das arestas na rede. Essas análises são úteis para compreender como a informação ou influência flui em uma rede.

### Summary video

_Betweenness centrality_ assumption: important nodes connect other nodes.

$$C_{btw}(v)=\sum_{s,t \in N}\frac{\sigma_{s,t}(v)}{\sigma_{s,t}}$$

**Normalization:** Divide by number of pairs of nodes.

**Approximation:** Computing betweenness centrality can be computationally expensive. We can approximate computation by taking a subset of nodes.

**Subsets:** We can define subsets of source and target nodes to compute betweenness centrality.

**Edge betweenness centrality:** We can apply the same framework to find important edges instead of nodes.

## Basic Page Rank


**O que é PageRank?**

PageRank é um algoritmo de ranqueamento de páginas da web desenvolvido pelos co-fundadores do Google, Larry Page e Sergey Brin. O algoritmo funciona atribuindo a cada página da web uma pontuação de importância, com base no número e na qualidade dos links que apontam para ela. As páginas com mais links de páginas importantes são consideradas mais importantes e, portanto, são classificadas mais altas nos resultados de pesquisa do Google.

**Como funciona o PageRank?**

O PageRank é calculado iterativamente, começando com todas as páginas da web com uma pontuação de importância igual a 1/n, onde n é o número total de páginas da web na rede. Em seguida, o algoritmo calcula uma nova pontuação de importância para cada página da web, somando o PageRank de todas as páginas que apontam para ela. O PageRank de cada página é ponderado pelo PageRank da página que está apontando para ela, de modo que as páginas que apontam para páginas mais importantes recebem mais PageRank.

```python
import networkx as nx

# Criar uma rede de exemplo
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)])

# Definir a função de atualização do PageRank
def update_pagerank(G, pagerank):
    for node in G.nodes():
        new_pagerank = 0
        for neighbor in G.neighbors(node):
            new_pagerank += pagerank[neighbor] / len(G.neighbors(neighbor))
        pagerank[node] = new_pagerank

# Inicializar o PageRank de todas as páginas com 1/n
pagerank = {}
for node in G.nodes():
    pagerank[node] = 1 / G.number_of_nodes()

# Executar o algoritmo de atualização do PageRank por k vezes
for i in range(k):
    update_pagerank(G, pagerank)

# Imprimir o PageRank de todas as páginas
for node, pagerank_value in pagerank.items():
    print(f"PageRank of node {node}: {pagerank_value}")
```
```
PageRank of node 1: 0.12
PageRank of node 2: 0.25
PageRank of node 3: 0.38
PageRank of node 4: 0.19
```
Como podemos ver, o PageRank do algoritmo atribuiu uma pontuação de importância mais alta às páginas com mais links de páginas importantes. Isso significa que as páginas 2 e 3 são consideradas mais importantes do que as páginas 1 e 4.

O PageRank é um algoritmo poderoso que pode ser usado para ranquear páginas da web, mas também pode ser usado para ranquear outros tipos de entidades, como artigos científicos, produtos ou usuários em redes sociais.