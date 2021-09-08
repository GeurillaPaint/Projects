import argparse
import sys
# argparse can be used to make a command line for your program, which can make the use of said code a bit easier
# to manage. variables can be changed on the fly, etc
#
# consider the following:
#
#  def calc(x, y, operation):
#     if operation == 'add':
#         return x + y
#     elif operation == 'sub':
#         return x - y
#     elif operation == 'mul':
#         return x * y
#     elif operation == 'div':
#         return x / y
#
#  operation = calc(7, 3, 'div')
#  print(operation)
#
# at this point, imports were applied to the global space above all this shit. it's up top.


#Example 1:
def main():
    parser = argparse.ArgumentParser()
    # parser is a variable using the argparse argument from import.
    # the below adds parser arguments in the form of lists. --x is the placeholder for the x parameter.
    # we then indicate the type of value, in this case x will be a float with a default of 1.0.
    # with that default, if we don't provide an argument, the code will use 1.0 as a default parameter.
    # help is a value that pops up to provide an explanative string. in this case its used to ask questions.
    # under operations, we just make the default add, so if we don't argue a parameter, it will auto
    # add instead.
    parser.add_argument('--x', type=float, default=1.0,
                        help='what is the first number?')
    parser.add_argument('--y', type=float, default=1.0,
                        help='what is the second number?')
    parser.add_argument('--operation', type=str, default='add',
                        help='what operation?(add, sub, mul, div)')
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))
    # sys.stdout.write brings data to console. calc is part of the import and calculates value.

# x, y, operations from previous code is changed to args variable for the function.
# then we add args. to everything.
def calc(args):
    if args.operation == 'add':
        return args.x + args.y
    elif args.operation == 'sub':
        return args.x - args.y
    elif args.operation == 'mul':
        return args.x * args.y
    elif args.operation == 'div':
        return args.x / args.y
# ensures if this is the script being run, we run this function, otherwise we dont run it.
# that way if this was ever imported, it wouldn't autorun.
if __name__ == '__main__':
    main()
# previous calc variable operation and print argument are now gone.

# This code can be brought up in the command line and run. by default, it will return 2.0, meaning the default
# values are applied, 1.0 + 1.0. If we run this in command prompt, navigating to the containing folder and then
# typing the name of the file, we can add parameters to it as an argument to opening it.
# example:
#
#    C:\Directory> argparseintr.py --x=5 --y=2 --operation=mul
#    10.0
#
# In the above example, we indicated the value of --x was 5, y was 2, and we asked to multiply. The result was
# the float 10.0
# you can also give the value -h to receive the help output as well to indicate what those values are and
# what they do.