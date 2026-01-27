import argparse
import sys
import os
from ..helpers import read_table


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Read a table and display its contents.")
#     parser.add_argument("--table", type=str, required=True, help="The name of the table to read.")
#     args = parser.parse_args()
#     df = read_table(args.table)
#     df.show() 