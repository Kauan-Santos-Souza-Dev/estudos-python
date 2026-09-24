## A instrução `raise` no Python

### A ideia central

Normalmente o Python gera erros sozinho (dividir por zero, abrir um arquivo que não existe). O `raise` permite que **você** dispare um erro de propósito, quando percebe que algo está errado segundo as regras do seu programa.

É como um alarme: você decide quando ele toca.

### 1. Uso básico

python

```python
def check_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative')
    return age

try:
    check_age(-5)
except ValueError as e:
    print(f'Error: {e}')  # Error: Age cannot be negative
```

- `raise` + tipo da exceção + mensagem.
- A função **para na hora** ao encontrar o `raise`. O `return` nem chega a ser executado.
- Quem chamou a função trata o erro com `try/except`.

### 2. Relançar o erro (`raise` sozinho)

Dentro de um `except`, um `raise` sem nada depois **repassa o mesmo erro** para cima.

python

```python
def process_data(data):
    try:
        return int(data) * 2
    except ValueError:
        print('Logging: Invalid data received')  # registra o problema
        raise  # repassa o mesmo ValueError

try:
    process_data('abc')
except ValueError:
    print('Handled at higher level')
```

Serve para fazer algo com o erro (log, limpeza) sem "engoli-lo": ele continua subindo pela pilha de chamadas até alguém tratá-lo.

### 3. Exceções personalizadas

Você pode criar seus próprios tipos de erro herdando de `Exception`:

python

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f'Insufficient funds: ${balance} available, ${amount} requested')

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    withdraw(100, 150)
except InsufficientFundsError as e:
    print(f'Transaction failed: {e}')
```

Vantagens:

- O nome do erro já diz o que aconteceu.
- Você pode guardar dados extras (`balance`, `amount`) no próprio erro.
- Dá para capturar **só esse erro**, sem misturar com outros.

_(Não se preocupe com classes e herança agora; isso vem em lições futuras. Por ora, use como receita.)_

### 4. Encadear erros: `from`

Ao transformar um erro em outro, você escolhe como fica o histórico:

python

```python
def parse_config(filename):
    try:
        with open(filename, 'r') as file:
            return int(file.read())
    except FileNotFoundError:
        raise ValueError('Configuration file is missing') from None
    except ValueError as e:
        raise ValueError('Invalid configuration format') from e
```

|Forma|O que faz|
|---|---|
|`raise X from None`|**Esconde** o erro original. O traceback mostra só o novo, mais limpo.|
|`raise X from e`|**Liga** o novo erro ao original. O traceback mostra os dois ("the direct cause of...").|

Regra prática: use `from e` quando o erro original ajuda a depurar, e `from None` quando ele é só ruído para quem lê.

### 5. `assert`: um atalho

python

```python
def calculate_square_root(number):
    assert number >= 0, 'Cannot calculate square root of negative number'
    return number ** 0.5
```

`assert condição, mensagem` equivale a "se a condição for falsa, faça `raise AssertionError(mensagem)`".

⚠️ Um cuidado que o texto não menciona: o Python pode **desativar** os `assert` (ao rodar com `python -O`). Use `assert` para checagens internas durante o desenvolvimento, e use `raise` de verdade para validar dados de usuários ou regras de negócio.

### Resumo

|Quero...|Uso|
|---|---|
|Sinalizar um erro|`raise ValueError('mensagem')`|
|Repassar o erro que acabei de capturar|`raise` (sem argumentos)|
|Um erro com nome e dados próprios|classe que herda de `Exception`|
|Trocar um erro por outro mantendo o histórico|`raise Novo from e`|
|Trocar um erro por outro escondendo o original|`raise Novo from None`|
|Checagem rápida durante o desenvolvimento|`assert condição, 'mensagem'`|

### Por que isso importa

Em aplicações reais (principalmente no back end), o `raise` é como você **impõe regras**: rejeitar dados inválidos, bloquear operações proibidas e dar mensagens claras do que deu errado. Isso deixa o código mais previsível e mais fácil de depurar.
