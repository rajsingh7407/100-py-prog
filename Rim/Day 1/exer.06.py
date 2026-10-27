import sys
sys.path.insert(0,"../src")
from course_tools import check, check_output
print("setup complete ")

answer = 6 * 7
check(answer, 42, hint="Multiplication is written with *, so six times seven is 6 * 7.")
