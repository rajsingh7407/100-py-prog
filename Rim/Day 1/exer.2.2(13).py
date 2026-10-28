import sys
sys.path.insert(0,"../../src")
from course_tools import check, check_output
print("setup complete ")

x = 3
y = 4
x = x + y
y = x - y
x = x - y
final_x = 4
final_y = 3
check(final_x, 4)
check(final_y, 3)
      