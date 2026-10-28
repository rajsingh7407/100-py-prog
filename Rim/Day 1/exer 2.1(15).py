import sys
sys.path.insert(0,"../../src")
from course_tools import check, check_output
print("setup complete ")

celsius = 25
fahrenheit = celsius*9/5+32

km = 42.195
miles = km*0.621371

hours = 2.5
minutes = hours*60
check(fahrenheit,77.0)
check(miles,26.21875)
check(minutes,150)