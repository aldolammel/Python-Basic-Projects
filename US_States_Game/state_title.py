from turtle import Turtle


class StatesTitle(Turtle):
    def __init__(self, state, position):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.1, 0.1, 0.1)
        self.color("black")
        self.penup()
        self.goto(position)
        self.write(state, align="left", font=("Arial", 10, "normal"))


