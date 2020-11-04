# мы можем импортировать
import math
# но не можем импортировать наш модуль, например, из корня диска C

# как python находит модули?
import sys

print(type(sys.path))
for p in sys.path:
    print(p)

a = sys.path[0]
b = a[2]
sys.path.append('C:' + b)

import mymodule