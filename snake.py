from ai import AI

class Snake:
    def __init__(self, location, length=3):
        x,y = location
        self.death = False
        self.ai = AI()
        self.body = [(x,y+i) for i in range(length)]

    def eat(self,x,y):
        self.body.append((x,y))

    def move(self, eating=False):
        direction = self.ai.move(self)
        x,y = self.body[0]
        if direction == "N":
            self.body.insert(0,(x,y-1))
        elif direction == "S":
            self.body.insert(0,(x,y+1))
        elif direction == "E":
            self.body.insert(0,(x+1,y))
        else:
            self.body.insert(0,(x-1,y))

        if not eating: self.body.remove(self.body[-1])
