import unittest
from unittest.mock import patch, MagicMock
from bq_consumer.query_executor import QueryExecutor
from bq_consumer.config_loader import ConfigLoader

class TestQueryExecutor(unittest.TestCase):

    # Eliminamos el mock del ConfigLoader para usar la configuración real
    def test_execute_query_success(self):
        # Utilizamos la configuración real en el archivo config.py
        executor = QueryExecutor()
        
        # Mock para el BigQueryConnector
        with patch('bq_consumer.query_executor.BigQueryConnector') as MockBigQueryConnector:
            mock_connector = MagicMock()
            MockBigQueryConnector.return_value = mock_connector
            mock_connector.execute_query.return_value = "dummy_dataframe"
            
            # Ejecutar el QueryExecutor con la consulta permitida
            result = executor.execute("SELECT * FROM `findep-calidad-uat-mx.MICROSERVICIOS.serv_caja_unica_acceso_cajas`")
            
            # Asegurarnos que la consulta fue ejecutada correctamente
            mock_connector.execute_query.assert_called_once_with("SELECT * FROM `findep-calidad-uat-mx.MICROSERVICIOS.serv_caja_unica_acceso_cajas`")
            self.assertEqual(result, "dummy_dataframe")

    def test_execute_query_invalid(self):
        # Utilizamos la configuración real en el archivo config.py
        executor = QueryExecutor()
        with self.assertRaises(ValueError):
            executor.execute("SELECT * FROM `other_project.other_dataset`")

    def test_execute_query_update(self):
        # Probar consulta UPDATE, debería ser rechazada
        executor = QueryExecutor()
        with self.assertRaises(ValueError):
            executor.execute("UPDATE `findep-calidad-uat-mx.MICROSERVICIOS.serv_caja_unica_acceso_cajas` SET campo = 'valor'")

    def test_execute_query_delete(self):
        # Probar consulta DELETE, debería ser rechazada
        executor = QueryExecutor()
        with self.assertRaises(ValueError):
            executor.execute("DELETE FROM `findep-calidad-uat-mx.MICROSERVICIOS.serv_caja_unica_acceso_cajas` WHERE campo = 'valor'")

    def test_execute_query_insert(self):
        # Probar consulta INSERT, debería ser rechazada
        executor = QueryExecutor()
        with self.assertRaises(ValueError):
            executor.execute("INSERT INTO `findep-calidad-uat-mx.MICROSERVICIOS.serv_caja_unica_acceso_cajas` (campo) VALUES ('valor')")

if __name__ == "__main__":
    unittest.main()
