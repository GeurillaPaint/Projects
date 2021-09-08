"""
Returns a tuple of an interable.
"""

# example code. This is not really an enumerator but it returns what an enumerator would return.

example = ['left', 'right', 'up', 'down']

for i in range(len(example)):
    print(i, example[i])

#example of a proper enumerator:

for i, j in enumerate(example):
    print(i,j)

# WAAAAAAY simpleer than the previous example. i and j are placeholders for list placement and string value.
"""
Both codes, the improper and the proper, return the following value:
(0, 'left')
(1, 'right')
(2, 'up')
(3, 'down')

Though both codes are right, only the second one is a proper enumerator and is also sleeker and faster. There
is no reason to use the first code. It's bad form. So what's the point of taking this list and making 
enumerated tuples? Well, you can make dictionaries out of it.
"""
new_dictionary = dict(enumerate(example))

print(new_dictionary)

"""
Return value:
{0: 'left', 1: 'right', 2: 'up', 3: 'down'}
"""