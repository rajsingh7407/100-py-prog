import sys
sys.path.insert(0,"../../src")
from course_tools import check, check_output
print("setup complete ")

principal = 1000
rate_percent = 5
years = 10

amount =round(principal * (1 + rate_percent / 100) ** years, 2)

balance = 1000
# three years of growth go here
balance *= 1.05
balance *= 1.05
balance *= 1.05
check(amount,187.09)
check(balance,9830852.9)

