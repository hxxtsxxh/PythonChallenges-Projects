# determine heads or tails of a coin
import random


class Coin:
    def __init__(self, trials):
        self.trials = trials

    def flip(self):
        count_heads = 0
        count_tails = 0
        for i in range(self.trials):
            val = random.randint(0, 1)
            if val == 0:
                print("Heads")
                count_heads += 1
            else:
                print("Tails")
                count_tails += 1
        print('')
        if count_heads > count_tails:
            print("Final Winner: Heads")
        elif count_tails > count_heads:
            print("Final Winner: Tails")
        else:
            print("No Winner")


coinOne = Coin(10)
coinOne.flip()
