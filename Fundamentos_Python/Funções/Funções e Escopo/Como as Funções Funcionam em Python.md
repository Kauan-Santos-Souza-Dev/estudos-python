# Como as Funções Funcionam em Python?

Funções são pedaços reutilizáveis de código que executam quando você faz uma chamada a elas. Python oferece funções embutidas, incluindo `print()`, que você usou em lições anteriores.

Outra função interna útil é `input()`, que permite solicitar uma entrada do usuário:

```python
name = input('What is your name?') # User types "Kolade" and presses Enter  
print('Hello', name) # Output: Hello Kolade
```

Por outro lado, `int()` converte um número, booleano e uma string numérica em um inteiro:

```python
print(int(3.14)) # 3
print(int('42')) # 42
print(int(True)) # 1
print(int(False)) # 0 
```

Você também pode escrever suas próprias funções customizadas. Para fazer isso, você usa a palavra-chave `def`, seguida do nome que deseja dar à sua função, um par de parênteses e dois pontos. Então, em uma nova linha, você escreve o código que sua função deve executar. O código que a função executa também é chamado de corpo da função.

Aqui está um exemplo de uma função personalizada chamada `hello` que imprime a string `Hello World` no terminal:

```python
def hello():
    print('Hello World')
```

Para executar a função, você precisa chamá-la pelo nome seguido de um par de parênteses:

```python
hello() # Hello World
```

Observe a indentação antes de `print('Hello World')`. Como você deve se lembrar das lições anteriores, o Python depende da indentação para determinar quais grupos de instruções pertencem juntos. Esses grupos de instruções são chamados de blocos de código.

Aqui está outra função simples que imprime a soma de dois números no terminal:

```python
def calculate_sum(a, b):
    print(a + b)
```

Você pode ver que nossa função, `calculate_sum`, tem `a` e `b` em seus parênteses, separados por uma vírgula. Esses são chamados de parâmetros. Pense nos parâmetros como variáveis substitutas que funcionam como "espaços" para os valores que você passa para as funções quando as chama.

Para usar os parâmetros, você precisa passar "arguments". Argumentos são os valores que você passa para uma função quando a chama.

Aqui está como chamar a função `calculate_sum` para somar os números `3` e `1`:

```python
calculate_sum(3, 1) # 4
```

Se você chamar a função sem o número correto de argumentos, você receberá um `TypeError`:

```python
calculate_sum()

# TypeError: calculate_sum() missing 2 required positional arguments: 'a' and 'b'
```

Funções também usam uma palavra-chave especial `return` para sair da função e retornar um valor. Se você não usar explicitamente `return`, o Python retornará `None` por padrão.

`None` é um valor especial que representa a ausência de um valor. É o único valor do tipo de dado `NoneType`. `None` é imutável e falso, o que significa que não pode ser alterado e é avaliado como `False` em um contexto booleano.

Aqui está um exemplo:

```python
def calculate_sum(a, b):
    print(a + b)

my_sum = calculate_sum(3, 1) # 4
print(my_sum) # None
```

Você pode ver que a função `calculate_sum` imprime a soma de `a` e `b`, mas não retorna nada explicitamente. Então, quando atribuímos seu resultado a `my_sum`, o valor é na verdade `None`. Para corrigir isso, você pode usar a palavra-chave `return` para enviar de volta o resultado:

```python
def calculate_sum(a, b):
    return a + b

my_sum = calculate_sum(3, 1)
print(my_sum) # 4
```

Agora, `calculate_sum` retorna a soma de `a` e `b`, que é armazenada em `my_sum`.
