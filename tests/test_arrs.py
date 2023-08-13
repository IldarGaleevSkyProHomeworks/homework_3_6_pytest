import pytest

from utils import arrs


@pytest.fixture()
def test_data():
    return [1, 2, 3]


def test_get(test_data):
    assert arrs.get(test_data, 2, "test") == 3
    assert arrs.get([], -1, "test") == "test"


def test_slice(test_data):
    assert arrs.my_slice(test_data, 1, 3) == [2, 3]
    assert arrs.my_slice(test_data, 1) == [2, 3]
    assert arrs.my_slice([1], -1) == [1]
    assert arrs.my_slice([1], -2) == [1]
    assert arrs.my_slice([]) == []
