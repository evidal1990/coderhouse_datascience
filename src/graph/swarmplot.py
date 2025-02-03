import matplotlib.pyplot as plt
import seaborn as sns


class Swarmplot:

    def __init__(
        self,
        data=None,
        x=None,
        y=None,
        hue=None,
        order=None,
        hue_order=None,
        orient=None,
        color=None,
        palette=None,
        size=5,
        edgecolor=None,
        linewidth=0,
        hue_norm=None,
        log_scale=None,
        native_scale=False,
        formatter=None,
        legend="auto",
        warn_thresh=0.05,
        ax=None,
        title=None,
        src=None,
    ):
        self.data = data
        self.x = x
        self.y = y
        self.hue = hue
        self.order = order
        self.hue_order = hue_order
        self.orient = orient
        self.color = color
        self.palette = palette
        self.size = size
        self.edgecolor = edgecolor
        self.hue_norm = hue_norm
        self.log_scale = log_scale
        self.native_scale = native_scale
        self.formatter = formatter
        self.legend = legend
        self.warn_thresh = warn_thresh
        self.ax = ax
        self.title = title
        self.src = src

    def draw(self):
        if self.data.empty:
            raise Exception("Dataframe não informado para desenhar o gráfico")

        plt.figure(figsize=(8, 6))
        sns.swarmplot(
            data=self.data,
            x=self.x,
            y=self.y,
            hue=self.hue,
            order=self.order,
            hue_order=self.hue_order,
            orient=self.orient,
            color=self.color,
            palette=self.palette,
            size=self.size,
            edgecolor=self.edgecolor,
            hue_norm=self.hue_norm,
            log_scale=self.log_scale,
            native_scale=self.native_scale,
            formatter=self.formatter,
            legend=self.legend,
            warn_thresh=self.warn_thresh,
            ax=self.ax
        )
        plt.title(self.title)
        plt.savefig(f'{self.src}/{self.y}_swarmplot.png',
                    dpi=300, bbox_inches='tight')
