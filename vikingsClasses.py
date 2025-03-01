#Soldier
import random
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self,damage):
        self.health -= damage
    pass
# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
    
        super().__init__(health,strength)
        self.name = name
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health>0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"
    pass
# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health,strength)
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health>0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"
    pass
# War
class War:
    def __init__(self):
        
        self.vikingArmy = []
        self.saxonArmy =[]
    def addViking(self,Viking):
        self.vikingArmy.append(Viking)
    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)
    def vikingAttack(self):
        Snum = random.randint(0,len(self.saxonArmy)-1)
        Vnum = random.randint(0,len(self.vikingArmy)-1)
        self.saxonArmy[Snum].receiveDamage (getattr(self.vikingArmy[Vnum],"strength"))
        if getattr(self.saxonArmy[Snum],"health")>0:
            return f"A Saxon has received {getattr(self.saxonArmy[Snum],'strength')} points of damage"
        else:
            self.saxonArmy.remove(self.saxonArmy[Snum])
            return f"A Saxon has died in combat"
            
    def saxonAttack(self):
        Vnum = random.randint(0,len(self.vikingArmy)-1)
        Snum = random.randint(0,len(self.saxonArmy)-1)
        self.vikingArmy[Vnum].receiveDamage (getattr(self.saxonArmy[Snum],"strength"))
        if getattr(self.vikingArmy[Vnum],"health")>0:
            return f"{getattr(self.vikingArmy[Vnum],'name')} has received {getattr(self.saxonArmy[Snum],'strength')} points of damage"
            
        else:
            Vname=getattr(self.vikingArmy[Vnum],'name')
            self.vikingArmy.remove(self.vikingArmy[Vnum])
            return f"{Vname} has died in act of combat"
    def showStatus(self):
        if len(self.saxonArmy)==0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy)==0:
            return  "Saxons have fought for their lives and survive another day..."
        if len(self.saxonArmy)>=1 and len(self.vikingArmy)>=1:
            return "Vikings and Saxons are still in the thick of battle."
    