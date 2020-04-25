import sys

usage_msg = """Usage: python operations.py <number1> <number2>
Example:\n\tpython operations 10 3
"""

if len(sys.argv) < 3:
    print(usage_msg)
elif len(sys.argv) > 3:
    print('InputError: too many arguments\n\n' + usage_msg)
elif sys.argv[1].isnumeric() == False or sys.argv[2].isnumeric() == False:
    print('InputError: only numbers\n\n' + usage_msg)
else:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print("Sum:\t\t" + str(a + b))
