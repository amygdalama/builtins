import __builtin__

print "In b, before importing a"

# the output from this should be the same as when we ran
# $ python a.py
print "__name__ is:", __name__
print "__builtin__ is __builtins__:", __builtin__ is __builtins__
print "type(__builtin__):", type(__builtin__)
print "type(__builtins__):", type(__builtins__)
print "\n"

import a
# code from a will execute here