# Week 3: Influence Measures and Network Centralization

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