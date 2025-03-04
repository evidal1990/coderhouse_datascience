import os
import matplotlib.pyplot as plt
import seaborn as sns
from graph.graph import Graph


class ViolinPlot(Graph):

    def draw(self):
        plt.figure(figsize=(8, 6))
        sns.violinplot(data=self.data, x=self.x, y=self.y, **self.kwargs)
        plt.title(self.title)

    def save(self):
        super().save("violinplot")
