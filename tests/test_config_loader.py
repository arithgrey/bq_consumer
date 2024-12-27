import unittest
import os
from bq_consumer.config_loader import ConfigLoader

class TestConfigLoader(unittest.TestCase):
    
    def test_load_config_success(self):
        # Asumimos que el archivo config.py existe en el directorio bq_consumer/
        config_loader = ConfigLoader("bq_consumer/config.py")
        config = config_loader.get_config()
        self.assertIn("project_id", config)
        self.assertIn("allowed_universes", config)
    
    def test_load_config_file_not_found(self):
        # Probar si el archivo config.py no se encuentra
        with self.assertRaises(FileNotFoundError):
            ConfigLoader("bq_consumer/non_existent_config.py")
    
    def test_config_contains_expected_keys(self):
        # Verificar si el archivo de configuración tiene las claves esperadas
        config_loader = ConfigLoader("bq_consumer/config.py")
        config = config_loader.get_config()
        self.assertEqual(config["project_id"], "findep-calidad-uat-mx")
        self.assertIsInstance(config["allowed_universes"], list)

if __name__ == "__main__":
    unittest.main()
