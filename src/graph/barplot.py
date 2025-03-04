import os
import matplotlib.pyplot as plt
import seaborn as sns
from graph.graph import Graph


class BarPlot(Graph):
    def __init__(
            self,
            data=None,
            x=None,
            y=None,
            hue=None,
            hue_order=None,
            order=None,
            orient=None,
            color=None,
            palette=None,
            saturation=0.75,
            fill=True,
            width=0.8,
            gap=0,
            log_scale=None,
            native_scale=False,
            formatter=None,
            legend='auto',
            ax=None,
            title=None,
            src=None,
            type="barplot",
            estimator='mean',
            errorbar=('ci', 95),
            n_boot=1000,
            seed=None,
            units=None,
            weights=None,
            dodge='auto',
            capsize=0,
            err_kws=None
    ):
        super().__init__(
            data=data,
            x=x,
            y=y,
            hue=hue,
            hue_order=hue_order,
            order=order,
            orient=orient,
            color=color,
            palette=palette,
            saturation=saturation,
            fill=fill,
            width=width,
            gap=gap,
            log_scale=log_scale,
            native_scale=native_scale,
            formatter=formatter,
            legend=legend,
            ax=ax,
            title=title,
            src=src,
            type=type
        )

        self.estimator = estimator
        self.errorbar = errorbar
        self.n_boot = n_boot
        self.seed = seed
        self.units = units
        self.weights = weights
        self.dodge = dodge
        self.capsize = capsize
        self.err_kws = err_kws

    def draw(self):
        if self.data.empty:
            raise Exception("Dataframe não informado para desenhar o gráfico")

        plt.figure(figsize=(8, 6))
        sns.barplot(
            data=self.data,
            x=self.x,
            y=self.y,
            hue=self.hue,
            order=self.order,
            hue_order=self.hue_order,
            estimator=self.estimator,
            errorbar=self.errorbar,
            n_boot=self.n_boot,
            seed=self.seed,
            units=self.units,
            weights=self.weights,
            orient=self.orient,
            color=self.color,
            palette=self.palette,
            saturation=self.saturation,
            fill=self.fill,
            width=self.width,
            dodge=self.dodge,
            capsize=self.capsize,
            err_kws=self.err_kws,
            ax=self.ax
        )

        if self.title:
            plt.title(self.title)
