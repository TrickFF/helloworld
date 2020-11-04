import moda
from folderB.modb import foo, bar
# import modc - выполняется весь код сразу при импорте
from modc import foo # Также выполняется весь код модуля

print(moda.foo)
moda.bar()

print(foo)
bar()