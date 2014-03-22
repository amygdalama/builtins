import __builtin__

print "Before importing b"
print __builtin__ is __builtins__

import b

print "In a, after importing b"
print __builtin__ is __builtins__