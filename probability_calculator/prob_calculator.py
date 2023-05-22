import random
import copy
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for color, amount in kwargs.items():
            for _ in range(amount):
                self.contents.append(color)

    def draw(self, amount):
        if amount > len(self.contents):
            return self.contents
        hat_instance = self.contents
        pulled_balls = []
        for _ in range(amount):
            pulled_ball = random.choice(hat_instance)
            pulled_balls.append(pulled_ball)
            hat_instance.remove(pulled_ball)
        return pulled_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    sucessful_experiments = 0
    for _ in range(num_experiments):
        sample_balls = {}
        for ball in hat.draw(num_balls_drawn):
            sample_balls[ball] = sample_balls.get(ball, 0) + 1
        print(f"Sample: {sample_balls} Expected: {expected_balls}")
        if sample_balls == expected_balls:
            sucessful_experiments = sucessful_experiments + 1
    return sucessful_experiments

hat1 = Hat(yellow=1, blue=1, green=6, red=6)

probability = experiment(hat1, expected_balls={"red":2, "green" : 2}, 
            num_balls_drawn=4, num_experiments=1000)

print(probability)