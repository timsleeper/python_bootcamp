import sys

if len(sys.argv) > 1:
    if not sys.argv[1].isnumeric() or len(sys.argv) != 2:
        print("ERROR")
    elif int(sys.argv[1]) == 0:
        print("I'm Zero.")
    elif int(sys.argv[1]) % 2 == 0:
        print("I'm Even.")
    elif int(sys.argv[1]) % 2 != 0:
        print("I'm Odd.")