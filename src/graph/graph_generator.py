import os

from dotenv import load_dotenv
from graph.box_plot import BoxPlot
from graph.swarmplot import Swarmplot

ANALYSIS_TYPE = {
    "UNIVARIATE": 0,
    "BIVARIATE": 1,
    "MULTIVARIATE": 2
}


class GraphGenerator:

    def __init__(self):
        load_dotenv()

    def draw_box_plot(self, analysis_type, dataframe, column):
        if analysis_type == ANALYSIS_TYPE["UNIVARIATE"]:
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

    def draw_swarmplot(self, analysis_type, dataframe, column):
        if analysis_type == ANALYSIS_TYPE["UNIVARIATE"]:
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
