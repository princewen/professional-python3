import functools
import logging
import time

def logged(func):
    """Cause the decorated method to be run and it's results logged, along with some other diagnostic information"""
    @functools.wraps(func)
    def inner(*args,**kwargs):
        start = time.time()
        return_value=func(*args,**kwargs)
        end=time.time()

        delta = end-start

        logger = logging.getLogger('decorator.logged')

        logger.warn('Called method {} at {} ; execution time is {}'.format(func.__name__,start,delta))
        logger.warn('result is {}'.format(return_value))
        return return_value
    return inner


@logged
def sleep_and_return(return_value):
    time.sleep(2)
    return return_value


print(sleep_and_return(5))


