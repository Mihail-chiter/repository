class Player():
    def __init__(self, hp, bal, arm, old, lvl, hit):
        self.hp = hp
        self.bal = bal
        self.arm = arm
        self.old = old
        self.lvl = lvl
        self.hit = hit
        print('tst')

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

p1 = Player(100, 435, 245, 234, 245, 543)
p2 = Player(200, 3423, 342, 567, 1, 32)
p1.kick(p2)