import functools

def require_ints(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        kwargs_value=[i for i in kwargs.values()]
        for arg in list(args)+kwargs_value:
            if not isinstance(arg,int):
                raise TypeError("{} only accepts integers as arguments.".format(func.__name__))
        return func(*args,**kwargs)
    return wrapper


@require_ints
def foo(x,y):
    """Return the sum of x and y"""
    return x+y

#抛出异常，只接受整数作为参数
#print (foo(3,4.2))

#输出8
print (foo(3,5))
# Help on function foo in module __main__:
#
# foo(x, y)
#     Return the sum of x and y


print (help(foo))