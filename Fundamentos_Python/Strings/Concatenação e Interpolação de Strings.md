# O que são concatenação de strings e interpolação de strings?

Ao trabalhar com strings, combinar diferentes pedaços de texto é uma operação comum com a qual você frequentemente lidará.

## Concatenando strings

Em Python, você pode combinar várias strings juntas com o operador mais (`+`). Esse processo é chamado de **concatenação de strings**. Veja como concatenar duas strings com o operador mais:

```python
my_str_1 = 'Hello'
my_str_2 = "World"

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) # Hello World
```

## Repetindo strings

Você também pode repetir uma string multiplicando-a por um inteiro usando o operador `*`. A string é repetida o número especificado de vezes:

```python
sound = 'ha'
repeated_sound = sound * 3
print(repeated_sound) # hahaha
```

## Concatenando strings com números

A concatenação funciona apenas com strings. Se você tentar concatenar uma string com um número, receberá um `TypeError`:

```python
name = 'John Doe'
age = 26

name_and_age = name + age
print(name_and_age) # TypeError: can only concatenate str (not "int") to str
```

Isso acontece porque o Python não converte automaticamente outros tipos de dados como inteiros em strings quando você os concatena. O Python exige que todos os elementos sejam strings antes de poder concatená-los. Para resolver isso, você pode converter o número em uma string com a função embutida `str()`, que retorna a representação em string do valor dado sem modificar o valor original:

```python
name = 'John Doe'
age = 26

name_and_age = name + str(age)
print(name_and_age) # John Doe26
```

Você também pode usar o operador de atribuição aumentada para concatenação. Isto é representado por um sinal de mais e igual (`+=`), e realiza tanto a concatenação e a atribuição em um único passo. Aqui está em ação:

```py
name = 'John Doe'
age = 26

name_and_age = name  # Start with the name
name_and_age += str(age)  # Append the age as string

print(name_and_age)  # John Doe26
```

## Interpolação de string

O processo de inserir variáveis e expressões em uma string é chamado de **string interpolation**. Python possui uma categoria de string chamada **f-strings** (abreviação de formatted string literals), que permite lidar com interpolação com uma sintaxe compacta e legível.

F-strings começam com `f` (minúsculo ou maiúsculo) antes das aspas e permitem que você incorpore variáveis ou expressões dentro de campos de substituição indicados por chaves (`{}`). Aqui está um exemplo:

```python
name = 'John Doe'
age = 26
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age) # My name is John Doe and I am 26 years old

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 10 is 15
```

Observe como você não precisa converter tipos não string com a função `str()`. No exemplo acima, o valor das variáveis `age`, `num1` e `num2` é convertido internamente em uma string durante o processo de interpolação.
