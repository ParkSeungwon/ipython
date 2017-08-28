import sys
import time

with open('name.py') as f:
    for line in f:
        print line,
        sys.stdout.flush()
        time.sleep(2)
    
        