# O que são List Comprehensions e quais são algumas funções úteis para trabalhar com listas?

Nas últimas aulas, você tem se familiarizado com o uso de loops assim:

```py
even_numbers = []

for num in range(21):
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)
```

Este exemplo cria uma nova lista vazia chamada `even_numbers` e percorre uma sequência de números entre `0` e `20`. Dentro do loop, há uma condição que verifica se o número atual tem um resto de `0` quando dividido por `2`. Isto é usado para determinar se o número é par. Se a condição for `True`, então o `num` atual é adicionado ao final da lista `even_numbers`. Finalmente, imprimimos a lista `even_numbers` no console.

Embora este código funcione, há uma forma mais concisa de escrevê-lo que usa list comprehension. List comprehension permite que você crie uma nova lista em uma única linha combinando um loop e uma condição diretamente dentro de colchetes. Isso torna o código mais curto e frequentemente mais fácil de ler.

Aqui está o exemplo refatorado de antes usando colchetes:

```py
even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers)
```

Neste exemplo refatorado, a lista `even_numbers` é criada usando uma única linha de código. A list comprehension percorre os números de `0` a `20` e inclui apenas aqueles que são divisíveis por `2`. Esta abordagem é mais compacta e elimina a necessidade de um loop separado e um bloco condicional.

Vamos dar uma olhada em outro exemplo para que possamos entender melhor como a list comprehension funciona:

```py
numbers = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(result)
```

Neste exemplo, temos uma lista de números e queremos criar uma nova lista de tuplas indicando quais números são pares ou ímpares. Na primeira parte da list comprehension, usamos uma declaração `if` para verificar se o número é divisível por `2` de forma exata. Se for o caso, então o resultado é uma tupla desse número seguida da palavra `Even`. Caso contrário, o resultado é uma tupla com o número seguido da palavra `Odd`.

Aqui está como o resultado aparece impresso no console:

```py
[(1, 'Odd'), (2, 'Even'), (3, 'Odd'), (4, 'Even'), (5, 'Odd')]
```

Outra forma de criar uma lista a partir de um iterável existente é a função `filter()`. Aqui está um exemplo de como criar uma nova lista apenas com palavras com mais de quatro caracteres:

```py
words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))
print(long_words) # ['mountain', 'river', 'cloud']
```

A função `filter()` é usada para selecionar elementos de um iterável que atendem a uma condição específica. A função `filter()` aceita uma função e um iterável como seus argumentos. Neste exemplo, estamos passando uma função `is_long_word` para a função `filter()` para verificar se a contagem da palavra atual é maior que `4`. Todas as palavras que têm uma contagem de caracteres maior que `4` são adicionadas em uma nova lista e atribuídas à variável `long_words`.

Além da função `filter()`, existem mais algumas funções que são úteis ao trabalhar com listas. Outra função para ficar atento é a função `map()`, que recebe um iterável e aplica uma função a cada um de seus elementos. Aqui está um exemplo de uso da função `map()` para converter uma lista de temperaturas de Celsius para Fahrenheit:

```py
celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit) # [32.0, 50.0, 68.0, 86.0, 104.0]
```

Assim como a função `filter()`, `map()` aceita uma função e um iterável como seus argumentos. A função `to_fahrenheit` recebe uma temperatura e a converte de Celsius para Fahrenheit.

A última função que vamos analisar é a função `sum()`. Esta função é usada para obter a soma de um iterável como uma lista ou tupla. Aqui está um exemplo de uso da função `sum()`:

```py
numbers = [5, 10, 15, 20]
total = sum(numbers)
print(total) # Result: 50
```

Você também pode passar um argumento opcional `start` que define o valor inicial para a soma. Aqui está um exemplo atualizado usando o argumento `start` como um argumento posicional:

```py
numbers = [5, 10, 15, 20]
total = sum(numbers, 10) # positional argument
print(total) # 60
```

Você também pode optar por usar o argumento `start` como um argumento nomeado assim:

```py
numbers = [5, 10, 15, 20]
total = sum(numbers, start=10) # keyword argument
print(total) # 60
```

Ambas as versões produzirão o mesmo resultado, mas o argumento de palavra-chave é um pouco mais explícito.

Compreensão de listas assim como outras funções como `map()`, `filter()` e `sum()` podem parecer um pouco confusas no começo. Mas com prática e tempo suficientes, você começará a se sentir mais confortável usando-os em seus programas Python.
