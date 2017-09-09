#!/usr/bin/python
from urllib import unquote
import os, sys
for i in range(1, len(sys.argv)): os.rename(sys.argv[i], unquote(sys.argv[i]))
