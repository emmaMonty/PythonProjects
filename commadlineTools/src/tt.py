#!/usr/bin/env python

from Concatenate import cat, tac
from CutPaste import cut, paste
from Grep import grep
from Partial import head, tail
from Sorting import sort
from WordCount import wc
from Usage import usage

import sys


if len(sys.argv) < 2:
    usage()
    sys.exit(1)
else:
    if sys.argv[1] == "cat":
        cat(sys.argv[2:])
    elif sys.argv[1] == "tac":
        tac(sys.argv[2:])
    elif sys.argv[1] == "wc":
        wc(sys.argv[2:]) 
    elif sys.argv[1] == 'head':
        head(sys.argv[2:])
    elif sys.argv[1] == 'tail':
        tail(sys.argv[2:])
    elif sys.argv[1] == 'grep':
        grep(sys.argv[2:])
    elif sys.argv[1] == 'sort':
        sort(sys.argv[2:])
    elif sys.argv[1] == 'cut':
        cut(sys.argv[2:])
    elif sys.argv[1] == 'paste':
        paste(sys.argv[2:])
