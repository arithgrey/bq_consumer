from .contracts import IBigQueryClient
import pandas as pd

class QueryService:
    """
    Servicio que expone un método para obtener datos.
    Depende de la interfaz IBigQueryClient, no de la implementación concreta.
    """

    def __init__(self, client: IBigQueryClient):
        self._client = client

    def fetch_data(self, query: str) -> pd.DataFrame:
        return self._client.run_query(query)
