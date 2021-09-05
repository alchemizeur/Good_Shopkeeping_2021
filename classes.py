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
    def __init__(self, name, title, idn_poss,idn_subj, idn_verb, idn_verb_past, idn_third_present, health, maxHealth, level, strength, defense, magic, magic_defense, character_id,gold,inventory_name):
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
        self.inventory_name = inventory_name

        ## status section
        self.is_dead = False
        self.can_be_looted = True
        self.is_lootable = False

    def self_identify(self):
        print(f"Hello, my name is {self.name}. My health is {self.health}/{self.maxHealth}.")

    def self_identify_inventory(self):
        print(f"My inventory is called {self.inventory_name.name}.")
        if self.inventory_name.space > 1:
            print(f"Opening {self.name}'s inventory. There are currently {self.inventory_name.space} units remaining in a {self.inventory_name.maxSpace} unit bag. The contents are as follows:")
        else:
            print(f"Opening {self.name}'s inventory. There is currently {self.inventory_name.space} unit remaining in a {self.inventory_name.maxSpace} unit bag. The contents are as follows:")

    def take_damage(self,aggressor,dmg_amt,source): ## potions take negative damage, there is no need for a heal buff
        self.health -= dmg_amt
        if dmg_amt >= 0:
            print(f"{self.name} {self.idn_third_present} taken {dmg_amt} damage from {aggressor.name}'s {source}!")
        else:
            print(f"{self.name} {self.idn_third_present} healed {abs(dmg_amt)} damage from {aggressor.name}'s {source}!")
        if self.health <= 0:
            self.is_dead
            print(f"{self.name} {self.idn_third_present} died.")
            if self.can_be_looted:
                self.is_lootable
                print(f"You may now loot {self.name}'s remains.")
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
        print(f"{self.name}. {self.description} Takes up {self.space} units in inventory, and is worth {self.base_worth} gold in the general market.")


@dataclass
class Inventory():
    def __init__(self, name,space, maxSpace,items): ## could be a problem if there are two characters with the same name, but we wont encouter that
        self.name = name
        self.space = space
        self.maxSpace = maxSpace
        self.items = items ## json


    def add_item(self): ##add, remove item from inventory
        print('add item')

    def remove_item(self):
        print('remove item')

    def add_inventory_space(self):
        print('permanently adds inventory space')

your_inv = Inventory('Cuckoo\'s Inventory',10,10,{})
yous = Character('Cuckoo','the bird','her','she','is','was','has',10,10,1,5,5,5,5,1000,10,your_inv)
wolfies_inv = Inventory('Wolfie\'s Inventory',10,10,{})
wolfie = Character('Wolfie','the wolf','his','he','is','was','has',10,10,1,5,5,5,5,2000,10,wolfies_inv)
potion = Item('Health Potion',1,'A simple health potion. Heals 3 points.',5)

yous.self_identify()
yous.take_damage(wolfie,5,'scratch')
yous.self_identify()
yous.take_damage(wolfie,-100,'health potion')
yous.self_identify()
yous.take_damage(wolfie,5,'scratch')
yous.take_damage(wolfie,6,'scratch')
yous.self_identify()
yous.self_identify_inventory()
potion.identify()



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