from abc import ABC, abstractmethod
import pandas as pd

class IBigQueryClient(ABC):
    @abstractmethod
    def run_query(self, query: str) -> pd.DataFrame:
        pass
