import sys
from typing import Callable

from .types import IStdin, IStdout

def run_dev(_, main: Callable[[IStdin, IStdout], None]) -> None:
    main(sys.stdin, sys.stdout)