
import sys
sys.path.insert(0,"../../src")
from course_tools import check, check_output
print("setup complete ")

first = 'second' 
last = 'first'
first,last = last,first
check(first,'first')
check(last,'second')