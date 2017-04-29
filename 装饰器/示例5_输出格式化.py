import functools
import json

class JSONOutputError(Exception):
    def __init__(self,message):
        self._message = message
    def __str__(self):
        return self._message

def json_output(func):
    """Run the decorated function,serialize the result of that funciton to Json
    ,and return the JSON string.
    """
    @functools.wraps(func)
    def inner(*args,**kwargs):

        try:
            result = func(*args, **kwargs)
        except JSONOutputError as ex:
            result = {
                'status':'error',
                'message':str(ex),
            }
        return json.dumps(result)

    return inner

@json_output
def do_nothing():
    return {'status':'none'}

@json_output
def error():
    raise JSONOutputError("This function is erratic")

if __name__ == '__main__':
    print (do_nothing())
    print (error())