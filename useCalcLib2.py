import calcLib2

print("Add from calclib2 import")
r = calcLib2.add(1,2,3,45)
print(r, calcLib2.test)

print("Add from calclib2 imported directly")
from calcLib2 import add
from calcLib2 import test
r = add(1,2,3,4)
print(r, test)

