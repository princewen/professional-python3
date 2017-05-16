"""
weakref模块能够帮助我们创建Python引用，却不会阻止对象的销毁操作。这一节包含了weak reference的基本用法，并且引入一个代理类。

在开始之前，我们需要明白什么是strong reference。strong reference是一个对对象的引用次数、生命周期以及销毁时机产生影响的指针。strong reference如你所见，就是当你将一个对象赋值给一个变量的时候产生的：

"""
a = [1,2,3]
b = a
"""在这种情况下，这个列表有两个strong reference，分别是a和b。在这两个引用都被释放之前，这个list不会被销毁。"""


class Foo(object):
    def __init__(self):
        self.obj = None
        print('created')

    def __del__(self):
        print ('destroyed')

    def show(self):
        print (self.obj)

    def store(self, obj):
        self.obj = obj


a = Foo()  # created
b = a
del a
# <class '__main__.Foo'>
print (type(b))
del b

"""Weak reference则是对对象的引用计数器不会产生影响。当一个对象存在weak reference时，并不会影响对象的撤销。这就说，如果一个对象仅剩下weak reference，那么它将会被销毁。

你可以使用weakref.ref函数来创建对象的weak reference。这个函数调用需要将一个strong reference作为第一个参数传给函数，并且返回一个weak reference。"""
import weakref
a = Foo()
# <class 'weakref'>
b = weakref.ref(a)
print (type(b))
print (a)
"""一个临时的strong reference可以从weak reference中创建，即是下例中的b()："""
# True
print (a==b())
"""请注意当我们删除strong reference的时候，对象将立即被销毁。"""
"""如果试图在对象被摧毁之后通过weak reference使用对象，则会返回None："""
del a
# True
print (b() is None)


