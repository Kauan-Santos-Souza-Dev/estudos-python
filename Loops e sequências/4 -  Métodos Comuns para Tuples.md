# Quais São Alguns Métodos Comuns para Tuples?

Na lição anterior, você aprendeu como trabalhar com o tipo de dado tuple. Nesta lição, você aprenderá sobre alguns métodos comuns que você usará ao trabalhar com tuples.

O primeiro método que vamos abordar é `count()`. Este método é usado para determinar quantas vezes um item aparece em uma tupla. Aqui está um exemplo de como verificar quantas vezes a string `Rust` aparece em uma tupla chamada `programming_languages`:

```py
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.count('Rust') # 2
```

Como `Rust` aparece duas vezes na tupla, o método `count()` retorna o número `2`. Se o item especificado na função `count()` não estiver presente na tupla, então o valor retornado é `0`:

```py
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.count('JavaScript') # 0
```

Se nenhum argumento for passado para a função `count()`, então o Python gera um `TypeError`:

```py
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.count()

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: tuple.count() takes exactly one argument (0 given)
"""
```

O próximo método que vamos analisar é o método `index()`. Este método é usado para encontrar o índice onde um item específico está presente em uma tupla. Aqui está um exemplo de uso do método `index()` para encontrar o índice da string `Java`:

```py
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.index('Java') # 1
```

Se o item especificado não puder ser encontrado, então o Python gera um `ValueError`:

```py
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.index('JavaScript')

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: tuple.index(x): x not in tuple
"""
```

Outra coisa que você pode fazer com o método `index()` é passar argumentos opcionais de índice inicial e final. Aqui está um exemplo de como passar um índice inicial opcional:

```py
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
programming_languages.index('Python', 3) # 5
```

Neste exemplo, estamos especificando onde começar a buscar pela string `Python`. Ao passar o número `3` como segundo argumento para a função `index()`, estamos especificando para começar a busca no índice `3`. Como `Python` aparece duas vezes na tupla, a função `index()` retornará o índice `5` em vez do índice `2` por causa do uso do argumento opcional de índice inicial.

Você também pode passar um índice de parada opcional. Aqui está um exemplo modificado de especificação de um índice inicial e final:

```py
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python', 'JavaScript', 'Python')
programming_languages.index('Python', 2, 5) # 2
```

Agora o resultado é o índice `2` porque estamos começando a busca no índice `2` e procurando até, mas não incluindo, o índice `5`.

Outra função comumente usada com tuplas é a função `sorted()`. Em uma lição anterior, você aprendeu sobre o método `sort()` para listas. Pois bem, a função `sorted()` pode ser usada em qualquer iterável, incluindo tuplas.

Aqui está um exemplo de como criar uma nova lista de números usando a função `sorted()`:

```py
numbers = (13, 2, 78, 3, 45, 67, 18, 7)
sorted(numbers) # [2, 3, 7, 13, 18, 45, 67, 78]
```

A função `sorted()` sempre criará uma nova lista com os valores ordenados. Isto difere do método `sort()` que ordena os elementos de uma lista no local e não retorna uma nova lista.

Se você precisar personalizar o comportamento de ordenação para um iterável, pode usar os argumentos opcionais `reverse` e `key`. Aqui está um exemplo de uso do argumento `key` para ordenar itens em uma tupla por comprimento:

```py
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
sorted(programming_languages, key=len)

# Result
# ['C++', 'Rust', 'Java', 'Rust', 'Python', 'Python']
```

Se você quiser criar uma nova lista de valores em ordem reversa, então você pode usar o argumento `reverse` assim:

```py
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')

print(sorted(programming_languages, reverse=True))

# Result
# ['Rust', 'Rust', 'Python', 'Python', 'Java', 'C++']
```

Tuples são um tipo de dado comum em Python. Entender como trabalhar com eles, junto com alguns métodos e funções úteis, ajudará você a escrever um código mais eficiente.
