from turtle import Turtle 

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        # now inside the paddle class we just use self
        self.color("white")
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
    def go_up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(), new_y)
    def go_down(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(), new_y)



# we want bounce logic in the paddle - distance logic- less than a certain ammount 








