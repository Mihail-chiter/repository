from random import *

class Player():
    def __init__(self, hp, bal, arm, old, lvl, hit):
        self.hp = hp
        self.bal = bal
        self.arm = arm
        self.old = old
        self.lvl = lvl
        self.hit = hit

    def print_info(self):
        print('здоровье', self.hp)
        print('денги', self.bal)
        print('brona', self.arm)
        print('old', self.old)
        print('lvl', self.lvl)
        print('hit', self.hit)

    def kick(self, enemy):
        enemy.arm -= self.hit
        if enemy.arm <= 0:
            enemy.hp -= self.hit
        print("hp p2", enemy.hp)
        print('arm p2', enemy.arm)

#p1 = Player(100, 435, 245, 234, 245, 543)
#p2 = Player(200, 3423, 342, 567, 1, 32)
#p1.kick(p2)

class Warion(Player):
    def __init__(self, hp, bal, arm, old, lvl, hit):
        super().__init__(hp, bal, arm, old, lvl, hit)

    def lech(self):
        print('Вы получили пизды')

class Swarion(Warion):
    def __init__(self, hp, bal, arm, old, lvl, hit):
        super().__init__(hp, bal, arm, old, lvl, hit)
    
    def oneshot(self):
        print('КАСТРИРОВАН')
#nik = Warion(hp=212, bal=23123, arm=123, old=282, lvl=28, hit=12374)

class Magpitux(Player):
    def __init__(self, hp, bal, arm, old, lvl, hit):
        super().__init__(hp, bal, arm, old, lvl, hit)
    
    def magpituh(self):
        self.hp += 10
        print('Здоровье персонажа:', self.hp)
        
    def magNEpituh(self):
        cislo = randint(1, 100)
        if cislo <= 10:
            print('Враг парализован')
        elif cislo == 74:
            print('вы парализованы')
        else:
            print('враг не парализован')

p1 = Magpitux(hp=100, bal=100, arm=80, old=282, lvl=28, hit=50)
p1.magpituh()
p1.magNEpituh()