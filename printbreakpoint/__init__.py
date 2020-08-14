import inspect
import sys


def pb(*args):
    """ Print breakpoint """
    callerframerecord = inspect.stack()[1]
    frame = callerframerecord[0]
    info = inspect.getframeinfo(frame)
    filename = info.filename.rsplit('/', 1)[-1]
    line = info.lineno
    fn = info.function
    divider = '|' if args else ''
    meta = f'\033[92mpb\033[0m | {filename}:{line} in {fn}() {divider}'
    print(meta, *args, file=sys.stderr)
