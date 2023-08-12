from utils import dicts


def test_get_val():

    test_data = {'key1': "val1", 'key2': "val2"}

    assert dicts.get_val(test_data, 'key1', "default") == "val1"
    assert dicts.get_val(test_data, 'key3', "default") == "default"
    assert dicts.get_val(test_data, 'key3') == "git"
