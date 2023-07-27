# Module 3 Quiz

1. A supervised learning model has been built to predict whether someone is infected with a new strain of a virus. The probability of any one person having the virus is 5%. Using accuracy as a metric, what would be a good choice for a baseline accuracy score that the new model would want to otperform?

**Solução:**

Para determinar uma boa pontuação de precisão de referência (baseline accuracy) para o novo modelo, precisamos considerar a probabilidade da classe majoritária no conjunto de dados, que é a classe que representa pessoas não infectadas com a nova cepa do vírus.

- Identificar a probabilidade da classe majoritária (pessoas não infectadas): Neste caso, a probabilidade de alguém não ter o vírus é $100\% - 5\% = 95\%$.
- Usar a probabilidade da classe majoritária como a precisão de referência (baseline accuracy): Uma vez que a classe majoritária representa o resultado mais comum (não infectado), um modelo de referência simples que sempre prevê a classe majoritária alcançaria uma precisão de $95\%$.
- O novo modelo deve ter como objetivo superar essa pontuação de precisão de referência: O objetivo do novo modelo é ter uma precisão maior que 95% para ser considerado melhor que a referência.

Portanto, uma boa escolha para a precisão de referência (baseline accuracy) que o novo modelo desejaria superar é $95\%$.

Conhecimento relacionado:

- Entendimento do conceito de precisão de referência (baseline accuracy) em tarefas de classificação binária.
- Avaliação do desempenho do modelo usando a precisão como métrica.
- Importância de estabelecer benchmarks de desempenho para comparar a eficácia dos modelos.

2. Given the following confusion matrix:

<center>

| |Predicted Positive| Predicted Negative |
|---:|:--:|:--:|
Condition positive |  67| 11|
Condition negative | 3 | 8|

</center>

Compute the accuracy o three decimals places.

**Solution**

Vamos calcular o valor do _accuracy_

- Verdadeiros positivos (True Positives, TP): 67 (casos positivos corretamente previstos)
- Verdadeiros negativos (True Negatives, TN): 8 (casos negativos corretamente previstos)
- Falsos positivos (False Positives, FP): 11 (casos negativos erroneamente previstos como positivos)
- Falsos negativos (False Negatives, FN): 3 (casos positivos erroneamente previstos como negativos)

Calcule a precisão (accuracy):
A precisão é a proporção de previsões corretas em relação ao total de previsões.

$$
\begin{align*}
Precisão (Accuracy) &= \frac{(TP + TN)} {(TP + TN + FP + FN)} \\
Precisão (Accuracy) &= \frac{(67 + 8)}{(67 + 8 + 11 + 3)} \\
Precisão (Accuracy) &= \frac{75}{89} \\
Precisão (Accuracy) &≈ 0.842 \\
\end{align*}
$$

Portanto, a precisão (accuracy) é aproximadamente $0.842$, arredondado para três casas decimais.

Conhecimento relacionado:

- Matriz de Confusão: Entendimento da matriz usada para avaliar o desempenho de modelos de classificação.
- Métricas de Avaliação: Precisão (Accuracy) é uma das métricas usadas para medir o desempenho de um modelo de classificação.
- Fórmulas para calcular as métricas de avaliação em relação aos valores da matriz de confusão.


3. Given the following confusion matrix:

<center>

| |Predicted Positive| Predicted Negative |
|-----------------:|:---:|:--:|
Condition Positive | 102 | 56 |
Condition Negative | 17  | 78 |

</center>

Compute the precision to three decimal places.

**Solução**

Vamos calcular a _precision_

- Verdadeiros positivos (True Positives, TP): 102 (casos positivos corretamente previstos)
- Falsos positivos (False Positives, FP): 56 (casos negativos erroneamente previstos como positivos)
- Verdadeiros negativos (True Negatives, TN): 78 (casos negativos corretamente previstos)
- Falsos negativos (False Negatives, FN): 17 (casos positivos erroneamente previstos como negativos)

A precisão é a proporção de verdadeiros positivos em relação ao total de casos positivos previstos.

$$
\begin{align*}
Precisão (Precision) &= \frac{TP}{(TP + FP)} \\
Precisão (Precision) &= \frac{102}{(102 + 56)} \\
Precisão (Precision) &= \frac{102}{158} \\
Precisão (Precision) &≈ 0.646 \\
\end{align*}
$$

Portanto, a precisão (precision) é aproximadamente $0.646$, arredondada para três casas decimais.

Conhecimento relacionado:

- Matriz de Confusão: Entendimento da matriz usada para avaliar o desempenho de modelos de classificação.
- Métricas de Avaliação: Precisão (Precision) é uma das métricas usadas para medir o desempenho de um modelo de classificação.
- Fórmulas para calcular as métricas de avaliação em relação aos valores da matriz de confusão.


4. Given the following confusion matrix:

<center>

| |Predicted Positive| Predicted Negative |
|-----------------:|:---:|:--:|
Condition Positive | 102 | 56 |
Condition Negative | 17  | 78 |

</center>

Compute the recall to three decimal places.

**Solução**

Vamos calcular o _recall_

- Verdadeiros positivos (True Positives, TP): 102 (casos positivos corretamente previstos)
- Falsos negativos (False Negatives, FN): 56 (casos positivos erroneamente previstos como negativos)
- Verdadeiros negativos (True Negatives, TN): 78 (casos negativos corretamente previstos)
- Falsos positivos (False Positives, FP): 17 (casos negativos erroneamente previstos como positivos)

O recall é a proporção de verdadeiros positivos em relação ao total de casos positivos reais.

$$
\begin{align*}
Recall &= \frac{TP}{(TP + FN)} \\
Recall &= \frac{102}{(102 + 17)} \\
Recall &= \frac{102}{119} \\
Recall &≈ 0.857 \\
\end{align*}
$$

Portanto, o recall é aproximadamente 0.646, arredondado para três casas decimais.

Conhecimento relacionado:

Matriz de Confusão: Entendimento da matriz usada para avaliar o desempenho de modelos de classificação.
Métricas de Avaliação: Recall é uma das métricas usadas para medir o desempenho de um modelo de classificação.
Fórmulas para calcular as métricas de avaliação em relação aos valores da matriz de confusão.


5. Using the fitted model `m` create a precision-recall curve to answer the following question:

    For the fitted model `m`, approximately what precision can we expect for a recall of 0.8?

(Use y_test and X_test to compute the precision-recall curve. If you wish to view a plot you can use `plt.show()`)

**Solução**

Para criar uma curva de precisão-recall para o modelo ajustado `m`` e estimar a precisão para um recall de 0.8, amos seguir os seguintes passos:

- Importe as bibliotecas necessárias:
Você precisará das bibliotecas numpy, matplotlib e da função precision_recall_curve da biblioteca sklearn.metrics.

- Obtenha as previsões do modelo m para o conjunto de teste (X_test):
Use o modelo ajustado m para fazer previsões nos dados de teste (X_test) e armazene as previsões.

- Calcule a curva de precisão-recall:
Use a função precision_recall_curve para calcular a precisão e o recall para diferentes limiares de probabilidade do modelo. Isso cria um conjunto de valores de precisão e recall que podem ser usados para plotar a curva.

- Encontre a precisão para um recall de 0.8:
Depois de calcular a curva de precisão-recall, encontre o valor de precisão correspondente a um recall de 0.8. Isso pode ser feito procurando o valor mais próximo de 0.8 no array de recalls e obtendo o valor correspondente no array de precisões.

- Plote a curva de precisão-recall (opcional):
Se desejar, você pode usar a biblioteca matplotlib para plotar a curva de precisão-recall e visualizar a relação entre precisão e recall.

Conhecimento relacionado:

- Avaliação de modelos de classificação: A curva de precisão-recall é uma ferramenta importante para avaliar o desempenho de modelos de classificação, especialmente quando as classes estão desbalanceadas.
- Precision-Recall Curve: Compreender como a curva é criada e interpretada pode fornecer insights sobre a precisão e o recall em diferentes pontos de corte das probabilidades do modelo.
- Uso da biblioteca Scikit-learn: A biblioteca Scikit-learn é amplamente utilizada para a construção e avaliação de modelos de aprendizado de máquina, incluindo a criação de curvas de precisão-recall.

```python
print(m)
```

```
LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True, intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1, penalty='12', random_state=None, solver = 'liblinear', tol=0.0001, verbose=0, warm_start=False)
```

```
# Previsões do modelo m para o conjunto de teste
y_pred_probs = m.predict_proba(X_test)[:, 1]

# Calculando a curva de precisão-recall
precision, recall, thresholds = precision_recall_curve(y_test, y_pred_probs)

# Encontrando a precisão para um recall de 0.8
idx = np.argmax(recall >= 0.8)
precision_at_recall_08 = precision[idx]

print("Precision at recall 0.8:", precision_at_recall_08)
```
```
Precision at recall 0.8: 0.267326732673
```

```python
# Plote a curva de precisão-recall (opcional)
plt.plot(recall, precision)
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.show()
```
<center>

![Precision-Recall Curve](q5.png)

</center>

8. Using the fitted model `m` what is micro precision score?

(Use y_test and X_test to compute the precision score.)

```python
print(m)
```
```
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0, decision_function_shape=None, degree = 3, gamma = 'auto', kernel = 'rbf', max_iter=-1, probability=False, random_state=None, shrinking=True, tol=0.001, verbose=False)
```

**Solução**

Para calcular o micro precision score usando o modelo ajustado `m``, Vamos precisar seguir os seguintes passos:

- Importe a função precision_score da biblioteca sklearn.metrics.
- Faça as previsões do modelo m para o conjunto de teste (X_test).
- Calcule o micro precision score usando a função precision_score.

```python
from sklearn.metrics import precision_score

# Faz as previsões do modelo m para o conjunto de teste
y_pred = m.predict(X_test)

# Calculo do micro precision score
micro_precision_score = precision_score(y_test, y_pred, average='micro')

print("Micro Precision Score:", micro_precision_score)
```

Neste código, a função `precision_score` é usada para calcular o micro precision score. O parâmetro `average='micro'` indica que queremos calcular o score considerando todas as classes como uma única classe (abordagem micro).

O micro precision score é útil quando há um desequilíbrio significativo entre as classes, e desejamos atribuir mais importância às previsões das classes majoritárias.

Conhecimento relacionado:

- Avaliação de modelos de classificação: A precisão é uma das métricas usadas para avaliar o desempenho de modelos de classificação.
- Micro Precision Score: Entendimento sobre a abordagem micro para calcular a precisão em casos de classes desequilibradas.
- Uso da biblioteca Scikit-learn: A biblioteca Scikit-learn é amplamente utilizada para a construção e avaliação de modelos de aprendizado de máquina, incluindo o cálculo de métricas de avaliação como a precisão.

9. Which of the following is tru of the R-Squared regression score metric?

    ✅ A model that always predicts the mean of y would get a score of 0.0

    ✅ The gihest possible score is 1.0

    ❎ The score can sometimes be negative.

    ❎ A model that always predicts the mean of y would get a score of 0.5

**Solução**

O R-squared é uma métrica comum para avaliar o desempenho de modelos de regressão. Vamos analisar cada afirmação:

- A model that always predicts the mean of y would get a score of 0.0:
    
    Isso é verdadeiro. Quando um modelo sempre faz previsões iguais à média dos valores reais de y, o R-squared será igual a 0.0. Significa que o modelo não está fornecendo nenhuma explicação da variabilidade dos dados em relação à média.

- The highest possible score is 1.0:
    
    Isso também é verdadeiro. O R-squared varia de 0.0 a 1.0. Um valor de 1.0 indica que o modelo explica toda a variabilidade dos dados, ou seja, todas as variações em y podem ser perfeitamente previstas a partir das variáveis independentes do modelo.

- The score can sometimes be negative:

    Isso é falso. O R-squared não pode ser negativo. Ele pode variar de 0.0 a 1.0, mas nunca será um valor negativo.

- A model that always predicts the mean of y would get a score of 0.5:
    
    Isso é falso. Como mencionado na primeira afirmação, um modelo que sempre prevê a média de y terá um R-squared de 0.0, não de 0.5.

Conhecimento relacionado:

- Coeficiente de determinação (R-squared): Entendimento sobre o R-squared como uma métrica comum para medir o desempenho de modelos de regressão.
- Interpretação do R-squared: Compreender o significado dos valores do R-squared em relação à qualidade do ajuste do modelo aos dados.

10. In a future society, a video surveillance algorithm is used to predict  a crime before it occurs. If you were reponsible for tuning this machine, what evaluation metric would you want to maximize to ensure no innocent people (people not about to commit a crime) are imprisoned (where crime is positive label)?

- Accuracy
- Precision
- Recall
- F1
- AUC

Se o objetivo é garantir que nenhuma pessoa inocente (que não está prestes a cometer um crime) seja presa, a métrica de avaliação mais relevante a ser maximizada é a "Recall" (Sensibilidade ou Taxa de Verdadeiros Positivos).

O objetivo é minimizar o número de falsos negativos (pessoas prestes a cometer um crime, mas não identificadas pelo algoritmo) para garantir que nenhum inocente seja preso erroneamente.

O Recall é a proporção de casos positivos corretamente identificados em relação ao número total de casos positivos reais. No contexto desse algoritmo de vigilância, o recall mede a capacidade do modelo de detectar com precisão os casos de crimes antes que ocorram, ou seja, identificar com sucesso as pessoas que estão prestes a cometer um crime.

Neste cenário, um falso negativo representaria uma pessoa prestes a cometer um crime que não foi detectada pelo algoritmo de vigilância. Isso pode levar a consequências graves, pois um criminoso pode escapar da vigilância e cometer um crime real. Portanto, é essencial minimizar os falsos negativos, o que significa maximizar o Recall.

Outras métricas como a "Precision", "F1 Score" ou "AUC" podem ser úteis para avaliar o desempenho geral do modelo, mas se o objetivo principal é garantir que nenhuma pessoa inocente seja presa erroneamente, o Recall é a métrica mais relevante e deve ser maximizado.

Conhecimento relacionado:

- Avaliação de modelos de classificação: Compreensão das diferentes métricas de avaliação utilizadas para medir o desempenho de modelos de classificação, como Accuracy, Precision, Recall, F1 Score e AUC.
- Precision e Recall: Compreender as diferenças e importância dessas métricas em cenários específicos, especialmente quando as consequências dos falsos positivos e falsos negativos são diferentes.

11. Consider the algorithm from the previous question. If you were responsible for tuning this machine, what evaluation metric would you wnat to maximize to ensure all criminals (people about to commit a crime) are impresoned (where crime is the positive label)?

- Accuracy
- Precision
- Recall
- F1
- AUC

Se o objetivo é garantir que todos os criminosos (pessoas prestes a cometer um crime) sejam presos, a métrica de avaliação mais relevante a ser maximizada é a "Precision" (Precisão Positiva).

O objetivo é minimizar o número de falsos positivos (pessoas não prestes a cometer um crime, mas identificadas como criminosos pelo algoritmo) para garantir que todos os criminosos sejam presos com precisão.

A Precision é a proporção de casos positivos corretamente previstos em relação ao número total de previsões positivas do modelo. No contexto desse algoritmo de vigilância, a precisão mede a capacidade do modelo de fazer previsões corretas sobre quem está prestes a cometer um crime, ou seja, identificar corretamente os criminosos.

Neste cenário, um falso positivo representaria uma pessoa que não está prestes a cometer um crime, mas foi erroneamente identificada pelo algoritmo como criminosa. Isso pode levar à prisão injusta de pessoas inocentes. Portanto, é essencial minimizar os falsos positivos, o que significa maximizar a Precision.

Outras métricas como a "Recall", "F1 Score" ou "AUC" podem ser úteis para avaliar o desempenho geral do modelo, mas se o objetivo principal é garantir que todos os criminosos sejam presos com precisão, a Precision é a métrica mais relevante e deve ser maximizada.

Conhecimento relacionado:

- Avaliação de modelos de classificação: Compreensão das diferentes métricas de avaliação utilizadas para medir o desempenho de modelos de classificação, como Accuracy, Precision, Recall, F1 Score e AUC.
- Precision e Recall: Compreender as diferenças e importância dessas métricas em cenários específicos, especialmente quando as consequências dos falsos positivos e falsos negativos são diferentes.