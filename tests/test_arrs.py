from utils import arrs
import pytest


@pytest.fixture
def fixt_arr():  # имя фикстуры любое
    return [1, 2, 3, 4]


def test_get(fixt_arr):
    assert arrs.get(fixt_arr, 1, "test") == 2  # поправил значение 3 на 2
    assert arrs.get([], 0, "test") == "test"


def test_my_slice(fixt_arr):  # поправил название тестовой функции
    assert arrs.my_slice(fixt_arr, 1, 3) == [2, 3]
    assert arrs.my_slice(fixt_arr, 1) == [2, 3, 4]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice(fixt_arr, None) == [1, 2, 3, 4]
