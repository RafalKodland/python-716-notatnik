class CustomTurtle():
    color = "red"

    def set_color(self, new_color):
        self.color = new_color
    
    def forward(self, length):
        print(f"Żółw rysuje linie o długości {length} i o kolorze {self.color}")
    
t1 = CustomTurtle()
t2 = CustomTurtle()

t1.set_color("green")

t1.forward(100)
t2.forward(50)

class BetterTurtle(CustomTurtle):
    def test(self):
        print("Test nowej funkcji")

t3 = BetterTurtle()

t3.test()