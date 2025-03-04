import os
import pandas as pandas

from dotenv import load_dotenv
from menu.main_menu import MainMenu


def main():
    load_dotenv(override=True)

    try:
        df = pandas.read_csv(os.getenv("CURRENT_FILE_PATH"), encoding="latin")
        if not isinstance(df, pandas.core.frame.DataFrame):
            raise Exception("O arquivo informado não é um dataframe.")

        main_menu = MainMenu(df=df)
        main_menu.print_options()

    except Exception as exception:
        print(exception)


main()
