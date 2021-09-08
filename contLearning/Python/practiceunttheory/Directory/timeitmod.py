# timeit allows you to time your code. timeit is equivalent to doing the following:
import time

start = time.time()
total = time.time() - start
"""
 Why would we use timeit when we could do this? The import time function as above is not precise enough for
 smaller snippets of code. Say you don't want to measure the entirety of your code, but just a section that
 seems to be running for too long. timeit is useful for that moment.
"""
import timeit
# print(timeit.timeit('1+3', number = 500000))
# here we have a sample timeit. This code will run the string 1+3 500,000 times. the return value will be how
# long it took to do this feat.

# consider the following code... you can actually use timeit to measure this code currently in """ by leaving
# it in """. Appending timeit to examplify:

print(timeit.timeit("""input_list = range(100)
def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False
    #generator
xyz = (i for i in input_list if div_by_five(i))

xyz = [i for i in input_list if div_by_five(i)]
""", number=5000))

# so we have a return of 0.0706399657503 when running this code 5000 times. Seems pretty cool.
# Keep in mind, within the triple quotes of timeit, it is its own little universe. Thus, you have to write it
# out like it is above. You can't shorten the code. Generally that won't be a problem, but just keep in mind.
# This is because it is seperated from any imports, functions, or classes outside of itself, so no list comp.
