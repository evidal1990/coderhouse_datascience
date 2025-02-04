import os
import json
import pandas as pandas

from dotenv import load_dotenv
from file.file_processor import FileProcessor
from graph.graph_generator import GraphGenerator

CURRENT_COLUMN = "against_ghost"


def main():
    load_dotenv(override=True)

    try:
        df = pandas.read_csv(os.getenv("CURRENT_FILE_PATH"))
        if not isinstance(df, pandas.core.frame.DataFrame):
            raise Exception("O arquivo informado não é um dataframe.")

        if json.loads(os.getenv("ENABLE_DF_INFOS").lower()):
            FileProcessor().write_df_infos_file(
                dataframe=df
            )
        if json.loads(os.getenv("ENABLE_DF_STATS").lower()):
            FileProcessor().write_df_stats_file(
                dataframe=df
            )
        if json.loads(os.getenv("ENABLE_DF_COLUMNS_VALUE_COUNTS").lower()):
            FileProcessor().write_df_column_value_counts(
                dataframe=df,
                column=CURRENT_COLUMN
            )
        if json.loads(os.getenv("ENABLE_DF_COLUMNS_STATS").lower()):
            FileProcessor().write_df_column_stats(
                dataframe=df
            )

        if json.loads(os.getenv("ENABLE_BOX_PLOT_GRAPH").lower()):
            graph_generator = GraphGenerator()
            graph_generator.draw_box_plot(
                dataframe=df,
                column=CURRENT_COLUMN
            )

        if json.loads(os.getenv("ENABLE_SWARM_PLOT_GRAPH").lower()):
            graph_generator = GraphGenerator()
            graph_generator.draw_swarmplot(
                dataframe=df,
                column=CURRENT_COLUMN
            )

    except Exception as exception:
        print(exception)


main()
