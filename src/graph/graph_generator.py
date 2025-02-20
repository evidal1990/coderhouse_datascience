from dotenv import load_dotenv
from graph.box_plot import BoxPlot
from graph.swarmplot import Swarmplot
from graph.violinplot import ViolinPlot


class GraphGenerator:

    def __init__(self):
        load_dotenv(override=True)

    def draw_box_plot(self, dataframe, x, y, src):

        box_plot = BoxPlot(
            data=dataframe,
            x=x,
            y=y,
            title="Boxplot",
            src=src,
            palette="viridis"
        )
        box_plot.draw()
        box_plot.save()

    def draw_swarmplot(self, dataframe, column):

        swarmplot = Swarmplot(
            data=dataframe,
            y=column,
            title=f'Swarmplot ({column})',
            src=column
        )
        swarmplot.draw()
        swarmplot.save()

    def draw_violinplot(self, dataframe, column):

        violinplot = ViolinPlot(
            data=dataframe,
            y=column,
            title=f'Violin ({column})',
            src=column
        )
        violinplot.draw()
        violinplot.save()
