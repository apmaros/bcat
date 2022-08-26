import gzip
import _pickle as cPickle
from typing import IO
from fs.bfile import BFile
from fs.compression import Compression


class PickleFile(BFile):
    format_name = "pickle"

    @staticmethod
    def get_lines(src: str, count: int, compression=None):
        with _get_file(src, compression) as f:
            return cPickle.load(f.read(count))

dd
def _get_file(src, compression) -> IO:
    if compression is None:
        return open(src, "rb")
    if compression.value == Compression.GZIP:
        return gzip.open(src, "rb")
    else:
        raise ValueError(
            f"Compression {compression} not supported "
            f"for {PickleFile.format_name}"
        )
