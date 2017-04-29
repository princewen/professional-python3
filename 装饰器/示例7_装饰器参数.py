import functools
import json

class JSONOutputError(Exception):
    def __init__(self,message):
        self._message = message
    def __str__(self):
        return self._message

def json_output(indent=None,sort_keys=False):
    """Run the decorated function,serialize the result of that funciton to Json
    ,and return the JSON string.
    """
    def actual_decorator(func):
        @functools.wraps(func)
        def inner(*args,**kwargs):

            try:
                result = func(*args, **kwargs)
            except JSONOutputError as ex:
                result = {
                    'status':'error',
                    'message':str(ex),
                }
            return json.dumps(result,indent=indent,sort_keys=sort_keys)
        return inner
    return actual_decorator

# 操作顺序很重要，首先执行函数调用json_output(indent=4)，得到actual_decorator
# 然后调用的结果再被应用到装饰器上，即相当于@actual_decorator
@json_output(indent=4)
def do_nothing():
    return {'status':'none'}

@json_output
def error():
    raise JSONOutputError("This function is erratic")

if __name__ == '__main__':
    print (do_nothing())
    #print (error())