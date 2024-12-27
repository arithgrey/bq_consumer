from google.cloud import bigquery
import pandas as pd

class BigQueryConnector:
    def __init__(self, project_id: str):
        self.client = bigquery.Client(project=project_id)

    def execute_query(self, query: str) -> pd.DataFrame:
        query_job = self.client.query(query)
        results = query_job.result()
        return results.to_dataframe()
