import inspect
import sys
from os.path import basename


def pb(*args, out_file=sys.stderr):
    """ Print breakpoint """
    info = inspect.stack()[1]
    filename = basename(info.filename)
    line = info.lineno
    fn = info.function
    divider = '|' if args else ''
    meta = f'\033[92mpb\033[0m | {filename}:{line} in {fn} {divider}'
    print(meta, *args, file=out_file)
