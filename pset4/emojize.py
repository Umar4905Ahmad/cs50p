import sys 

if len(sys.argv) < 2 :
    sys.exit("too few arguments")

for arg in sys.argv :
    print("Welcome to the underworld", arg)

    