import numpy as np
import matplotlib.pyplot as plt
import random


def dice(dicetype, rolls):

    values = np.random.randint(1, dicetype+1, rolls)
    i = 0
    for value in values:
        new_dice_value = 0
        if value == dicetype:
            exploding = True
            while exploding == True:
                new_dice = random.randint(1, dicetype + 1)
                if new_dice != dicetype:
                    exploding = False
                new_dice_value = new_dice + new_dice_value
        values[i] = value + new_dice_value
        i = i + 1
        plt.hist(values, 6)
        plt.show()
    return values


def main():
    pass

if __name__ == "__main__":
    main()