from dataclasses import dataclass

# Character | Capaple of having a name, health stats, holding inventory, fighting, dying, retreating, can be looted
#   Player | Capable of equipping inventory
# item | can be picked up, dropped, take up space
#   story item
#   Consumable
#   Weapon
# inventory | Capable of being held by a character, space (units), holding items



@dataclass
class Character():
    def __init__(self, name, title, idn_poss,idn_subj, idn_verb, idn_verb_past, idn_third_present, health, maxHealth, level, strength, defense, magic, magic_defense, character_id,gold):
        self.name = name
        self.title = title
        self.idn_poss = idn_poss                        ## possessive for corresponding identity (her)
        self.idn_subj = idn_subj                        ## subject for corresponding identity (she)
        self.idn_verb = idn_verb                        ## verb for corresponding identity (is)
        self.idn_verb = idn_verb_past                   ## verb for corresponding identity, past (was)
        self.idn_third_present = idn_third_present      ## verb for third person present, (has)
        self.health = health
        self.maxHealth = maxHealth                      #int
        self.level = level
        self.strength = strength
        self.defense = defense
        self.magic = magic
        self.magic_defense = magic_defense
        self.character_id = character_id                #for matching inventory
        self.gold = gold

        ## status section
        self.is_dead: False

    def self_identify(self):
        print(f"Hello, my name is {self.name}. My health is {self.health}/{self.maxHealth}.")

    def take_damage(self,aggressor,dmg_amt,source): ## potions take negative damage, there is no need for a heal buff
        self.health -= dmg_amt
        if dmg_amt >= 0:
            print(f"{self.name} {self.idn_third_present} taken {dmg_amt} damage from {aggressor.name}'s {source}!")
        else:
            print(f"{self.name} {self.idn_third_present} healed {abs(dmg_amt)} damage from {aggressor.name}'s {source}!")
        if self.health <= 0:
            self.is_dead = True
            print(f"{self.name} {self.idn_third_present} died.")
        if self.health > self.maxHealth:
            self.health = self.maxHealth
        if self.health < 0:
            self.health = 0


@dataclass
class Item():
    def __init__(self, name, space, description, base_worth):
        self.name = name
        self.space = space
        self.description = description
        self.base_worth = base_worth

    ## maybe this shouldn't be a subclass...

    def identify(self):
        print(f"{self.name}. {self.description} Takes up {self.space} units in inventory, and is worth {self.base_worth} gold.")


@dataclass
class Inventory():
    def __init__(self, owner, space, maxSpace): ## could be a problem if there are two characters with the same name, but we wont encouter that
        self.character_id = {owner.character_id}
        self.space = space
        self.maxSpace = maxSpace
        self.items = {} ## json

    def identify(self):
        print(f"Opening {owner.name}'s inventory. There is currently {self.space} units remaining in a {self.maxspace} unit bag. The contents are as follows:")
#       if self_items =






you = Character('Cuckoo','the bird','her','she','is','was','has',10,10,1,5,5,5,5,1000,10)
your_inv = Inventory('you',100,100)
wolfie = Character('Wolfie','the wolf','his','he','is','was','has',10,10,1,5,5,5,5,2000,10)
potion = Item('Health Potion',1,'A simple health potion. Heals 3 points.',5)

you.self_identify()
you.take_damage(wolfie,5,'scratch')
you.self_identify()
you.take_damage(wolfie,-100,'health potion')
you.self_identify()
you.take_damage(wolfie,5,'scratch')
you.take_damage(wolfie,6,'scratch')
you.self_identify()
potion.identify()
your_inv.identify()



'''   def exchange_money(self,):


@dataclass
class Item():
    name: str
    units: int




## SUBCLASSES

@dataclass
class Player(Character):
    health: float = 100.0
    maxHealth: float = 200.0
    level: int = 1
    strength: int = 5
    defense: int = 5
    magic: int = 5
    magic_defense: int = 5


def ADD_WEAPON(weapontoadd):
    weapons.append(weapontoadd)
    
    def deal_damage(self, character):
        character.take_damage(self.attack_value)
        character.poison(self.poison_duration, self.poison_amt)'''