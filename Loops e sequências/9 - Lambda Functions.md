# O que são Lambda Functions e como elas funcionam?

Ao longo das lições anteriores, você está acostumado a definir funções usando a palavra-chave `def` assim:

```py
def square(num):
    return num ** 2

print(square(4)) # 16
```

Mas quando se trata de trabalhar com funções de ordem superior como `map()` e `filter()`, você pode usar uma função anônima inline. É aqui que entram as funções lambda.

Aqui está como a função `square()` fica quando refatorada em uma função lambda:

```py
lambda num: num ** 2
```

Como mencionado anteriormente, funções lambda são anônimas, então esta função não tem mais o nome `square` associado a ela. Funções lambda são ótimas quando você precisa usá-las em funções de ordem superior como esta:

```py
numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]
```

Neste exemplo, temos uma lista de números e queremos criar uma nova lista de números pares. Então passamos uma função lambda como um dos argumentos para a função `filter()` para obter uma nova lista contendo os números `2` e `4`.

Ao trabalhar com funções lambda é importante estar ciente das melhores práticas. Por exemplo, não é uma boa prática atribuir uma função lambda a uma variável assim:

```py
numbers = [1, 2, 3, 4, 5]

square = lambda x: x ** 2
squared_numbers = list(map(square, numbers))
print(squared_numbers) # [1, 4, 9, 16, 25]
```

Isso anula o propósito de usar funções anônimas. Neste caso, você deve usar uma função regular, assim:

```py
numbers = [1, 2, 3, 4, 5]

def square(num):
    return num ** 2

squared_numbers = list(map(square, numbers))
print(squared_numbers) # [1, 4, 9, 16, 25]
```

Além disso, você deve evitar criar funções lambda que sejam difíceis de ler ou desnecessariamente complicadas, como esta:

```py
result = (lambda x: (x**2 + 2*x - 1) if x > 0 else (x**3 - x + 4))(3)
print(result)  # 14
```

Embora esta função execute corretamente e produza o resultado correto de `14`, ela não é fácil de ler ou visualizar. Nesse caso, seria melhor criar uma função separada com uma declaração `if/else` e então chamar essa função:

```py
def calculate_expression(x):
    if x > 0:
        return x**2 + 2*x - 1
    else:
        return x**3 - x + 4

print(calculate_expression(3))  # 14
```

Tanto funções regulares quanto funções lambda têm seus casos de uso em programas Python. Se você está lidando com uma única expressão inline, então pode considerar usar uma função lambda. Caso contrário, usar uma função regular seria o caminho a seguir.
