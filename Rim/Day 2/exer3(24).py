import sys
sys.path.insert(0,"../../src")
from course_tools import check, check_output
print("setup complete ")

import math

x1, y1 = 1, 2
x2, y2 = 4, 6

distance = math.sqrt((x2-x1)**2 + (y2 - y1)**2)
check(distance, 5.0)