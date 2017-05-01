"""
作者：文文
python中的正则表达式
python版本：python3.5

"""

#python中正则表达式是re模块
import re

#re模块最主要的是search函数，接受一个正则表达式规则和一个字符串，返回第一个匹配，如果没有找到匹配，返回None
# r代表原始字符串，原始字符串与正常字符串的区别是原始字符串不会将\解释成一个转义字符，但是遇到+、(、)等的时候仍表示转义字符
# search对象返回结果可以又match对象接受，
match = re.search(r'fox','The quick brown fox jumped...')
#调用group得到搜索结果，输出fox
print (match.group())
#在原始字符串中匹配开始的索引
print (match.start())
#在原始字符串中匹配结束的索引
print (match.end())


#search 得到的是第一个匹配，如果想要的到所有的匹配，那么可以使用findall或者finditer函数
#findall 返回搜索结果的列表
#finditer 返回一个生成器
#output : ['o', 'o']
print (re.findall(r'o','The quick brown fox jumped'))
# output:<callable_iterator object at 0x102d386a0>
print (re.finditer(r'o','The quick brown fox jumped'))

