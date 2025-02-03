import os

from dotenv import load_dotenv
from graph.box_plot import BoxPlot
from const import AnalysisType


class GraphGenerator:

    def __init__(self):
        load_dotenv()

    def draw_box_plot(self, analysis_type, dataframe, column):
        if analysis_type == AnalysisType.UNIVARIATE:
            box_plot = BoxPlot(
                data=dataframe,
                y=column,
                title=f'Boxplot ({column})',
                src=f'{os.getenv("RESULTS_UNIVARIATE_GRAPH_BOXPLOT_PATH")}'
            )
            if not os.path.exists(
                    os.getenv("RESULTS_UNIVARIATE_GRAPH_BOXPLOT_PATH")):
                os.makedirs(
                    os.getenv("RESULTS_UNIVARIATE_GRAPH_BOXPLOT_PATH"))
            box_plot.draw()
