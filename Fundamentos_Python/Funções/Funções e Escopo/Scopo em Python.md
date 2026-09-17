# O que é Scope em Python e como ele funciona?

O escopo determina onde você pode usar uma variável no seu código.

Python tem regras adicionais de escopo. Por enquanto, foque no escopo local e global.

Uma variável criada fora de uma função tem escopo global. Você pode usá-la tanto dentro quanto fora das funções.

Uma variável criada dentro de uma função tem escopo local. Você só pode usá-la dentro dessa função. Parâmetros de função também são variáveis locais.

Aqui está um exemplo de escopo local e global:

```python
tax_rate = 0.1

def calculate_tax(price):
    tax = price * tax_rate
    return tax

print(calculate_tax(50)) # 5.0
print(tax_rate) # 0.1
print(tax) # NameError: name 'tax' is not defined
```

A variável `tax_rate` é global porque foi criada fora da função. A função `calculate_tax` pode lê-la, e a segunda chamada de `print()` também pode lê-la.

O parâmetro `price` e a variável `tax` são locais para `calculate_tax`. Eles estão disponíveis enquanto essa função executa, mas não fora dela. A última chamada de `print()` gera um `NameError` porque `tax` não está definido no escopo global.
