import os
import pandas as pandas

from dotenv import load_dotenv
from file.file_processor import FileProcessor
from graph.graph_generator import GraphGenerator
from const.analysis_type import AnalysisType


def main():
    load_dotenv()

    try:
        df = pandas.read_csv(os.getenv("CURRENT_FILE_PATH"))
        # print(df.head())

        if os.getenv("ENABLE_DF_INFOS"):
            FileProcessor().write_df_infos_file(dataframe=df)
        if os.getenv("ENABLE_DF_INFOS"):
            FileProcessor().write_df_stats_file(dataframe=df)
        if os.getenv("ENABLE_DF_INFOS"):
            FileProcessor().write_df_column_stats(dataframe=df)

        if os.getenv("ENABLE_BOX_PLOT_GRAPH"):
            graph_generator = GraphGenerator()
            graph_generator.draw_box_plot(
                AnalysisType.UNIVARIATE, df, os.getenv("CURRENT_ANALYSIS"))

    except Exception as exception:
        print(exception)


main()
