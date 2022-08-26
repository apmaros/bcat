from typing import List, Dict

import pyarrow.parquet as pq
from fs.bfile import BFile


class ParquetFile(BFile):
    format_name = "parquet"

    @staticmethod
    def get_lines(src, lines, compression=None) -> List[Dict]:
        if compression:
            raise ValueError("Compression is not supported for parquet")

        pf = pq.ParquetFile(src)
        df = next(pf.iter_batches(batch_size=lines)).to_pandas()

        return df.to_dict("records")
