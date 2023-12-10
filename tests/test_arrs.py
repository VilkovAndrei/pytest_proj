from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2  # поправил значение 3 на 2
    assert arrs.get([], 0, "test") == "test"


def test_my_slice():  # поправил название тестовой функции
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice([1, 2, 3], None) == [1, 2, 3]
