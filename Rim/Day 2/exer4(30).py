import sys
sys.path.insert(0,"../../src")
from course_tools import check, check_output
print("setup complete ")

typo = "Pxthon"

fixed = typo[0] + "y"+ typo[2:]
check(fixed, "Python")
