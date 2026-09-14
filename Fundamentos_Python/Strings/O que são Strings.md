# O que são Strings e o que é Imutabilidade de String?

Uma string é uma sequência de caracteres cercada por aspas simples ou duplas. O Python trata ambas as formas como strings, então você pode usar qualquer uma delas. Aqui estão alguns exemplos:

Código de exemplo

```python
my_str_1 = 'Hello'
my_str_2 = "World"
```

Se você precisar de uma string de múltiplas linhas, pode usar três aspas duplas ou aspas simples:

Código de exemplo

```python
my_str_3 = """Multiline
string"""
my_str_4 = '''Another
multiline
string'''
```

Se sua string contém aspas simples ou duplas, então você tem duas opções:

- Use o tipo oposto de aspas. Ou seja, se sua string contém aspas simples, use aspas duplas para envolver a string e vice-versa:

Código de exemplo

```python
msg = "It's a sunny day"
quote = 'She said, "Hello World!"'
```

- Escape a aspa simples ou dupla na string com uma barra invertida (`\`). Com este método, você pode usar aspas simples ou duplas para envolver a própria string:

Código de exemplo

```python
msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""
```

Às vezes, pode ser necessário verificar se uma string contém um ou mais caracteres. Para isso, o Python fornece o operador `in`, que retorna um booleano que especifica se o caractere ou os caracteres existem na string ou não.

Aqui estão alguns exemplos:

Código de exemplo

```python
my_str = 'Hello world'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False
```

Vamos agora ver como é possível obter o tamanho de uma string e como trabalhar com caracteres individuais em uma string, um processo que chamamos de **indexação**. Para obter o comprimento de uma string, você pode usar a função embutida `len()`. Aqui está um exemplo:

Código de exemplo

```python
my_str = 'Hello world'
print(len(my_str))  # 11
```

Cada caractere em uma string tem uma posição chamada índice. O índice é baseado em zero, significando que o índice do primeiro caractere de uma string é `0`, o índice do segundo caractere é `1` e assim por diante. Para acessar um caractere pelo seu índice, você usa colchetes (`[]`) com o índice do caractere que deseja acessar dentro. Aqui estão alguns exemplos:

Código de exemplo

```python
my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w
```

A indexação negativa também é permitida, então você pode obter o último caractere de qualquer string com `-1`, o penúltimo caractere com `-2` e assim por diante:

Código de exemplo

```python
my_str = 'Hello world'
print(my_str[-1])  # d
print(my_str[-2]) # l
```

No Python, valores podem ser mutáveis ou imutáveis. Um valor mutável pode ser alterado depois de criado, enquanto um valor imutável não pode.

Você pode apontar uma variável para um novo valor, o que é chamado de reatribuição, mas não pode mudar o valor imutável em si adicionando, removendo ou substituindo qualquer um de seus elementos.

Strings são imutáveis no Python. Isso significa que você pode reatribuir uma string diferente a uma variável:

Código de exemplo

```python
greeting = 'hi'
greeting = 'hello'
print(greeting) # hello
```

Mas a modificação direta de uma string não é permitida:

Código de exemplo

```python
greeting = 'hi'
greeting[0] = 'H' # TypeError: 'str' object does not support item assignment
```

Inteiros, floats e booleanos também são imutáveis. Você vai aprender sobre outros tipos imutáveis em lições futuras.
