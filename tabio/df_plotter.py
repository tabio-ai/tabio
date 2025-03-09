import matplotlib.pyplot as plt


# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html
class DFPlotter(object):

    def __init__(self, df):
        self.df = df
        _, self.ax = plt.subplots()

    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.scatter.html
    def scatter(self, x=None, y=None):
        if x is None and y is None:
            x, y = self.df.columns[:2]
        self.df.plot.scatter(x, y, ax=self.ax)
        plt.show()

    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.line.html
    def line(self, x=None, y=None):
        if x is None and y is None:
            x, y = self.df.columns[:2]
        self.df.plot.line(x, y, ax=self.ax)
        plt.show()

    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.hist.html
    def hist(self, bins=10):
        self.df.iloc[:, 0].plot.hist(bins=bins, ax=self.ax)
        plt.show()
