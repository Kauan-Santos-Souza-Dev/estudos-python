
# Criar um Rastreador de Estatísticas de Personagem de Jogo

class GameCharacter:

# Método construtor
    def __init__(self, name):
        self._name = name
        self.health = 150
        self.mana = 50
        self._level = 1

# Propriedade Name
     # Getter que retorna nome.
    @property
    def name(self):
        return self._name

# Propriedade Health
    # Getter que retorna a saúde atual.
    @property
    def health(self):
        return self._health
    
    # Setter que limita a saúde entre 0 a 100
    @health.setter 
    def health(self, value):
        if value < 0:
            self._health = 0
        elif value > 100:
            self._health = 100
        else:
            self._health = value

# Propriedade Mana
    # Getter que retorna o mana atual.
    @property
    def mana(self):
        return self._mana

    # Setter que limita mana ao intervalo de 0 a 50
    @mana.setter
    def mana(self,valor):
        if valor < 0:
            self._mana = 0
        elif valor > 50:
            self._mana = 50
        else:
            self._mana = valor

# Getter para level que retorna o nível atual do personagem.
    @property
    def level(self):
        return self._level

# Método para incrementar o nível do personagem em 1.
    def level_up(self):
        self._level += 1
  # Usar um setter dentro de um método, basta atribuir pela property (sem o _)      
        self.health = 100 
        self.mana = 50
        print(f"{self.name} leveled up to {self.level}!")

# Método que retorna uma string formatada
    def __str__(self):
        return f"Name: {self._name}\nLevel: {self._level}\nHealth: {self._health}\nMana: {self._mana}"

# Instanciar 
character = GameCharacter('Arthur Morgan')

print(character.name)
print(character.health)
print(character.mana)

print(character.level)   # 1
character.level_up()
print(character)
