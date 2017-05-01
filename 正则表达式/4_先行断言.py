"""
作者：文文
正则表达式中的先行断言知识
python版本：python3.5

"""
import re

"""

正则表达式中有一种机制能够基于之后的内容是否存在接受或者拒绝一个匹配，而不需要接下来的内容作为匹配的一部分，它被称为先行断言
取反先行断言：使用(?!字符、字符组或其他基本单元)
正向先行断言: 使用(?=字符、字符组或其他基本单元)

"""
#取反先行断言
#表示n后面不能紧跟e
#仅仅返回字符n
#output : <_sre.SRE_Match object; span=(2, 3), match='n'>
print (re.search(r'n(?!e)','final'))

#output : None
print (re.search(r'n(?!e)','jasmine'))

#output : <_sre.SRE_Match object; span=(5, 6), match='n'>
print (re.search(r'n(?!e)','Python'))

#正向先行断言，表示n后面紧跟e，但返回的匹配结果不包含后面的e
#output : <_sre.SRE_Match object; span=(5, 6), match='n'>
print (re.search(r'n(?=e)','jasmine'))

#output : None
print (re.search(r'n(?=e)','python'))

