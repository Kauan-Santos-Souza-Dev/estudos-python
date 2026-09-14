 # Como declarar variáveis e quais são as convenções de nomenclatura para nomear variáveis?

Em Python, variáveis são como caixas rotuladas para armazenar e referenciar dados de diferentes tipos. Para criar uma variável, escreva seu nome à esquerda, seguido pelo operador de atribuição (`=`) e o valor que você quer armazenar à direita. Aqui está um exemplo de como criar as variáveis `name` e `age`:

```python
name = 'John Doe'
age = 25
```

No exemplo acima, a variável `name` armazena o valor `'John Doe'`. Esse valor é uma string, que é uma série de caracteres usada para representar texto. Strings são escritas com aspas simples ou duplas, por exemplo `'Hello'` ou `"Hello"`. Em aulas futuras, você aprenderá mais sobre como trabalhar com strings em Python.

Ao nomear variáveis em Python, há algumas regras importantes que você deve ter em mente:

- Os nomes das variáveis só podem começar com uma letra ou um underscore (`_`), não com um número.
- Os nomes das variáveis só podem conter caracteres alfanuméricos (`a-z`, `A-Z`, `0-9`) e underscores (`_`).
- Os nomes das variáveis são sensíveis a maiúsculas e minúsculas: `age`, `Age` e `AGE` são todos considerados únicos.
- Os nomes das variáveis não podem ser palavras-chave reservadas do Python, como `if`, `class` ou `def`.

Se você quebrar alguma dessas regras, seu programa Python vai gerar um `SyntaxError`:

```md
    5variable_name = 5
     ^
SyntaxError: invalid syntax
```

Agora vamos revisar algumas convenções comuns de nomenclatura para variáveis em Python.

Primeiro, os nomes das variáveis devem estar em minúsculas, com as palavras separadas por underscore. Isso é chamado de snake case:

```python
my_variable_name = 'freeCodeCamp'
```

Em seguida, você deve usar nomes descritivos para variáveis. Por exemplo, se você quiser salvar a idade de um usuário como uma variável, `user_age` é melhor do que `age` ou uma abreviação como `ua`:

```python
user_age = 30
```

Dessa forma, você pode comunicar facilmente o propósito de uma variável para outros membros da equipe (ou para você mesmo no futuro) em uma base de código grande.

Outra convenção é evitar usar nomes de variáveis com uma única letra. Nomes de uma letra são comuns em Python, mas devem ser evitados porque não comunicam propósito ou significado:

```python
x = 56 # What do you mean by x?
```

O símbolo de cerquilha (`#`) e o texto que o segue formam um comentário. Comentários permitem que você adicione notas e explicações ao seu código.

Em Python, comentários começam com o símbolo de cerquilha (`#`), e a linguagem ignora tudo depois do símbolo `#` naquela linha:

```python
# This is a single-line comment
```

Comentários de múltiplas linhas podem ser criados usando comentários de uma única linha consecutivos:

```python
# This is a
# multi-line
# comment
```

Você pode usar comentários para explicar seu código, deixar lembretes para si mesmo ou esclarecer por que uma linha existe. Comentários são especialmente úteis quando você está aprendendo ou trabalhando em equipes.

No entanto, você não deve usar comentários para explicar o que seus nomes de variáveis significam. Em vez disso, os nomes que você escolher para suas variáveis devem ser descritivos e comunicar para que elas servem e seguir as outras regras de nomenclatura mencionadas anteriormente para evitar erros de sintaxe.
