import sys
sys.path.insert(0,"../../src")
from course_tools import check, check_output
print("setup complete ")
word = "Python"
two_lines = "Hello World\nThis is a test"
columns = "A\tB\tC"
check(two_lines, "Hello World\nThis is a test")
check(columns, "A\tB\tC")