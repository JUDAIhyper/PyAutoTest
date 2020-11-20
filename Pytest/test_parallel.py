from time import sleep
import pytest

@pytest.mark.flaky(reruns=5,reruns_delay=1) #设置失败执行5次，0延迟
def test_01():
    sleep(3)
    assert 2+2==4
def test_02():
    sleep(2)
    print("hahaha")
def test_03():
    sleep(2)
    print("acfun")
    
if __name__=="__main__":
    pytest.main(['-sv','test_parallel.py','--tests-per-worker','auto'])

#不使用线程： pytest -q .\test_parallel.py
#指定线程数： pytest -q .\test_parallel.py --tests-per-worker auto
