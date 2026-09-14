# Quais São Alguns Métodos Comuns de String?

Um método é uma função que você chama em um valor. Para chamar um método de string, escreva a string ou o nome da variável seguido de um ponto e da chamada do método. Você vai aprender mais sobre métodos quando estudar classes e objetos. Aqui estão alguns métodos comuns de string:

- `upper()`: Retorna uma nova string com todos os caracteres convertidos para maiúsculas.

```python
my_str = 'hello world'

uppercase_my_str = my_str.upper()
print(uppercase_my_str)  # HELLO WORLD
```

- `lower()`: Retorna uma nova string com todos os caracteres convertidos para minúsculas.

```python
my_str = 'Hello World'

lowercase_my_str = my_str.lower()
print(lowercase_my_str)  # hello world
```

- `strip()`: Retorna uma nova string com os caracteres especificados no início e no fim removidos. Se nenhum argumento for passado, remove os espaços em branco do início e do fim.

```python
my_str = '  hello world  '

trimmed_my_str = my_str.strip()
print(trimmed_my_str)  # "hello world"
```

- `replace(old, new)`: Retorna uma nova string com todas as ocorrências de `old` substituídas por `new`.

```python
my_str = 'hello world'

replaced_my_str = my_str.replace('hello', 'hi')
print(replaced_my_str)  # hi world
```

- `split(separator)`: Divide uma string em um separador especificado em uma lista de strings. Uma lista agrupa valores entre colchetes. Se nenhum separador for especificado, `split()` divide pelo espaço em branco.

```python
my_str = 'hello world'

split_words = my_str.split()
print(split_words)  # ['hello', 'world']
```

- `join()`: Junta as strings em uma coleção em uma única string com um separador.

```python
my_list = ['hello', 'world']

joined_my_str = ' '.join(my_list)
print(joined_my_str)  # hello world
```

- `startswith(prefix)`: Retorna um booleano indicando se uma string começa com o prefixo especificado.

```python
my_str = 'hello world'

starts_with_hello = my_str.startswith('hello')
print(starts_with_hello)  # True
```

- `endswith(suffix)`: Retorna um booleano indicando se uma string termina com o sufixo especificado.

```python
my_str = 'hello world'

ends_with_world = my_str.endswith('world')
print(ends_with_world)  # True
```

- `find(substring)`: Retorna o índice da primeira ocorrência de `substring`, ou `-1` se não encontrar nenhuma.

```python
my_str = 'hello world'

world_index = my_str.find('world')
print(world_index)  # 6
```

- `count(substring)`: Retorna o número de vezes que uma substring aparece em uma string.

```python
my_str = 'hello world'

o_count = my_str.count('o')
print(o_count)  # 2
```

- `capitalize()`: Retorna uma nova string com o primeiro caractere em maiúscula e os outros caracteres em minúscula.

```python
my_str = 'hello world'

capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)  # Hello world
```

- `isupper()`: Retorna `True` se todas as letras na string estiverem em maiúsculas e `False` se não estiverem.

```python
my_str = 'hello world'

is_all_upper = my_str.isupper()
print(is_all_upper)  # False
```

- `islower()`: Retorna `True` se todas as letras na string estiverem em minúsculas e `False` se não estiverem.

```python
my_str = 'hello world'

is_all_lower = my_str.islower()
print(is_all_lower)  # True
```

- `title()`: Retorna uma nova string com a primeira letra de cada palavra em maiúscula.

```python
my_str = 'hello world'

title_case_my_str = my_str.title()
print(title_case_my_str)  # Hello World
```
