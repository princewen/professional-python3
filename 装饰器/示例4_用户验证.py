class User(object):
    """A representation of a user in our application"""
    def __init__(self,username,email):
        self.username = username
        self.email = email


class AnonymousUser(User):
    """An anonymous user,a stand-in for an actual user that nonetheless is not an actual user"""

    def __init__(self):
        self.username=None
        self.email=None
    def __nonzero__(self):
        return False


import functools

def requires_user(func):
    @functools.wraps(func)
    def inner(user,*args,**kwargs):
        """Verify that the user is truthy; if so ,run the decorated method,and if not,raise ValueError"""
        if user and isinstance(user,User):
            return func(user,*args,**kwargs)
        else:
            return ValueError('A vaild user is required to run this.')
    return inner


@requires_user
def print_user(user):
    print ("user's username is {}".format(user.username))
    print ("user's email is {}".format(user.email))


if __name__ == '__main__':
    user = User('sxw','xxx@qq.com')
    print_user(user)