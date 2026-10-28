import sys
sys.path.insert(0,"../../src")
from course_tools import check, check_output
print("setup complete ")
planet = 'mars'
moons = 4
check(planet,'mars')
check(moons,4)