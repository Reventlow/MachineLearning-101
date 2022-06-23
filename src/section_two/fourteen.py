import matplotlib.pyplot as plt
from scipy import stats




import numpy as np

def mean_three(a: int, b: int, c: int):
    incomes = np.random.normal(a, b, c, 1000000000)
    return np.mean(incomes)

def hist(a: int, b: int, c: int):
    incomes = np.random.normal(a, b, c)
    plt.hist(incomes, 50)
    plt.show()

def mode_this(low: int, high: int, size: int):
    ages = np.random.randint(low, high, size)
    return ages

def stat_this(ages):
    return stats.mode(ages)

def main():
    pass


if __name__ == "__main__":
    main()