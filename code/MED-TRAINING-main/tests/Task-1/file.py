import sys

import placeholders
#from placeholders import *
#from basics import *
'''
def test_module_usage_needs_import():
    import module1
    print(module1.greet("jack"))
    

print(placeholders.__doc__)
'''

s1 = set()
s2 = set()
s3 = set()

s1 = set(dir())
from module3 import *
s2 = set(dir())
from module4 import *
s3 = set(dir())

print((s2 - s1))
print((s3 - s2))
