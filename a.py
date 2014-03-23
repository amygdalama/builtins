import __builtin__

print "In a"
print "__name__ is:", __name__
print "__builtin__ is __builtins__:", __builtin__ is __builtins__
print "type(__builtin__):", type(__builtin__)
print "type(__builtins__):", type(__builtins__)
print "__builtins__ is __builtin__.__dict__", __builtins__ is __builtin__.__dict__