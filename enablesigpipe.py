#exploit dev function that allows
#you to keep stdin open.  equiv to cat <(cat file.txt) - | ./testbin

#!/bin/python

from fcntl import fcntl, F_GETFL, F_SETFL
from os import O_NONBLOCK, read
import signal

def enable_sigpipe():

    signals = ('SIGPIPE', 'SIGXFZ', 'SIGXFSZ')
    for sig in signals:
        if hasattr(signal, sig):
            signal.signal(getattr(signal, sig), signal.SIG_DFL)
