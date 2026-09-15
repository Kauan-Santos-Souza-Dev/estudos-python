# Como Funcionam as Atribuições Aumentadas?

A atribuição aumentada aplica uma operação a uma variável e armazena o resultado de volta na mesma variável, tudo em um único passo.

A sintaxe básica de uma atribuição aumentada é assim:

```python
variable <operator>= value
```

Qual é uma maneira mais eficiente de fazer isso:

```python
variable = variable <operator> value
```

Por exemplo, aqui está um exemplo de uso de atribuição aumentada para adicionar `5` a uma variável existente:

```python
my_var = 10
my_var += 5

print(my_var) # 15
```

E aqui está a mesma coisa, mas sem atribuição aumentada:

```python
my_var = 10
my_var = my_var + 5

print(my_var) # 15
```

A vantagem da atribuição aumentada é que ela fornece uma forma concisa e legível de atualizar o valor de uma variável sem repetir o nome da variável. Por sua vez, isso reduz a redundância e os erros potenciais que podem surgir de um erro de digitação ou algo semelhante.

Todo operador pode usar uma atribuição aumentada. Já vimos o operador de atribuição de adição (`+=`), então vamos ver outros.

- O operador de atribuição de subtração (`-=`) subtrai o operando da direita da variável da esquerda e armazena a diferença na variável da esquerda:

```python
count = 14
count -= 3

print(count) # 11
```

- O operador de atribuição de multiplicação (`*=`) multiplica a variável à esquerda pelo operando à direita e armazena o produto de volta na variável à esquerda:

```python
product = 65
product *= 7

print(product) # 455
```

- O operador de atribuição de divisão (`/=`) divide a variável à esquerda pela da direita e armazena o resultado de volta na variável à esquerda:

```python
price = 100
price /= 4

print(price) # 25.0
```

- O operador de divisão inteira (`//=`) realiza a divisão inteira da variável à esquerda pela da direita e armazena o resultado de volta na variável à esquerda:

```python
total_pages = 23
total_pages //= 5

print(total_pages) # 4
```

- O operador de atribuição de módulo (`%=`) calcula o resto da variável à esquerda dividida pela da direita e armazena o resultado de volta na variável à esquerda:

```python
bits = 35
bits %= 2

print(bits) # 1
```

- O operador de atribuição de exponenciação (`**=`) eleva a variável à esquerda à potência da variável à direita e armazena o resultado de volta na variável à esquerda:

```python
power = 2
power **= 3

print(power) # 8
```

Você também pode usar alguns operadores de atribuição aumentada com strings. Por exemplo, o operador de atribuição de adição facilita a concatenação de strings:

```python
greet = 'Hello'
greet += ' World'

print(greet) # Hello World
```

E o operador de atribuição de multiplicação pode ser usado para repetir uma string:

```python
greet = 'Hello'
greet *= 3

print(greet) # HelloHelloHello
```

Outras atribuições aumentadas lançam um `TypeError` quando você as usa com strings:

```python
greet = 'Hello'
greet -= ' World'

print(greet) # TypeError: unsupported operand type(s) for -=: 'str' and 'str'


greet = 'Hello'
greet /= 'World'

print(greet) # TypeError: unsupported operand type(s) for /=: 'str' and 'str' 
```
