#values = [75,45,65,456]
def log(sequence, message, *values):
    if not values:
        print('%s:%s' %(sequence, message))
    else:
        values_str = ','.join(str(x) for x in values)
        print('%s:%s: %s'%(sequence, message, values_str))


def my_generator():
    for i in range(100):
        yield i

def my_func(*args):
    print(args)


