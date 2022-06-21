import matplotlib.pyplot as plt



import numpy as np

def mean_three(a: int, b: int, c: int):
    incomes = np.random.normal(a, b, c)
    return np.mean(incomes)

def hist(a: int, b: int, c: int):
    incomes = np.random.normal(a, b, c)
    plt.hist(incomes, 50)
    plt.show()


def main():
    pass


if __name__ == "__main__":
    main()