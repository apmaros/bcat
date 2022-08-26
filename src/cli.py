import argparse
import json
from os.path import exists

from fs.compression import Compression
from fs.file import get_file
from fs.parquet_file import ParquetFile
from fs.pickle_file import PickleFile


def main():
    args = _parse_cli_args()

    lines = args.lines
    src = args.path
    compression = args.compression
    file_format = args.format

    if not exists(src):
        raise ValueError(f'File path={src} does not exist')

    file = get_file(file_format)

    if not file:
        raise ValueError(f'File format {format} not supported')

    recs = file.get_lines(src, lines, compression)

    print(json.dumps(recs[:lines]))


def _parse_cli_args():
    parser = argparse.ArgumentParser(description='Like a cat but for binary')
    parser.add_argument("--lines", '-l', type=int)
    parser.add_argument(
        '--format',
        '-f',
        choices=[
            ParquetFile.format_name,
            PickleFile.format_name
        ],
        required=True,
        help="File format"
    )
    parser.add_argument(
        '--compression',
        '-c',
        choices=[
            Compression.GZIP
        ]
    )
    parser.add_argument(
        'path',
        help="Path to the file"
    )

    return parser.parse_args()


if __name__ == '__main__':
    main()
