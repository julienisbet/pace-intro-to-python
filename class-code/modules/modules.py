# importing the entire module
import module1
import module2

# importing individual functions
# note that say_hello from module1 will be overwritten
from module1 import say_hello
from module2 import say_hello

# using an alias
from module1 import say_hello as sh1
from module2 import say_hello as sh2

# importing multiple functions
from module2 import say_hello, say_goodbye

print("My name is", __name__)
sh1()
sh2()

say_goodbye()
