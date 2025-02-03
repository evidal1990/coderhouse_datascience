import os

from dotenv import load_dotenv
from graph.box_plot import BoxPlot
from graph.swarmplot import Swarmplot


class GraphGenerator:

    def __init__(self):
        load_dotenv(override=True)

    def draw_box_plot(self, dataframe, column):
        box_plot = BoxPlot(
            data=dataframe,
            y=column,
            title=f'Boxplot ({column})',
            src=f'{os.getenv("RESULTS_UNIVARIATE_GRAPH_PATH")}'
        )
        if not os.path.exists(
                f'{os.getenv("RESULTS_UNIVARIATE_GRAPH_PATH")}'):
            os.makedirs(
                f'{os.getenv("RESULTS_UNIVARIATE_GRAPH_PATH")}')
        box_plot.draw()

    def draw_swarmplot(self, dataframe, column):
        swarmplot = Swarmplot(
            data=dataframe,
            y=column,
            title=f'Swarmplot ({column})',
            src=f'{os.getenv("RESULTS_UNIVARIATE_GRAPH_PATH")}'
        )
        if not os.path.exists(
                f'{os.getenv("RESULTS_UNIVARIATE_GRAPH_PATH")}'):
            os.makedirs(
                f'{os.getenv("RESULTS_UNIVARIATE_GRAPH_PATH")}')
        swarmplot.draw()
