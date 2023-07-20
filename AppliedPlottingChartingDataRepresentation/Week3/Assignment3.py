#!/usr/bin/env python
# coding: utf-8

# # Assignment 3 - Building a Custom Visualization
# 
# Nesta tarefa, você deve escolher __uma__ das opções apresentadas abaixo e enviar um visual, bem como seu código-fonte para avaliação por pares. Os detalhes de como você resolve a tarefa dependem de você, embora sua tarefa deva usar matplotlib para que seus colegas possam avaliar seu trabalho. As opções diferem no nível de desafio, mas não há notas associadas ao nível de desafio escolhido. No entanto, seus colegas serão solicitados a garantir que você tenha pelo menos uma qualidade mínima para uma determinada técnica para ser aprovado. Implemente a técnica totalmente (ou exceda-a!) e você poderá obter notas completas para a tarefa.
# 
# Ferreira, N., Fisher, D., & Konig, A. C. (2014, April). [Sample-oriented task-driven visualizations: allowing users to make better, more confident decisions.](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/Ferreira_Fisher_Sample_Oriented_Tasks.pdf) 
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (pp. 571-580). ACM. ([video](https://www.youtube.com/watch?v=BI7GAs-va-Q))
# 
# Neste [paper](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/Ferreira_Fisher_Sample_Oriented_Tasks.pdf) os autores descrevem os desafios que os usuários enfrentam ao tentar fazer julgamentos sobre dados probabilísticos gerados por meio de amostras. Como exemplo, eles olham para um gráfico de barras de quatro anos de dados (replicado abaixo na Figura 1). Cada ano tem um valor do eixo y, que é derivado de uma amostra de um conjunto de dados maior. Por exemplo, o primeiro valor pode ser o número de votos em um determinado distrito ou disputa para 1992, com a média em torno de 33.000. Além disso, é plotado o intervalo de confiança de 95% para a média (consulte as palestras do boxplot para obter mais informações e o parâmetro yerr dos gráficos de barras).
# 
# <br>
# <img src="assets/Assignment3Fig1.png" alt="Figure 1" style="width: 400px;"/>
# <h4 style="text-align: center;" markdown="1">  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Figure 1 from (Ferreira et al, 2014).</h4>
# 
# <br>
# 
# Um desafio que os usuários enfrentam é que, para um determinado valor do eixo y (por exemplo, 42.000), é difícil saber quais valores do eixo x têm maior probabilidade de serem representativos, porque os níveis de confiança se sobrepõem e suas distribuições são diferentes (os comprimentos das barras do intervalo de confiança são desiguais). Uma das soluções que os autores propõem para esse problema (Figura 2c) é permitir que os usuários indiquem o valor do eixo y de interesse (por exemplo, 42.000) e, em seguida, desenhem uma linha horizontal e barras coloridas com base nesse valor. Assim, as barras podem ser coloridas de vermelho se estiverem definitivamente acima desse valor (dado o intervalo de confiança), azuis se estiverem definitivamente abaixo desse valor ou brancas se contiverem esse valor.
# 
# 
# <br>
# <img src="assets/Assignment3Fig2c.png" alt="Figure 1" style="width: 400px;"/>
# <h4 style="text-align: center;" markdown="1">  Figure 2c from (Ferreira et al. 2014). Note that the colorbar legend at the bottom as well as the arrows are not required in the assignment descriptions below.</h4>
# 
# <br>
# <br>
# 
# **Opção mais fácil:** Implemente a coloração da barra conforme descrito acima - uma escala de cores com pelo menos três cores (por exemplo, azul, branco e vermelho). Suponha que o usuário forneça o valor do eixo y de interesse como um parâmetro ou variável.
# 
# **Opção mais difícil:** Implemente a coloração da barra conforme descrito no artigo, onde a cor da barra é realmente baseada na quantidade de dados cobertos (por exemplo, um gradiente variando de azul escuro para a distribuição certamente abaixo deste eixo y , para branco se o valor certamente estiver contido, para vermelho escuro se o valor certamente não estiver contido, pois a distribuição está acima do eixo).
# 
# **Opção ainda mais difícil:** Adicione interatividade à anterior, que permite ao usuário clicar no eixo y para definir o valor de interesse. As cores da barra devem mudar de acordo com o valor selecionado pelo usuário.
# 
# **Opção mais difícil:** permite que o usuário defina interativamente um intervalo de valores y nos quais esteja interessado e recolora com base nisso (por exemplo, uma faixa do eixo y, consulte o artigo para obter mais detalhes).
# 
# ---
# 
# *Note: The data given for this assignment is not the same as the data used in the article and as a result the visualizations may look a little different.*

# In[1]:


# Use the following data for this assignment:

import pandas as pd
import numpy as np

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])
df


# In[12]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import matplotlib.colors as col
import matplotlib.cm as cm
import seaborn as sns

# %matplotlib notebook


# In[13]:


df_mean = df.mean(axis=1)
df_std = df.std(axis=1)


# In[14]:


n = df.shape[1]
n


# In[15]:


y = np.mean(df_mean.values)
y


# O erro padrão é uma medida de quão precisa é a estimativa da média. Quanto maior o erro padrão, menos preciso é a estimativa. O nível de confiança do intervalo de confiança é a probabilidade de que a verdadeira média do conjunto de dados esteja dentro do intervalo de confiança.
# 
# Para calcular o erro padrão `yerr` temos:
# 
# - `df_std` é o desvio padrão do conjunto de dados;
# - `n` é o número de observações no conjunto de dados;
# - `st.norm.ppf` é uma função que retorna o ponto percentil da distribuição padrão;
# - `1 - 0.05 / 2` é o nível de confiança do intervalo de confiança. 

# In[43]:


# Compute the 95% confidence intervals
yerr = df_std / np.sqrt(n) * st.norm.ppf(1 - 0.05 / 2)
conf_ints = [
    st.norm.interval(confidence=0.95, loc=mu, scale=se)
    for mu, se in zip(df_mean, df_std / np.sqrt(n))
]


# In[44]:


conf_ints


# In[45]:


# Compute the probablility of the mean > y for each column
def compute_probs(y, conf_int):
    
    # Mínimo do intervalo maior que a média
    if y < np.min(conf_int): 
        result = 1.0
    # Máximo do intervalor menor que a média
    elif y > np.max(conf_int): 
        result = 0.0
    # Média contida no intervalo
    else: 
        result = (np.max(conf_int) - y) / (np.max(conf_int) - np.min(conf_int))
    
    return result


# In[46]:


# Compute probabilities
probs = [compute_probs(y, ci) for ci in conf_ints]


# In[47]:


# Setup the colormap
cc = ['seismic', 'bwr', 'coolwarm', 'RdBu', 'PRGn', 'PiYG']
cmap = cm.get_cmap(cc[5])
cpick = cm.ScalarMappable(cmap=cmap, norm=col.Normalize(vmin=0, vmax=1.0))
cpick.set_array([])


# In[55]:


# Setup the plot
plt.figure()
bars = plt.bar(
    range(len(df)),
    df_mean,
    #                width=1,
    edgecolor='lightgray',
    yerr=yerr,
    alpha=0.8,
    color=cpick.to_rgba(probs),
    capsize=7)

# Add the colorbar
ax = plt.subplot(111)
cbar = plt.colorbar(cpick, ax=ax, orientation="vertical")

# Turn off some plot rectangle spines
[plt.gca().spines[loc].set_visible(False) for loc in ['top', 'right']]

# Add the horizontal line
hoz_line = plt.axhline(y=y, color='gray', linewidth=1, linestyle='--')

# Set ticks and labels
plt.title('Easiest option')

plt.xlabel('Year')
plt.ylabel('Value')

plt.xticks(range(len(df)), df.index)
yt_o = plt.gca().get_yticks()
yt = np.append(yt_o, y)
plt.gca().set_yticks(yt)
y_text = plt.text(-0.5, 50000, 'y = %d' % y, bbox=dict(fc='white', ec='k'))


# In[ ]:




