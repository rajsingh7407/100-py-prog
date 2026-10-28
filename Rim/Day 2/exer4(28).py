import sys
sys.path.insert(0,"../../src")
from course_tools import check, check_output
print("setup complete ")

date = "2026-10-18"

year = date[0:4]
month = date[5:7]
day = date[8:100]
uk_date = day +"/"+month +"/"+year
check(uk_date, "18/10/2026")