"""
作者：文文
内容：python3的字符串
版本：python3.5
"""

"""
python语言有两种不同的字符串，一个用于存储文本，一个用于存储原始字节
文本字符串内部使用Unicode存储，字节字符串存储原始字节并显示ASCII
"""

"""
python3中，文本型字符串类型被命名为str，字节字符串类型被命名为bytes
正常情况下，实例化一个字符串会得到一个str实例，如果希望得到一个bytes实例，需要在文本之前添加b字符
"""

text_str = 'The quick brown fox jumped over the lazy dogs'
print (type(text_str)) #output : <class 'str'>


byte_str = b'The quick brown fox jumped over the lazy dogs'
print (type(byte_str)) #output : <class 'bytes'>

"""
可以在str与bytes之间进行类型转换，str类包含一个encode方法，用于使用特定编码
将其转换为一个bytes。于此类似，bytes类包含一个decode方法，接受一个编码作为
单个必要参数，并返回一个str。另一个需要注意的是，python3中永远不会尝试隐式地在
一个str与一个bytes之间进行转换，需要显式使用str.encode 或者 bytes.decode方法。
"""
#output :  b'The quick brown fox jumped over the lazy dogs'
print (text_str.encode('utf-8'))

#output : The quick brown fox jumped over the lazy dogs
print (byte_str.decode('utf-8'))

#output : False
print ('foo' == b'foo')

#Output : KeyError: b'foo'
d={'foo':'bar'}
print (d[b'foo'])

#Output : TypeError: Can't convert 'bytes' object to str implicitly
print ('foo'+b'bar')

#Output : TypeError: %b requires bytes, or an object that implements __bytes__, not 'str'
print (b'foo %s' % 'bar')

#output : bar b'foo'
print ('bar %s' % b'foo')


"""
读取文件
文件总是存储字节，因此，为了使用文件中读取的文本数据，必须首先将其解码为一个文本字符串。
python3中，文本正常情况下会自动为你解码，所以打开或读取文件会得到一个文本字符串。
使用的解码方式取决系统，在mac os 或者 大多数linux系统中，首选编码是utf-8，但windows不一定。
可以使用locale.getpreferredencoding()方法得到系统的默认解码方式。
"""

# <class 'str'>
# Python中有两种不同的字符串数据，文本字符串与字节字符串，两种字符串之间可以互相转换
# 本章将会学到文本字符串和字节字符串的区别，以及这两类字符串在python2和python3中的区别。
with open('字符串与unicode','r') as f:
    text_str=f.read()
    print (type(text_str))
    print (text_str)

import locale
#output : UTF-8
print (locale.getpreferredencoding())

"""
读取文件时可以显示声明文件的编码，使用open方法的encoding关键字
"""

# <class 'str'>
# Python中有两种不同的字符串数据，文本字符串与字节字符串，两种字符串之间可以互相转换
# 本章将会学到文本字符串和字节字符串的区别，以及这两类字符串在python2和python3中的区别。
with open('字符串与unicode','r',encoding='utf-8') as f:
    text_str = f.read()
    print(type(text_str))
    print(text_str)

"""
如果你希望以字节字符串的形式读取文件，使用如下的方式
"""

# <class 'bytes'>
# b'Python\xe4\xb8\xad\xe6\x9c\x89\xe4\xb8\xa4\xe7\xa7\x8d\xe4\xb8\x8d\xe5\x90\x8......
with open('字符串与unicode','rb') as f:
    text_str=f.read()
    print (type(text_str))
    print (text_str)

