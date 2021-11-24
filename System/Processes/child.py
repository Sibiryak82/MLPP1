# Пример 5.4.PP4E\System\Processes\child.py

import os, sys
print('Hello from child', os.getpid(), sys.argv[1])