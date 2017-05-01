"""
作者：文文
正则表达式中的标记
python版本：python3.5

"""

import re

"""
re.IGNORECASE | re.I ：忽略大小写
re.DOTALL | re.S : .字符在正常情况下不会匹配换行符，但是使用re.S可以使其匹配换行符
re.MULTILINE | re.M : 多行模式,导致仅能够匹配字符串开始与结束的^和$字符可以匹配字符串内任意行的开始与结束
re.VERBOSE | re.X : 允许复杂的正则表达式以更容易阅读的方式表示。导致所有的空白（除了在字符组中的）被忽略，包括换行符，同时将#当作注释字符
re.DEBUG : 编译正则表达式时将一些调试信息输出到sys.stderr

在python2与python3中，一些字符快捷方式的工作机制存在区别，如\w在python3中匹配几乎所有语言的单词，但是在python2中仅匹配英文字符
所以，为了使re模块强制遵循python2或者python3的标准，可以使用如下两个标记
re.Unicode | re.U ：re模块强制遵循python3的标准
re.ASCII | re.A ：re模块强制遵循python2的标准

使用多个标记：使用|操作符即可

"""
#output : <_sre.SRE_Match object; span=(0, 6), match='Python'>
print (re.search(r'python','Python is awesome',re.I))

#output : <_sre.SRE_Match object; span=(0, 3), match='foo'>
print (re.search(r'.+','foo\nbar'))

#output : <_sre.SRE_Match object; span=(0, 7), match='foo\nbar'>
print (re.search(r'.+','foo\nbar',re.S))

#output : None
print (re.search(r'^bar','foo\nbar'))

#output : <_sre.SRE_Match object; span=(4, 7), match='bar'>
print (re.search(r'^bar','foo\nbar',re.M))

#output : <_sre.SRE_Match object; span=(0, 8), match='873-2323'>
print (re.search(r"""(?P<first_three>[\d]{3}) # the first three digits
                    -                        # a literal hyphen
                    (?P<last_four>[\d]{4})# the last four code
        """,'873-2323',re.X))

