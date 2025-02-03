import matplotlib.pyplot as plt
import seaborn as sns


class BoxPlot:

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
        saturation=0.75,
        fill=True,
        dodge="auto",
        width=0.8,
        gap=0,
        whis=1.5,
        linecolor="auto",
        linewidth=None,
        fliersize=None,
        hue_norm=None,
        native_scale=False,
        log_scale=None,
        formatter=None,
        legend="auto",
        ax=None,
        title=None,
        src=None
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
        self.saturation = saturation
        self.fill = fill
        self.dodge = dodge
        self.width = width
        self.gap = gap
        self.whis = whis
        self.linecolor = linecolor
        self.linewidth = linewidth
        self.fliersize = fliersize
        self.hue_norm = hue_norm
        self.native_scale = native_scale
        self.log_scale = log_scale
        self.formatter = formatter
        self.legend = legend
        self.ax = ax
        self.title = title
        self.src = src

    def draw(self):
        if self.data.empty:
            raise Exception("Dataframe não informado para desenhar o gráfico")

        plt.figure(figsize=(8, 6))
        sns.boxplot(
            data=self.data,
            x=self.x,
            y=self.y,
            hue=self.hue,
            order=self.order,
            hue_order=self.hue_order,
            orient=self.orient,
            color=self.color,
            palette=self.palette,
            saturation=self.saturation,
            fill=self.fill,
            dodge=self.dodge,
            width=self.width,
            gap=self.gap,
            whis=self.whis,
            linecolor=self.linecolor,
            linewidth=self.linewidth,
            fliersize=self.fliersize,
            hue_norm=self.hue_norm,
            native_scale=self.native_scale,
            log_scale=self.log_scale,
            formatter=self.formatter,
            legend=self.legend,
            ax=self.ax
        )
        plt.title(self.title)
        plt.savefig(f'{self.src}{self.y}', dpi=300, bbox_inches='tight')
