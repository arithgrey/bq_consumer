from google.cloud import bigquery
import pandas as pd
from .contracts import IBigQueryClient

class DefaultBigQueryClient(IBigQueryClient):
    """
    Implementación 'real' que se conecta a BigQuery usando google-cloud-bigquery.
    Asume que las credenciales ya están configuradas en el entorno.
    """
    def __init__(self):
        self._client = bigquery.Client()

    def run_query(self, query: str) -> pd.DataFrame:
        query_job = self._client.query(query)
        return query_job.to_dataframe()
