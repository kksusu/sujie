#coding:utf-8
import unittest

def div_shang(a,b):
    return a//b
def div_yushu(a,b):
    return a%b
def div_float(a,b):
    return a/b
class DivFunction(unittest.TestCase):
    def setUp(self):
        print("test started")
    def tearDown(self):
        print("test ended")
    def test_div1(self):
        shang=div_shang(5,3)
        print('shang equals %r'%shang)
        try:
            self.assertEqual(div_shang(5,3),10//3)
        except Exception as msg:
            print(msg)
    def test_div2(self):
        yushu=div_yushu(10,6)
        print(yushu)
    def test_div3(self):
        float=div_float(7,2)
        print(float)
    def test_div4(self):
        pass
if __name__=='__main__':
    unittest.main()

