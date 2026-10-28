import sys
sys.path.insert(0,"../../src")
from course_tools import check, check_output
print("setup complete ")

n = 4827
last_digit = n%10
without_last_digit = n//10  
tens_digit = without_last_digit%10 
check(last_digit,7)
check(without_last_digit,482)
check(tens_digit,2)