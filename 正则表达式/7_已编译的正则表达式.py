"""
作者：文文
预先将正则表达式编译
python版本：python3.5

"""
import re

""" 使用re.comiple对正则表达式进行预先编译"""
pattern = re.compile(r'(\+?1)?[ .-]?\(?([\d]{3})\)?[ .-]?([\d]{3})[ .-]?([\d]{4})')

"""
可以使用如下两种方式进行调用，输出结果一样
<_sre.SRE_Match object; span=(0, 12), match='213-867-5309'>
"""
print (pattern.search('213-867-5309'))
print (re.search(pattern,'213-867-5309'))