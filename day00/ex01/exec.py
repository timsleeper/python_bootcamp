import sys

full_string = " ".join(sys.argv[1:])
rev_string = ""

for i in range(len(full_string)):
    rev_string = rev_string + full_string[-(i + 1)].swapcase()

if rev_string != "":
    print(rev_string)
