import os
import matplotlib.pyplot as plt
import seaborn as sns


class ViolinPlot:

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
        inner="box",
        split=False,
        width=0.8,
        dodge="auto",
        gap=0,
        linewidth=None,
        linecolor="auto",
        cut=2,
        gridsize=100,
        bw_method="scott",
        bw_adjust=1,
        density_norm="area",
        common_norm=False,
        hue_norm=None,
        formatter=None,
        log_scale=None,
        native_scale=False,
        legend="auto",
        ax=None,
        inner_kws=None,
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
        self.inner = inner
        self.split = split
        self.dodge = dodge
        self.width = width
        self.gap = gap
        self.linecolor = linecolor
        self.linewidth = linewidth
        self.cut = cut
        self.gridsize = gridsize
        self.bw_method = bw_method
        self.bw_adjust = bw_adjust
        self.density_norm = density_norm
        self.common_norm = common_norm
        self.hue_norm = hue_norm
        self.native_scale = native_scale
        self.log_scale = log_scale
        self.formatter = formatter
        self.legend = legend
        self.ax = ax
        self.inner_kws = inner_kws
        self.title = title
        self.src = src

    def draw(self):
        if self.data.empty:
            raise Exception("Dataframe não informado para desenhar o gráfico")

        plt.figure(figsize=(8, 6))
        sns.violinplot(
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
            inner=self.inner,
            split=self.split,
            dodge=self.dodge,
            width=self.width,
            gap=self.gap,
            linecolor=self.linecolor,
            linewidth=self.linewidth,
            cut=self.cut,
            gridsize=self.gridsize,
            bw_method=self.bw_method,
            bw_adjust=self.bw_adjust,
            density_norm=self.density_norm,
            common_norm=self.common_norm,
            hue_norm=self.hue_norm,
            native_scale=self.native_scale,
            log_scale=self.log_scale,
            formatter=self.formatter,
            legend=self.legend,
            ax=self.ax,
            inner_kws=self.inner_kws
        )
        plt.title(self.title)

    def save(self):
        path = f'results/{self.src}'
        if not os.path.exists(path):
            os.makedirs(path)

        plt.savefig(f'{path}/{self.y}_violinplot.png',
                    dpi=300, bbox_inches='tight')
