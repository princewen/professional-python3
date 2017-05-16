"""
array模块定义了一个很像list的新对象类型，不同之处在于它限定了这个类型只能装一种类型的元素。array元素的类型是在创建并使用的时候确定的。

如果你的程序需要优化内存的使用，并且你确定你希望在list中存储的数据都是同样类型的，那么使用array模块很合适。举个例子，如果需要存储一千万个整数，如果用list，那么你至少需要160MB的存储空间，然而如果使用array，你只需要40MB。但虽然说能够节省空间，array上几乎没有什么基本操作能够比在list上更快。

在使用array进行计算的时候，需要特别注意那些创建list的操作。例如，使用列表推导式(list comprehension)的时候，会将array整个转换为list，使得存储空间膨胀。一个可行的替代方案是使用生成器表达式创建新的array。

"""

import array
#'i'代表list的类型，只能是integer的数据
a = array.array('i',[1,2,3,4,5])
b = array.array(a.typecode,(2*x for x in a))
#array('i', [1, 2, 3, 4, 5])
print (a)
#array('i', [2, 4, 6, 8, 10])
print (b)

"""因为使用array是为了节省空间，所以更倾向于使用in-place操作。一种更高效的方法是使用enumerate："""
for i,x in enumerate(a):
    a[i] = 2 * x
print (a)

"""对于较大的array，这种in-place修改能够比用生成器创建一个新的array至少提升15%的速度。

那么什么时候使用array呢？是当你在考虑计算的因素之外，还需要得到一个像C语言里一样统一元素类型的数组时。"""

import array
from timeit import Timer


def arraytest():
    a = array.array("i", [1, 2, 3, 4, 5])
    b = array.array(a.typecode, (2 * x for x in a))


def enumeratetest():
    a = array.array("i", [1, 2, 3, 4, 5])
    for i, x in enumerate(a):
        a[i] = 2 * x


if __name__ == '__main__':
    m = Timer("arraytest()", "from __main__ import arraytest")
    n = Timer("enumeratetest()", "from __main__ import enumeratetest")

    print (m.timeit())  # 5.22479210582
    print (n.timeit())  # 4.34367196717



