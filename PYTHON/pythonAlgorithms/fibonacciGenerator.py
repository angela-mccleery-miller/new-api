def fib(num):
    a,b = 0,1
    for i in xrange(0, num):
        # yield is a generator  / xrange behaves like a generator & yields one result at a time.  
        # where range puts the entire range of nums in memory at once.
        yield "{}: {}".format(i + 1, a)
        a, b = b, a + b

for item in fib(10):
    print(item)