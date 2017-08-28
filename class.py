class My :
    pop = 0
    def __init__(self, name):
        self.name = name
        My.pop += 1
    def say(self):
        print My.pop, '. hi', self.name
        
    @classmethod
    def how_many(cls):
        print cls.pop
        
class derived(My):
    def __init__(self, name, add):
        My.__init__(self, name)
        self.add = add

m = My('sfe')
m.say()
m2 = My('number2')

m2.say()
My.how_many()

m3 = derived('seungwon', 'suwon')
m3.say()

f = open('/home/zezeon/poem.txt')
while True:
    l = f.readline()
    if len(l) == 0: break
    print(l)

