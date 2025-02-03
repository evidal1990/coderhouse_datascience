import os
import pandas as pandas

from dotenv import load_dotenv
from file.file_processor import FileProcessor
from graph.graph_generator import GraphGenerator

CURRENT_COLUMN_ANALYSIS = "against_dark"
ANALYSIS_TYPE = {
    "UNIVARIATE": 0,
    "BIVARIATE": 1,
    "MULTIVARIATE": 2
}


def main():
    os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

    load_dotenv()

    try:
        df = pandas.read_csv(os.getenv("CURRENT_FILE_PATH"))
        if not isinstance(df, pandas.core.frame.DataFrame):
            raise Exception("O arquivo informado não é um dataframe.")
        print(df.head())

        if bool(os.getenv("ENABLE_DF_INFOS")):
            FileProcessor().write_df_infos_file(
                dataframe=df
            )
        if bool(os.getenv("ENABLE_DF_INFOS")):
            FileProcessor().write_df_stats_file(
                dataframe=df
            )
        if bool(os.getenv("ENABLE_DF_INFOS")):
            FileProcessor().write_df_column_stats(
                dataframe=df
            )

        if bool(os.getenv("ENABLE_BOX_PLOT_GRAPH")):
            graph_generator = GraphGenerator()
            graph_generator.draw_box_plot(
                ANALYSIS_TYPE["UNIVARIATE"], df, CURRENT_COLUMN_ANALYSIS)

        if bool(os.getenv("ENABLE_SWARM_PLOT_GRAPH")):
            graph_generator = GraphGenerator()
            graph_generator.draw_swarmplot(
                ANALYSIS_TYPE["UNIVARIATE"], df, CURRENT_COLUMN_ANALYSIS)

    except Exception as exception:
        print(exception)


main()
