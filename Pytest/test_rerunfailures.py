def test_fail_return():
    assert 2+2==5
#pytest -v .\test_rerunfailures.py --reruns 3
#--reruns 设置测试用例失败后的重试次数