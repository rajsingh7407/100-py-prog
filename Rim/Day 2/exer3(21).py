import sys
sys.path.insert(0,"../../src")
from course_tools import check, check_output
print("setup complete ")

total_seconds = 98765

hours = total_seconds//3600
minutes = total_seconds//60
seconds = total_seconds%60
check(hours,4)
check(minutes,78)
check(seconds,5)