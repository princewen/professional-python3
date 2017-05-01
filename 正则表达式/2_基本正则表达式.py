"""
作者：文文
主要介绍一些基本的匹配规则
python版本：python3.5

"""

import re

"""1 字符组
使用方括号并在方括号内列出所有可能的字符从而表示一个字符组,一定要注意，它仅仅匹配一个字符
[Pp]：匹配大写P或者小写p
[A-Z]:匹配大写A到大写Z中任何一个
[^0-9]:在方括号中的^是取反字符（^还可以表示字符串的开始)，表示匹配除0-9之外的字符

一些快捷方式
\w: 与任意单词字符匹配，python3中基本上与几乎任何语言的任意单词匹配，python2中至于英语单词字符匹配，但无论哪个版本，都会匹配数字、下划线或者连字符
\W: 匹配\w包含字符之外的所有字符
\d: 匹配数字字符，python3中，还与其他语言的数字字符匹配，在python2中，它只匹配[0-9]
\D: 匹配\d包含字符之外的所有字符
\s: 匹配空白字符，比如空格、tab、换行等
\S: 匹配\s包含字符之外的所有字符
\b: 匹配一个长度为0的字串,它仅仅在一个单词开始或结尾处匹配，也被称为词边界字符快捷方式
\B: 匹配不在单词开始或结束位置长度为0的子字符串,简单来说，使用\B表明这里不是一个单词的结束

字符串的开始与结束
^字符指定字符串的开始
$字符指定字符串的结束

任意字符
.字符表示任何单个字符，但是它仅仅只能出现在方括号字符组以外，如果出现在方括号里面，仅表示.字符这一个字符
"""

#output:<_sre.SRE_Match object; span=(0, 6), match='Python'>
print (re.search(r'[pP]ython','Python 3'))

#output:<_sre.SRE_Match object; span=(0, 6), match='python'>
print (re.search(r'[pP]ython','python 3'))

#output:<_sre.SRE_Match object; span=(0, 4), match='gray'>
print( re.search(r'gr[ae]y','gray'))

#output :None, 因为方括号仅仅匹配一个字符
print (re.search(r'gr[ae]y','graey'))

#output:<_sre.SRE_Match object; span=(0, 1), match='x'>
print (re.search(r'[a-zA-Z]','x'))

#output:<_sre.SRE_Match object; span=(0, 1), match='A'>
print (re.search(r'[^a-z]','A'))

#output:None
print (re.search(r'[^a-z]','b'))

#output : <_sre.SRE_Match object; span=(0, 4), match='cron'>
print (re.search(r'\bcron\b','cron'))

#output : None
print (re.search(r'\bcron\b','croner'))

#output : None
print (re.search(r'cron\B','cron'))

#output : <_sre.SRE_Match object; span=(0, 4), match='cron'>
print (re.search(r'cron\B','croner'))

#output : <_sre.SRE_Match object; span=(0, 1), match='P'>
print (re.search(r'\w','Python 3'))

#output : ['P', 'y', 't', 'h', 'o', 'n', '3']
print (re.findall(r'\w','Python 3'))

#output : None
print (re.search(r'^python','This code is in python'))

#output : <_sre.SRE_Match object; span=(0, 6), match='python'>
print (re.search(r'^python','python 3'))

#output : <_sre.SRE_Match object; span=(16, 22), match='python'>
print (re.search(r'python$','This code is in python'))

#output : None
print (re.search(r'python$','python 3'))

#output : <_sre.SRE_Match object; span=(0, 6), match='python'>
print (re.search(r'p.th.n','python 3'))

"""2 可选字符
目前为止，所有我们看到的正则表达式都是在正则表达式中的字符与被搜索的字符串中的字符保持1:1的关系,
然而有时，一个字符或许是可选的，比如有多种拼写方式的单词，如color 和 colour  都表示颜色
此时可以使用？指定一个字符、字符组或其他基本单元可选，即期望该字符、字符组或其他基本单元出现0次或者1次（这是?的第一个作用，出现在一个字符、字符组或其他基本单元后面时起作用）
"""

#output : <_sre.SRE_Match object; span=(15, 20), match='honor'>
print (re.search(r'honou?r','He served with honor and distinction.'))

#output : <_sre.SRE_Match object; span=(15, 21), match='honour'>
print (re.search(r'honou?r','He served with honour and distinction.'))

"""3 重复
有时你需要同样的字符或者字符组重复出现，或者出现0次或者1次
{N} : 表示一个字符、字符组或其他基本单元重复出现N次
{M,N} : 表示一个字符、字符组或其他基本单元重复出现M-N次,最少出现M次，最多出现N次,但尽可能匹配多的字符
{M,N}? : 表示一个字符、字符组或其他基本单元重复出现M-N次，但尽可能少的匹配字符（这是？的第二个作用，出现在重复之后，使其变为惰性匹配）
{M,}:  表示一个字符、字符组或其他基本单元重复出现至少M次，但没有上限
* : 代替{0,},表示一个字符、字符组或其他基本单元重复出现0次或多次
+ : 代替{1,},表示一个字符、字符组或其他基本单元重复出现1次或多次
"""

#output : <_sre.SRE_Match object; span=(0, 8), match='867-5309'>
print (re.search(r'[\d]{3}-[\d]{4}','867-5309 / Jenny'))

#output : <_sre.SRE_Match object; span=(0, 4), match='0323'>
print (re.search(r'[\d]{3,4}','0323'))

#惰性匹配, output : <_sre.SRE_Match object; span=(0, 3), match='032'>
print (re.search(r'[\d]{3,4}?','0323'))

#<_sre.SRE_Match object; span=(0, 4), match='1600'>
print (re.search(r'[\d]+','1600 Pennsylvania Ave.'))





