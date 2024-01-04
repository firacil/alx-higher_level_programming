#!/usr/bin/python3
if __name__ == "__main__":
    import sys

arg_no = len(sys.argv) - 1  # exclude script

if arg_no == 0:
    print('{:d} arguments.'.format(arg_no))
elif arg_no == 1:
    print('{:d} argument:'.format(arg_no))
else:
    print('{:d} arguments:'.format(arg_no))

for i in range(1, len(sys.argv)):
    print(f'{i}: {sys.argv[i]}')
