import inspect
import sys


def pd(*args):
    """ Print debugging. """
    callerframerecord = inspect.stack()[1]
    frame = callerframerecord[0]
    info = inspect.getframeinfo(frame)
    filename = info.filename.rsplit('/', 1)[-1]
    line = info.lineno
    fn = info.function
    divider = '|' if args else ''
    meta = f'\033[92mpd | {filename}:{line} in {fn}() {divider}'
    args += ('\033[00m', )
    print(meta, *args, file=sys.stderr)
