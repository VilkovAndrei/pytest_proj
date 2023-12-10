from utils import dicts


def test_get_val():
    assert dicts.get_val({"Name": "Anna", "Age": 12, "School": "3"}, "Age", 'git') == 12
    assert dicts.get_val({"Name": "Anna", "Age": 12, "School": "3"}, "Name",  'git') == "Anna"
    assert dicts.get_val({"Name": "Anna", "Age": 12, "School": "3"}, "123",  'git') == 'git'
    assert dicts.get_val({}, "123", 'git') == 'git'
