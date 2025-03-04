import os
import matplotlib.pyplot as plt
import seaborn as sns


class Graph():

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
            type=""
    ):
        self.data = data
        self.x = x
        self.y = y
        self.hue = hue
        self.hue_order = hue_order
        self.order = order
        self.orient = orient
        self.color = color
        self.palette = palette
        self.saturation = saturation
        self.fill = fill
        self.width = width
        self.gap = gap
        self.log_scale = log_scale
        self.native_scale = native_scale
        self.formatter = formatter
        self.legend = legend
        self.ax = ax
        self.title = title
        self.src = src
        self.type = type

    def save(self):
        path = f'results/{self.src}'
        if not os.path.exists(path):
            os.makedirs(path)

        plt.savefig(f'{path}/{self.y}_{self.type}.png',
                    dpi=300, bbox_inches='tight')
