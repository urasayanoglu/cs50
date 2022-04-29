import sys

"""try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguements")"""

if len(sys.argv) < 2:
    sys.exit("Too few arguements")

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)


    
