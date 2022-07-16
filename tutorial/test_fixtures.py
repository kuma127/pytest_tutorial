import pytest


@pytest.fixture(scope='module')
def func_list():
    yield [1, 2, 3]
    print('Hello')


def test_func_list(func_list):
    assert len(func_list) == 3


@pytest.fixture()
def func_dic():
    return {"test": 1, "sample": 2}


def test_func_dic(func_dic):
    assert func_dic["test"] == 1


def test_func_double(func_list, func_dic):
    assert func_list[0] == func_dic["test"]
