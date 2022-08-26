from typing import Optional

from fs.bfile import BFile
from fs.parquet_file import ParquetFile
from fs.pickle_file import PickleFile


def get_file(file_format: str) -> Optional[BFile]:
    file = None

    match file_format:
        case ParquetFile.format_name:
            file = ParquetFile()
        case PickleFile.format_name:
            file = PickleFile()

    return file
