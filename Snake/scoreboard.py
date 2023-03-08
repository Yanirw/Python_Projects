from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 28,"normal")
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt", mode="r") as high_score:
            high_score_var = high_score.read()
            self.high_score = int(high_score_var)
        self.current_score = 0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_scoreboard()

               
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.current_score}   High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("data.txt", mode="w") as high_score:
                high_score.write(f"{self.high_score}")
                
        self.current_score = 0
        self.update_scoreboard    


    def game_over(self):
        self.goto(-110,0)
        self.write("GAME OVER", font=("Arial", 30,"bold"))
   

    
    def update_score(self):
        self.current_score += 1 
        self.update_scoreboard()

