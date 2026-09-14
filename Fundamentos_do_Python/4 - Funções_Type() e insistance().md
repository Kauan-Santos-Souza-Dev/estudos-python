# Como funcionam as funções type() e isinstance()?

Na lição anterior, você aprendeu sobre tipos de dados comuns em Python, incluindo os tipos string, inteiro e float. Conforme você desenvolve seus programas, precisará aprender como visualizar o tipo de uma variável.

Aqui está uma variável de exemplo:

```py
developer = 'Devin'
```

Para ver qual é o tipo de `developer`, você pode usar a função `type()` assim:

```py
developer = 'Devin'

print(type(developer)) # <class 'str'>
```

A saída de `<class 'str'>` significa que `developer` é do tipo string.

Se você não fornecer nenhum argumento para a função `type()`, receberá a seguinte mensagem de erro:

```md
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: type() takes 1 or 3 arguments
```

Aqui estão os tipos de dados que você aprendeu até agora, junto com o que a função `type()` imprime para cada um:

```python
my_integer_var = 10
print(type(my_integer_var))  # <class 'int'>

my_float_var = 4.50
print(type(my_float_var))  # <class 'float'>

my_string_var = 'hello'
print(type(my_string_var))  # <class 'str'>

my_boolean_var = True
print(type(my_boolean_var))  # <class 'bool'>
```

Haverá momentos no seu programa em que você precisará verificar se uma variável específica é de um tipo determinado antes de realizar operações nela. É aí que a função `isinstance()` é útil.

Aqui está uma variável de exemplo com uma string atribuída a ela:

```py
account_balance = '12'
```

Se você tentar realizar operações matemáticas como divisão usando a variável `account_balance`, receberá uma mensagem de erro.

```py
account_balance = '12'

account_balance / 2

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for /: 'str' and 'int'
```

Para verificar se `account_balance` é um inteiro, você pode usar a função `isinstance()` assim:

```py
account_balance = '12'

isinstance(account_balance, int) # False
```

A função embutida `isinstance()` permite verificar se uma variável corresponde a um tipo de dado específico. Ela recebe um valor e o tipo contra o qual você quer verificar, e então retorna um booleano. Neste caso, como `account_balance` é uma string, ela retornará `False`.

A função `isinstance()` também permite verificar múltiplos tipos ao mesmo tempo.

Aqui está um exemplo verificando se `account_balance` é um `int` ou `float`:

```py
account_balance = 12
isinstance(account_balance, (int, float)) # True
```

Neste exemplo, `account_balance` é um inteiro, então `isinstance()` retorna `True`. Se `account_balance` fosse `12.0`, `isinstance()` ainda retornaria `True` porque você está verificando para inteiros ou floats.

Em futuras oficinas e laboratórios, você usará as funções `type()` e `isinstance()` para garantir que suas variáveis contenham os tipos de dados corretos antes de realizar operações nelas.
