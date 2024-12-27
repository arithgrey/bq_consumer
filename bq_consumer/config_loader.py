import os
import importlib.util

class ConfigLoader:
    def __init__(self, config_file: str = "config.py"):
        self.config_file = config_file
        self.config = self._load_config()

    def _load_config(self):
        """
        Carga el archivo .py que contiene la configuración, y lo evalúa para obtener el diccionario.
        """
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"El archivo de configuración '{self.config_file}' no se encuentra.")
        
        spec = importlib.util.spec_from_file_location("config", self.config_file)
        config_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(config_module)
        
        return config_module.CONFIG

    def get_config(self):
        return self.config
