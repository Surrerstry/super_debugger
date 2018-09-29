"""
Example of usage in kind of real time situation.
"""

from super_debugger import super_debugger
from time import sleep

val = 'a'
print(val)

super_debugger(ctrl_c_turn_on=True, sleeping_time=2, be_verbose=2)

# now press ctrl-c
# change context on that one that you want (most probably script stopped in super_debugger or signal library)
# check or change what you want
# have fun

sleep(20)

print(val)

