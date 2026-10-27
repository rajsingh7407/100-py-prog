import sys
sys.path.insert(0, "../src")
from course_tools import check, check_output

print("setup complete") 

error_name = "SyntaxError"

check(error_name, "SyntaxError", hint="The error type is the word before the colon on the last line of the red message.")
