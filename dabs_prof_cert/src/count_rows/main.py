import argparse
import sys
sys.path.append("../../src")
<<<<<<< HEAD
from helpers import read_table, row_count
=======
from helpers import read_table
>>>>>>> 077ddd3491fdfa872d18e9cfb452bdc99a1ec8a2

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read a table and display its contents.")
    parser.add_argument("--table", type=str, required=True, help="The name of the table to read.")
    args = parser.parse_args()
    df = read_table(args.table)
    rows_count = row_count(df)
    print(f"Total rows in table {args.table}: {rows_count}")