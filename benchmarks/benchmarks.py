# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.

import os
import time

def time_boo():
    print(os.environ)
    time.sleep(3)
