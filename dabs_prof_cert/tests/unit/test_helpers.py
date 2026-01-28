from databricks.connect import DatabricksSession
from src import helpers 
import pytest

@pytest.fixture()
def pyspark_session():
    """Create a PySpark session for testing."""
    return DatabricksSession.builder.serverless(True).getOrCreate()

def test_row_count(pyspark_session):
    """Test the row_count helper function."""
    data = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
    columns = ["name", "id"]
    df = pyspark_session.createDataFrame(data, columns)
    
    count = helpers.row_count(df)
    
    assert count == 3, f"Expected row count to be 3, but got {count}"