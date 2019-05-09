import time

def decorate(func):
    def timer(*args, **kwargs):
        s1 = time.strftime('%X') + ' > '
        logg(s1)
        print(s1, end='')
        func(*args, **kwargs)
        s2 = '\n' + time.strftime('%X') + ' > %s行动结束\n' % args[0].nickname
        logg(s2)
        print(time.strftime('%X') + ' > %s行动结束\n' % args[0].nickname)
    return timer

def logg(ar, **kwargs):
    file = open('File_test/Game_log.txt', mode='a+', encoding='utf-8')
    file.write(ar)
    file.flush()
    file.close()


class Warrior:
    blood = 50
    attack = 10
    defense = 10

    def __init__(self, nickname):
        self.nickname = nickname


    @decorate
    def att(self, other):
        temp = self.attack - other.defense
        other.blood -= temp
        self.s =  "%s攻击了%s，%s扣了%s血量" % (
            self.nickname, other.nickname, other.nickname, temp)
        print(self.s)
        logg(self.s)
        return self.s


    @decorate
    def move(self):
        print("战士正在徒步")


lingting = Warrior("聆听")
moran = Warrior("墨染")
lingting.att(moran)

# lingting.move()
