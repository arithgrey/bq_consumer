from bigquery_connector import BigQueryConnector
from config_loader import ConfigLoader
import pandas as pd

class QueryExecutor:
    def __init__(self):
        # Carga la configuración automáticamente al crear la instancia
        config_loader = ConfigLoader()
        self.config = config_loader.get_config()

    def execute(self, query: str) -> pd.DataFrame:
        # Validamos si la consulta es permitida según el universo de configuraciones
        if not self._is_valid_query(query):
            raise ValueError("Query not allowed in this environment")
        
        # Conexión a BigQuery
        project_id = self.config.get("project_id", "")
        connector = BigQueryConnector(project_id)
        
        # Ejecutamos la consulta
        return connector.execute_query(query)

    def _is_valid_query(self, query: str) -> bool:
        """
        Validamos si la consulta está permitida según la configuración del archivo.
        """
        allowed_universes = self.config.get("allowed_universes", [])
        for universe in allowed_universes:
            if universe in query:
                return True
        return False
