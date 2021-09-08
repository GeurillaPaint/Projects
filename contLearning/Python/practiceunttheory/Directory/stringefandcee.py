# STRING CONCATENATION AND FORMATTING

#String Concatenation:

# Method 1 - simple list and print, basic concatenation
names = [
    'Jeff',
    'Gary',
    'Jill',
    'Rudolph\n' # \n added to segregate methods
]

for name in names:
    print('Hello to you, ' + name)

# Method 2 - .join method, built in python function. less readable, more function, basic concatenation
names = [
    'Alotta',
    'Capulet',
    'Mercutio',
    'Dionysis\n' # \n added to segregate methods
 ]

for name in names:
     print(' '.join(['Hello to you,', name]))


# Method 3 - importing, displaying and reading out a list.

import os

location_of_files = 'C:\\Users\\Patrick Hill\\projectlab\\practiceunttheory'
file_name = 'method3.txt'

print(location_of_files + '\\' + file_name)
# open does what it says it does.
# os.path.join is a join fn of os. we choose our listed variables from before and open them as f.
with open(os.path.join(location_of_files, file_name)) as f:
    print(f.read())  # here we call f which is listed as a path on windows and ask the system to open it.


#String formatting
# we are looking to print Gary bought 12 turnips today.
# consider the following.. with the given variables, it is tempting to run a string as this:
who = 'Gary'
how_many = 12
print(who + ' bought ' + str(how_many) + ' turnips today.')

# this statement works, but it is not the best method. even %s from a list is not the best way:
information = ('Gary', 12)
print('%s bought %s turnips today.' %(information))

#apparently the best way is to use {} and .format like so:
print ('{0} bought {1} turnips today.' .format(who, how_many))
# it appears that {} doesnt require numbers in py3. This code was run without numbers in py2 and worked fine.
# however in py2, it is ideal to have numbers in the brackets. Those numbers tell the code which item in the list
# to put in said bracket. So this is neat.
print ('{1} bought {0} turnips today.' .format(who, how_many))
#example of what happens when you swap the numbers.