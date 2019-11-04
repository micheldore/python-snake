import random

class AI:
    def move(self, snake):
        gothere = ["N","S","E","W"]
        xh,yh = snake.body[0]
        xb,yb = snake.body[1]
        try:
            if xh < xb:
                gothere.remove("E")
            elif xh > xb:
                gothere.remove("W")
            elif yh > yb:
                gothere.remove("N")
            else:
                gothere.remove("S")

            if xh+1 == 40:
                gothere.remove("E")
            elif xh-1 == 0:
                gothere.remove("W")
            elif yh-1 == 0:
                gothere.remove("N")
            elif yh + 1 == 40:
                gothere.remove("S")
        except:
            print("Error")
        return random.choice(gothere)
