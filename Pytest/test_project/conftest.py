import pytest
#设置测试钩子
@pytest.fixture()
def test_url():
    return "http://www.baidu.com"
#只作用于它所在的目录及子目录