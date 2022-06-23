import numpy as np
import matplotlib.pyplot as plt


def sdv(salary: float, vari: float, amount):
    incomes = np.random.normal(salary, vari, amount)

    plt.hist(incomes, 50)
    plt.show()
    print(incomes.std())
    print(incomes.var())

def main():
    pass


if __name__ == "__main__":
    main()
