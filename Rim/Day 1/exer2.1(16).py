import sys
sys.path.insert(0,"../../src")
from course_tools import check, check_output
print("setup complete ")

price = 10
quantity = 3
total = price * quantity
price = 20
quantity = quantity + 1

total_after = 30
new_total = 80
check(total_after,30)
check(new_total,80)