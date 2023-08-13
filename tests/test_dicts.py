import pytest

from utils import dicts


@pytest.fixture()
def test_data():
    return {'key1': "val1", 'key2': "val2"}


@pytest.mark.parametrize("args, expected_result", [
    (('key1', "default"), "val1"),
    (('key3', "default"), "default"),
    (('key3',), "git")
])
def test_get_val(test_data, args, expected_result):
    assert dicts.get_val(test_data, *args) == expected_result
