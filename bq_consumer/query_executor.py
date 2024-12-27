import re
from bq_consumer.bigquery_connector import BigQueryConnector
from bq_consumer.config_loader import ConfigLoader
import pandas as pd

class QueryExecutor:
    def __init__(self):
        # Cargar la configuración automáticamente al crear la instancia
        config_loader = ConfigLoader()
        self.config = config_loader.get_config()

    def execute(self, query: str) -> pd.DataFrame:
        self._is_valid_query(query)
        project_id = self.config.get("project_id", "")
        connector = BigQueryConnector(project_id)
        
        # Ejecutar la consulta
        return connector.execute_query(query)

    def _is_valid_query(self, query: str):
        """
        Valida que la consulta sea un SELECT y que no contenga comandos no permitidos como UPDATE, DELETE, etc.
        """
        # Validar que la consulta sea un SELECT
        if not query.lstrip().startswith("SELECT"):
            raise ValueError("Consulta no permitida: solo se permiten consultas SELECT")

        # Validación para asegurarse de que no se utilicen comandos peligrosos (UPDATE, DELETE, etc.)
        invalid_commands = r"\b(update|delete|insert|alter|drop)\b"
        if re.search(invalid_commands, query, re.IGNORECASE):  # Usamos re.IGNORECASE para no preocuparnos por mayúsculas/minúsculas
            raise ValueError("Consulta no permitida: comandos como UPDATE, DELETE, INSERT, ALTER, DROP no están permitidos")

        # Validación de la tabla consultada en allowed_universes
        allowed_universes = self.config.get("allowed_universes", [])
        if not any(universe in query for universe in allowed_universes):
            raise ValueError("Consulta no permitida: la tabla consultada no está en el universo permitido")
