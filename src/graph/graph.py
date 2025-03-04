import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class Graph():

    def __init__(self, data: pd.DataFrame, x: str, y: str, src: str, title: str, type: str, **kwargs):
        self.data = data
        self.x = x
        self.y = y
        self.src = src
        self.title = title
        self.type = type
        self.figure_width = 8
        self.figure_height = 6
        self.kwargs = kwargs

    def draw_boxplot(self):
        plt.figure(
            figsize=(
                self.figure_width,
                self.figure_height
            )
        )
        sns.boxplot(
            data=self.data,
            x=self.x,
            y=self.y,
            **self.kwargs
        )
        plt.title(self.title)

    def draw_violinplot(self):
        plt.figure(
            figsize=(
                self.figure_width,
                self.figure_height
            )
        )
        sns.violinplot(
            data=self.data,
            x=self.x,
            y=self.y,
            **self.kwargs
        )
        plt.title(self.title)

    def draw_barplot(self):
        plt.figure(
            figsize=(
                self.figure_width,
                self.figure_height
            )
        )
        sns.barplot(
            data=self.data,
            x=self.x,
            y=self.y,
            **self.kwargs
        )
        plt.title(self.title)

    def draw_swarmplot(self):
        plt.figure(
            figsize=(
                self.figure_width,
                self.figure_height
            )
        )
        sns.swarmplot(
            data=self.data,
            x=self.x,
            y=self.y,
            **self.kwargs
        )
        plt.title(self.title)

    def save(self):
        path = f'results/{self.src}'
        if not os.path.exists(path):
            os.makedirs(path)

        plt.savefig(f'{path}/{self.y}_{self.type}.png',
                    dpi=300, bbox_inches='tight')
