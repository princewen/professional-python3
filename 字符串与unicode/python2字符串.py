#-*-coding:utf-8 -*-#
"""
作者：文文
内容：python2的字符串
版本：python2.7
"""
import sys
"""
python2中也有两种字符串，不过，python3中的str类在python2中名称为unicode,但是，python3中的bytes类在python2中名称为str类。
这意味着在python3中str类是一个文本字符串，而在python2中str类是一个字节字符串。
若不使用前缀实例化字符串，则返回一个str类（这里是字节字符串！！！），如果想要得到一个文本字符串，需要在字符串前面加上u字符。
"""

byte_str = 'The quick brown fox jumped over the lazy dogs'
#output : <type 'str'>
print type(byte_str)

text_str = u'The quick brown fox jumped over the lazy dogs'
#output : <type 'unicode'>
print type(text_str)

"""
与python3不同的是，python2会在文本字符串和字节字符串之间尝试进行隐式转换。
该工作机制是，如果解释器遇到一个不同种类的字符串混合操作，解释器首先会将字节字符串转换为文本字符串，然后对文本字符串进行操作。
解释器在将字节字符串转换为文本字符串的过程中使用隐式解码，python2中默认编码几乎总是ASCII.
我们可以使用sys.getdefaultencoding 方法来查看默认编码方式。
"""
#output :  foobar
print 'foo'+u'bar'

#output : ascii
print sys.getdefaultencoding()

#output : False
print 'foo'==u'bar'

#Output : bar
d = {u'foo':'bar'}
print d['foo']

"""
python2中，调用encode方法可以将任意类型的字符串转换为字节字符串，或使用decode将任意类型的字符串转换为文本字符串
在实际使用中，这容易使人迷惑并导致灾难，考虑下面的例子：
如下所示，下面这段代码报错了，在第一个encode之后，已经将字符串按照utf-8格式转换为字节字符串，由于还有一个encode过程，首先会存在一个隐式解码过程，将字节字符串先解码为文本字符串，
这里将会使用默认的隐式转换方式，即getgetdefaultencoding()得到的方式，这里为ascii编码，因此下面的语句相当于：
text_str.encode('utf-8').decode('ascii').encode('utf-8')
"""

text_str = u'\u03b1 is for alpha'

# Traceback (most recent call last):
#   File "/Users/shixiaowen/python3/python高级编程/字符串与unicode/python2字符串.py", line 48, in <module>
#     print text_str.encode('utf-8').encode('utf-8')
# UnicodeDecodeError: 'ascii' codec can't decode byte 0xce in position 0: ordinal not in range(128)

print text_str.encode('utf-8').encode('utf-8')



"""
python2中，无论以何种方式打开文件，read方法总是返回一个字节字符串
"""
# <type 'str'>
# Python中有两种不同的字符串数据，文本字符串与字节字符串，两种字符串之间可以互相转换
# 本章将会学到文本字符串和字节字符串的区别，以及这两类字符串在python2和python3中的区别。
with open('字符串与unicode','r') as f:
    text_str=f.read()
    print (type(text_str))
    print text_str


