import matplotlib.pyplot as pyplot
import seaborn as sns

from seaborn import boxplot
from const.graph_type import GraphType


class GraphGenerator():

    def __init__(self):
        pass

    def generate(self, dataframe, graphType):

        if graphType == GraphType.BOX_PLOT:
            pass
