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
        pulled_balls = []
        for _ in range(amount):
            pulled_ball = random.choice(self.contents)
            pulled_balls.append(pulled_ball)
            self.contents.remove(pulled_ball)
        return pulled_balls
    
def compare_samples(sample, expected):
    for x, y in expected.items():
        if x not in sample or y > sample.get(x, 0):
            return False
    return True 

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    sucessful_experiments = 0
    hat_instance = copy.copy(hat.contents)
    for _ in range(num_experiments):
        sample_balls = {}
        for ball in hat.draw(num_balls_drawn):
            sample_balls[ball] = sample_balls.get(ball, 0) + 1
        if compare_samples(sample_balls, expected_balls):
            sucessful_experiments += 1
        hat.contents = copy.copy(hat_instance)
    return sucessful_experiments / num_experiments
