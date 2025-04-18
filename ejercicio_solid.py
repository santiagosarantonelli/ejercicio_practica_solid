from abc import ABC, abstractmethod

class atackManager(ABC): # Clase maestra
    @abstractmethod # Metodo abstracto
    def attack(self, superhero):
        pass

# Implementaciones concretas (Tipos de ataque, podemos agregar los que quisieramos gracias a la clase maestra)
# Clase ataque de puño
class PunchAttack(atackManager):
    # Solicitamos el superheroe
    def attack(self, superhero):
        # Devolvemos el ataque
        return f"{superhero.name} attacks with a powerfull punch!!!!" #

# Clase ataque laser
class LaserAttack(atackManager):
    # Solicitamos el superheroe
    def attack(self, superhero):
        # Devolvemos el ataque
        return f"{superhero.name} attacks with a long laser!!!!"
    
# Clase ataque bola de fuego
class FireballAttack(atackManager):
    # Solicitamos el superheroe
    def attack(self, superhero):
        # Devolvemos el ataque
        return f"{superhero.name} attacks with a fire ball!!!!"
    
# Clase ataque bola de fuego
class IceballAttack(atackManager):
    # Solicitamos el superheroe
    def attack(self, superhero):
        # Devolvemos el ataque
        return f"{superhero.name} attacks with a ice ball!!!!"

# Clase base de los superheroes
class Superhero:
    def __init__(self, name, healt, atackManager) -> None:
            self.name = name
            self.healt = healt
            self.atackManager = atackManager
    
    # Funcion para realizar su ataque
    def attack(self):
         return self.atackManager.attack(self)
     
# Clase base sobre el juego
class Game:
    def __init__(self) -> None:
            # Creamos una lista con todos los superheroes
            self.superheroes = []

    # Funcion que agrega superheroes al juego
    def add_superheroes(self, superhero):
         self.superheroes.append(superhero)

    # Funcion para mostrar todos los ataques de los superheroes
    def superheroe_action(self):
         # Recorremos la lista de los superheroes dentro del juego
         for superhero in self.superheroes:
              # Mostramos sus ataques
              print(superhero.attack())

# Modo de uso
game = Game()

# Creamos dichos superheroes
Superman = Superhero("Superman", 100, PunchAttack())
Cyclops = Superhero("Cyclops", 80, LaserAttack())
Ace = Superhero("Ace", 100, FireballAttack())
Iceman = Superhero("Iceman", 100, IceballAttack())

# Los agregamos al juego
game.add_superheroes(Superman)
game.add_superheroes(Cyclops)
game.add_superheroes(Ace)
game.add_superheroes(Iceman)

game.superheroe_action()