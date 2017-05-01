
"""
作者：文文
单元测试
python版本：python3.5

"""

"""
将代码与其他内容(甚至是其程序自身的其他代码部分）隔离的测试成为单元测试
"""


def calculate_age_at_wedding(person):
    """Calculate the age of a person at his or her wedding ,given the
        record of the person as a dictionary-like object
    """

    anniversary = person['anniversary']
    birthday = person['birthday']

    age = anniversary.year - birthday.year

    if birthday.replace(year=anniversary.year) > anniversary:
        age -= 1

    return age


import unittest
from datetime import date

""" 使用 python -m unittest unittest_framewrok.py 执行
    成功执行的测试，返回.
    测试执行失败，打印F
    测试发生错误，打印E
    遇到希望跳过的测试打印字母S
"""

"""测试结果

.EFs
======================================================================
ERROR: test_error_case (unittest_framework.Tests)
Attempt to send an empty dict to the funciton.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/shixiaowen/python3/python高级编程/单元测试/unittest_framework.py", line 77, in test_error_case
    age = calculate_age_at_wedding(person)
  File "/Users/shixiaowen/python3/python高级编程/单元测试/unittest_framework.py", line 19, in calculate_age_at_wedding
    anniversary = person['anniversary']
KeyError: 'anniversary'

======================================================================
FAIL: test_failure_case (unittest_framework.Tests)
Assert a wrong age ,and fail
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/shixiaowen/python3/python高级编程/单元测试/unittest_framework.py", line 71, in test_failure_case
    self.assertEqual(age, 99)
AssertionError: 25 != 99

----------------------------------------------------------------------
Ran 4 tests in 0.001s

FAILED (failures=1, errors=1, skipped=1)
"""

class Tests(unittest.TestCase):

    #正确的测试用例，返回.
    def test_calculate_age_at_wedding(self):
        """
        Establish that hte "calculate_age_at_wedding" function seems to calculate a person's age
        at his wedding correctly ,given a dictionary-like object representing a person.
        """

        person={'anniversary':date(2012,4,21),
                'birthday':date(1986,6,15)}

        age = calculate_age_at_wedding(person)

        self.assertEqual(age,25)

        person={'anniversary':date(1969,8,11),
                'birthday':date(1945,2,15)}
        age = calculate_age_at_wedding(person)

        self.assertEqual(age,24)


    # 失败的测试用例，assert不通过，返回F
    def test_failure_case(self):
        """Assert a wrong age ,and fail"""
        person = {'anniversary': date(2012, 4, 21),
                  'birthday': date(1986, 6, 15)}

        age = calculate_age_at_wedding(person)

        self.assertEqual(age, 99)

    #错误的测试用例，assert之前有代码报错，返回E
    def test_error_case(self):
        """Attempt to send an empty dict to the funciton."""
        person = {}
        age = calculate_age_at_wedding(person)
        self.assertEqual(age,25)

    #希望跳过的测试用例，返回S
    @unittest.skipIf(True,'This test was skiped')
    def test_skipped_case(self):
        """Skip this test"""
        pass

