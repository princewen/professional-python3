import functools
import time

def sortable_by_creation_time(cls):

    original_init = cls.__init__

    @functools.wraps(original_init)
    def new_init(self,*args,**kwargs):
        original_init(self,*args,**kwargs)
        self._created = time.time()

    cls.__init__ = new_init

    cls.__lt__ = lambda self,other:self._created < other._created
    cls.__gt__ = lambda self,other:self._created > other._created

    return cls



@sortable_by_creation_time
class Sortable(object):
    def __init__(self,identifier):
        self.identifier = identifier

    def __repr__(self):
        return self.identifier


first = Sortable('first')
second = Sortable('second')
third = Sortable('third')

print (sorted([second,first,third]))
