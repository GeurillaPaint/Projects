# most common generator used is range.
# range does not return values between the indicated number, but instead a stream in the range 0-5.
#
# Here is an example of the simple range generator:

# variable=[]
# for i in range(5):
#     variable.append(i)
#  This returns a range list, [0, 1, 2, 3, 4]

# You also have list comprehension which is something like this:
xyz = [i for i in range(5)]
print(xyz)

# which is equal to saying this:
xyz = []
for i in range(5):
    xyz.append(i)
print(xyz)
# python is intelligent enough to know what you want, and you can just make a simple one liner as mentioned
# rather than using up 3 fucking lines of code. Yea, fuck that.

# But generators are also able to be simplified. Here's the difference between a list comp and a generator:

# List comp
xyz = [i for i in range(5)]
# generator
xyz = (i for i in range(5))

# the parenthesis make the difference. generators won't store the value to memory, though they're slower.

# you cannot directly print the generator, cause you will get returned that it's a generator. you have to iterate

# ex:

xyz = (i for i in range(5))
print(xyz)
# this returns the value <generator object <genexpr> at 0x0000000002A9D480>

for i in xyz:
    print(i)
# This takes the value from the generator and iterates it. We ask for the value of i in the variable,
# which according to the generator is any/all numbers within its 5 range. then we ask to print that number.
# the code returns the entire array of possibilities which is written in a column, 0 through 4.


# -------------------------------------------------------------------------------------------------------------


# In the cases you want to take your iteration data and manipulate it, cause you want more than a list comp
# or a generator.. consider the following:

input_list = [5, 6, 2, 10, 15, 20, 5, 2, 1, 3]
# div_by_five function created here, takes any number and tells us if it's divisible by 5.


def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False


xyz = (i for i in input_list if div_by_five(i))
# again, python is smart. The code before you is a shorthand or liscomp of the following:
#
# xyz = []
# for i in input_list:
#   if div_by_five(i):
#       xyz.append(i)
for i in xyz:
    print(i)
# The above, which returns the result of that generator, can also be simplified, but only in python3. in 2,
# don't be fucking lazy and do the for argument cause the print doesn't work in python 2 brackets.
# EXAMPLE IN 3:    [print(i) for i in xyz]

# It gets pretty complicated if you make it. Here's an example:

xyz = [i for i in input_list if div_by_five(i)]
# [[print(i,ii) for ii in range(5)] for i in range(5)]

# had to # that print cause it wont work in 2. But basically we embed a couple iterations in to each other
# allowing us to make something that returns every combination of 2 numbers within the range of 5.
# Here is an example of what that top code should do:
for i in range(5):
    for ii in range(5):
        print i, ii
# incidentally, you could remove the print and run the code in 2.7 as this:
xyz = [[(i,ii) for ii in range(5)] for i in range(5)]
print(xyz)
# i chose [] for the i,ii butyou can do () to make them tuples, or even {:} for dictionary.

# in regards to huge data pools, if you make a list, say for a range of 99999999999999999999999 for whatever stupid
# reason, with a list you will run out of memory. Generators, you will run out of time.
