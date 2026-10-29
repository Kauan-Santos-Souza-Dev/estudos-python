"""
Objetivo: Cumprir as user stories abaixo e fazer todos os testes passarem para completar o laboratório.

Histórias de Usuário:

Você deve criar uma classe chamada Planet.
A classe Planet deve ter um método __init__ que:
Possui quatro parâmetros: self, name, planet_type e star.
Lança um TypeError com a mensagem name, planet type, and star must be strings se algum dos argumentos passados não for do tipo string.
Levanta um ValueError com a mensagem name, planet_type, and star must be non-empty strings se algum dos argumentos passados for uma string vazia.
Atribui os valores passados aos atributos da instância name, planet_type e star.
A classe Planet deve ter um método orbit que retorna uma string no formato {name} is orbiting around {star}....
A classe Planet deve ter um método __str__ que retorne uma string no formato Planet: {name} | Type: {planet_type} | Star: {star}.
Você deve criar três instâncias da classe Planet chamadas planet_1, planet_2 e planet_3.
Você deve imprimir cada objeto planet para ver a saída do método __str__.
Você deve chamar o método orbit em cada objeto planeta e imprimir o resultado.
"""

class Planet:
    def __init__(self,name,planet_type,star):
        if not isinstance(name, str) or not isinstance(planet_type, str) or not isinstance(star, str):
            raise TypeError('name, planet type, and star must be strings')
        if name == "" or planet_type == "" or star == "":
            raise ValueError('name, planet_type, and star must be non-empty strings')
        self.name = name
        self.planet_type = planet_type
        self.star = star

    def orbit(self):
        return f'{self.name} is orbiting around {self.star}...'  
    
    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'
    
planet_1 = Planet('Earth', 'Terrestrial', 'Sun')
planet_2 = Planet('Mars', 'Terrestrial', 'Sun')
planet_3 = Planet('Jupiter', 'Gas Giant', 'Sun')

print(planet_1)
print(planet_2)
print(planet_3)

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())

