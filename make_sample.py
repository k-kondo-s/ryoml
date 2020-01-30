import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class MakeSample:

    def make_sample(self):
        a = -1
        b = 5

        x = np.arange(0, 10, 0.1)
        # y = [a * i + b + np.random.randn() for i in x]
        # plt.plot(x, y, 'o')
        # plt.show()

        data_sample = [[i, a * i + b + np.random.randn()] for i in x]
        # print(data_sample)

        df = pd.DataFrame(data_sample)
        print(df)
        df.to_csv('./sample.csv', index=None, header=False)
