# O que é a Biblioteca Padrão do Python e como importar um módulo?

No desenvolvimento de software, uma biblioteca é como uma caixa de ferramentas para desenvolvedores.

Em vez de ter que implementar cada parte do código você mesmo do zero, uma biblioteca oferece código pré-escrito e reutilizável, como funções, classes e estruturas de dados que você pode usar em seus projetos.

Python possui uma extensa biblioteca padrão com muitos módulos internos diferentes. Eles são todos soluções padronizadas e bem avaliadas para muitos dos problemas e tarefas que você enfrentará diariamente como programador, tais como:

- Interagindo com o sistema operacional.
    
- Trabalhando com arquivos.
    
- Rede.
    
- Trabalhando com data e hora.
    
- Realizando operações matemáticas.
    
- Usando expressões regulares.
    
- Testando e depurando seu código.
    
- E muito mais!
    

Alguns exemplos de módulos internos populares são `math`, `random`, `re` (abreviação de "regular expressions") e `datetime`.

O módulo `math` possui funções úteis para realizar operações matemáticas mais complexas.

O módulo `random` é útil para gerar números aleatórios.

O módulo `re` é usado para trabalhar com expressões regulares.

E o módulo `datetime` é útil para trabalhar com datas e horários em Python.

Mas como você pode acessar as variáveis, constantes, funções e classes definidas nesses módulos internos?

Você usa uma declaração de importação. Estas declarações permitem que você importe módulos para o seu script Python. As declarações de importação geralmente são escritas no topo do arquivo. Além disso, você pode personalizá-los com base nas suas necessidades. Primeiro, você usa a declaração `import`, seguida pelo nome do módulo:

```python
import module_name
```

Vamos supor que você queira importar o módulo `math`. Nesse caso, você escreveria isso no topo do seu arquivo:

```python
import math
```

Então, se você precisar fazer uma chamada de uma função desse módulo no seu script Python, você usaria notação de ponto, com o nome do módulo seguido pelo nome da função:

```python
module_name.function_name() 
```

Por exemplo, para obter a raiz quadrada de 36, você escreveria `math` seguido de um ponto e depois `sqrt`, uma abreviação de raiz quadrada, e entre parênteses, você passaria quaisquer argumentos necessários. Neste caso, só precisamos passar o número do qual queremos a raiz quadrada:

```python
math.sqrt(36)
```

Esta é a versão mais básica de uma declaração de importação, mas existem outras alternativas.

Se você precisar importar o módulo com um nome diferente (também conhecido como "alias"), você pode usar esta sintaxe, com `as` seguido pelo alias no final da declaração de importação:

```python
import module_name as module_alias
```

Isso é frequentemente usado para abreviar nomes longos de módulos ou para evitar conflitos de nomes.

Por exemplo, para se referir ao módulo `math` como `m` no seu código, você pode atribuir um alias a ele, assim:

```python
import math as m 
```

Então, você pode acessar os elementos do módulo usando o alias:

```python
m.sqrt(36)
```

Mas às vezes você não precisa importar tudo de um módulo. Talvez você precise de apenas uma ou duas funções ou classes específicas. Python tem exatamente o que você precisa nesse caso.

Agora a declaração de importação começa com `from`, seguida pelo nome do módulo e depois a palavra-chave `import` seguida pelo nome dos elementos que você deseja importar:

```python
from module_name import name1, name2
```

Então, você pode usar esses nomes sem o prefixo do módulo no seu script Python.

Se você quiser atribuir aliases a esses nomes, pode fazer isso usando a palavra-chave `as` após cada um, seguida do alias que deseja usar:

```python
from module_name import name1 as alias1, name2 as alias2
```

Vamos supor que você queira importar apenas as funções radians, sine e cosine do módulo `math`. Você escreveria:

```python
from math import radians, sin, cos
```

Agora você pode chamar essas funções diretamente no seu código, sem o módulo `math` como prefixo.

Aqui temos um exemplo mais detalhado:

Para encontrar o seno e o cosseno de um ângulo específico inicialmente expresso em graus, podemos chamar a função `radians` para convertê-lo em radianos e depois chamar as funções seno e cosseno, passando o ângulo em radianos:

```python
from math import radians, sin, cos

angle_degrees = 40
angle_radians = radians(angle_degrees)

sine_value = sin(angle_radians)
cos_value = cos(angle_radians)

print(sine_value) # 0.6427876096865393
print(cos_value)  # 0.766044443118978
```

Note como estamos chamando as funções diretamente, sem o nome do módulo como prefixo. Isso ocorre porque importamos as funções com essa sintaxe alternativa.

Isso é útil, mas pode resultar em conflitos de nomes se você já tiver funções ou variáveis com o mesmo nome definidas no próprio script Python. Então isso é algo para ter em mente ao escolher qual tipo de declaração de importação você quer usar.

E finalmente, encontramos esta declaração de importação que termina com um asterisco. O asterisco está dizendo ao Python que você quer importar tudo naquele módulo, mas você quer importar de forma que não precise usar o nome do módulo como prefixo:

```python
from module_name import *
```

Por exemplo, se você fizer isso ao importar o módulo `math`, poderá chamar qualquer função definida nesse módulo sem especificar o nome do módulo como prefixo. Aqui estão alguns exemplos:

```python
from math import *
print(sqrt(36))  # 6.0
print(pow(5, 2)) # 25.0
print(exp(1))    # 2.718281828459045
```

No entanto, isso geralmente é desencorajado porque pode levar a colisões de namespace e dificultar saber de onde certos nomes estão vindo.

As declarações de importação funcionam exatamente da mesma forma para funções, classes, constantes, variáveis e quaisquer outros elementos definidos no módulo.

Aqui está um exemplo de uma constante do módulo `math`, o número `pi`:

```python
import math
print(math.pi)
```

E aqui está um exemplo de uma classe do módulo `datetime`. Criamos um objeto date que representa 15 de julho de 1959. Então, atribuímos esse objeto `date` a uma variável e acessamos o dia, o mês e o ano individualmente usando a notação de ponto:

```python
import datetime
birthday = datetime.date(1959, 7, 15)
print(birthday.day)    # 15
print(birthday.month)  # 7
print(birthday.year)   # 1959
```

Você pode encontrar mais informações sobre o conteúdo do módulo na documentação oficial do Python para esse módulo.

Ótimo. Agora que você sabe mais sobre módulos, você também deve conhecer este idiom muito importante em scripts Python, porque eles estão muito relacionados:

A ideia central é simples: **um arquivo Python pode ser executado ou importado, e o `if __name__ == '__main__'` deixa você separar os dois casos.**

**O problema que ele resolve**

Imagine o arquivo `calculos.py`:

python

```python
def dobro(x):
    return x * 2

print(dobro(5))
```

Se você roda `python calculos.py`, imprime `10`. Ótimo. Mas agora, em outro arquivo:

python

```python
import calculos   # imprime 10 na tela, sem você pedir!
```

Ao **importar**, o Python executa o arquivo inteiro, então o `print` roda junto. Normalmente você só queria reaproveitar a função `dobro`.

**A solução**

python

```python
def dobro(x):
    return x * 2

if __name__ == '__main__':
    print(dobro(5))
```

Agora:

- `python calculos.py` → imprime `10`
- `import calculos` → não imprime nada, e a função `dobro` fica disponível

**Como funciona por dentro**

Todo arquivo Python tem uma variável automática chamada `__name__`:

- Se o arquivo foi **executado diretamente**, `__name__` vale `"__main__"`.
- Se foi **importado**, `__name__` vale o nome do módulo (`"calculos"`).

Então a condição `__name__ == '__main__'` pergunta: "este arquivo está sendo o programa principal?". Se sim, o bloco roda. Se foi importado, o bloco é ignorado.

**Teste você mesmo**

Crie um arquivo com apenas:

python

```python
print(__name__)
```

Rode-o diretamente e veja `__main__`. Depois importe-o de outro arquivo e veja o nome do módulo aparecer.

**Resumo em uma frase:** o bloco `if __name__ == '__main__'` significa "só execute isto se eu for o arquivo que foi rodado, e não se alguém me importou".

Isso é muito usado em projetos reais, então você vai ver esse padrão o tempo todo.
