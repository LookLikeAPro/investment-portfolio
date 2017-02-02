__all__ = []

import sys
import os
def setup_path():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(os.path.join(BASE_DIR, "lib"))
setup_path()
