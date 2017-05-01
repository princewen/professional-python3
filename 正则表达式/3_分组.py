"""
作者：文文
主要介绍正则表达式中的分组概念
python版本：python3.5

"""
import re
"""
python正则表达式提供了一个机制将表达式分组，当使用分组时，除了获得整个匹配，还可以在匹配中选择每一个单独组
可以在正则表达式中使用圆括号指定分组

"""
match = re.search(r'([\d]{3})-([\d]{4})','867-5309 / Jenny')

#返回整个匹配,即867-5309
print (match.group())

#返回一个对应每一个单个分组的元组
#output : ('867', '5309')
print (match.groups())

#获取单个分组，0代表完整的匹配，正式的分组编号从1开始
#output : 867-5309
print (match.group(0))

#output : 867
print (match.group(1))

#output : 5309
print (match.group(2))

"""

命名分组
除了按位置编号的分组外，python正则表达式还提供一个命名分组的机制
一个命名分组的语法是在开始的"("字符后面立即添加 ?P<group_name>
当使用命名分组时，match对象提供了一个groupdict函数，返回一个分组字典，键对应分组的名称
当命名分组和非命名分组同时出现时，非命名分组不会出现在返回的字典中

"""
match = re.search(r'(?P<first_three>[\d]{3})-(?P<last_four>[\d]{4})','867-5309 / Jenny')

#output : 867
print (match.group('first_three'))

#output : {'last_four': '5309', 'first_three': '867'}
print (match.groupdict())

match = re.search(r'(?P<first_three>[\d]{3})-([\d]{4})','867-5309 / Jenny')

#非命名分组不会出现在结果中
#output : {'first_three': '867'}
print (match.groupdict())

"""

引用已经存在的分组
有时候，你或许会寻找同样一个子匹配，该匹配会接下来再次出现
例如，尝试解析一段xml代码，xml代码的开始标记和结束标记必须是相同的，使用<([\w_]+)>和<(/[\w_]+)>并不可行，因为没有限制开始标记必须相同，<boo>和</foo>也可以匹配
正则表达式提供了解决这种问题的一种方式--使用回溯引用
可以使用\M回溯引用编号分组，此时\1表示匹配第一个分组，\2表示匹配第二个分组（最多99个）

"""

#匹配xml
match = re.search(r'<([\w_]+)>stuff</\1>','<foo>stuff</foo>')

#output : <foo>stuff</foo>
print (match.group())

#output : ('foo',) ，此时只有一个分组，因为回溯引用取代了第二个分组
print (match.groups())

#output : None , 因为前后两个标签不一致
print (re.search(r'<([\w_]+)>stuff</\1>','<foo>stuff</boo>'))


