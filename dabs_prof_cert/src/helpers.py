from pyspark.sql import DataFrame
from pyspark.sql import SparkSession

def read_table(table_name: str) -> DataFrame:
    """Read a table into a DataFrame."""
    spark = SparkSession.builder.getOrCreate()

    df = spark.table(table_name)
    
    return df

def row_count(df: DataFrame) -> int:
    """Return the number of rows in the DataFrame."""
    return df.count()