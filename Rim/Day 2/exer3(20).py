import sys
sys.path.insert(0,"../../src")
from course_tools import check, check_output
print("setup complete ")

bill = 84.50
tip_percent = 18
people = 4

tip = bill*tip_percent/100
total = round(bill+tip,2)
per_person = round(total/people,2)

check(tip,15.21)
check(total,56.78)
check(per_person,34.78)