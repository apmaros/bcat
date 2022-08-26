from abc import ABC, abstractmethod
from typing import List, Dict

from fs.compression import Compression


class BFile(ABC):
    @abstractmethod
    def format_name(self):
        raise "Not implemented"

    @staticmethod
    @abstractmethod
    def get_lines(
            src: str, count: int, compression: Compression = None
    ) -> List[Dict]:
        raise "Not implemented"
