# Quais são os tipos de dados comuns em Python?

Antes de trabalhar com variáveis em Python, é importante entender os tipos de dados. Um tipo de dado descreve o tipo de valor que uma variável contém, por exemplo, um número ou um pedaço de texto. Linguagens de programação usam tipos de dados para saber como armazenar e trabalhar com diferentes tipos de informação.

Python é uma linguagem dinamicamente tipada. Isso significa que você não especifica o tipo de dado de uma variável quando a cria. Python determina o tipo a partir do valor atribuído à variável.

Aqui estão alguns exemplos:

```python
name = 'John Doe' # Python knows this is a string
age = 25 # Python knows this is an integer
```

Uma variável pode depois receber um valor de um tipo diferente:

```python
age = 25
age = 'Twenty-five'
```

Após a segunda atribuição, `age` contém uma string em vez de um inteiro.

Por enquanto, concentre-se em quatro tipos de dados que você usará ao longo deste módulo:

- Inteiro: Um número inteiro sem decimais, por exemplo, `10` ou `-5`.

```python
my_integer_var = 10
print('Integer:', my_integer_var) # Integer: 10
```

- Float: Um número com ponto decimal, como `4.41` ou `-0.4`.

```python
my_float_var = 4.50
print('Float:', my_float_var) # Float: 4.5
```

- String: Uma sequência de caracteres entre aspas simples ou duplas como `'Hello world!'`.

```python
my_string_var = 'hello'
print('String:', my_string_var) # String: hello
```

- Booleano: Um tipo verdadeiro ou falso, escrito como `True` ou `False`.

```python
my_boolean_var = True
print('Boolean:', my_boolean_var) # Boolean: True
```

Python tem outros tipos de dados. Você aprenderá cada um quando precisar deles pela primeira vez.
