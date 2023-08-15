import unittest
import os
import sys

'''
Unittest python script
'''

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
GIT_TOP = os.path.join(THIS_DIR, "../..")
sys.path.append(GIT_TOP)

import pythonPack # noqa


class SampleTest(unittest.TestCase):

  def test_defaultPrint(cls):
    print("==This is default unittest==")
    print(f"\t checking file absPath :: {THIS_DIR}")
    print(f"\t checking file absPath :: {GIT_TOP}")

  def test_checkPath(cls):
    print("==Test checkPath scripts==")
    print(f"\t checking directory absPath :: {pythonPack.checkPath.validPathType( os.path.join(GIT_TOP, 'unitTest/unitTest_build/checkPath'))}")
    print(f"\t checking file absPath :: {pythonPack.checkPath.validFileType( os.path.join(GIT_TOP, 'unitTest/unitTest_build/checkPath/test.txt'))}")
    try:
      pythonPack.checkPath.validPathType(os.path.join(GIT_TOP, 'unitTest/unitTest_build/checkPath'))
      pythonPack.checkPath.validPathType(os.path.join(GIT_TOP, 'unitTest/unitTest_build/checkPath/text2.txt'))
      raise ValueError
    except Exception:
      pass


if __name__ == '__main__':
  unittest.main()
