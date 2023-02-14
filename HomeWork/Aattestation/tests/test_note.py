import pytest

from src.note import Note


@pytest.mark.parametrize('data_list, expected_result', [
    (['23', '11', '2023'], True), ('12', False), ('', False),
    ('add', False)])
def test_check_separator(data_list, expected_result):
    assert Note.check_separator(data_list) == expected_result


@pytest.mark.parametrize('day, expected_result', [
    ('0', False), ("3", '3'), ("32", False), ("30", '30'),
    ("aaa", False), ('03', '3')])
def test_check_day(day, expected_result):
    assert Note.check_day(day) == expected_result


@pytest.mark.parametrize('month, expected_result', [
    ('01', '1'), ('2', '2'), ('12', '12'), ('10', '10'),
    ('0', False), ('13', False), ('aaaa', False), ('', False)])
def test_check_month(month, expected_result):
    assert Note.check_month(month) == expected_result


@pytest.mark.parametrize('year, expected_result', [
    ('20', False), ('23', '2023'), ('', False), ('1asda', False), ('2022', False),
    ('2023', '2023')])
def test_check_year(year, expected_result):
    assert Note.check_year(year) == expected_result


@pytest.mark.parametrize('value_pk, expected_result', [
    ('1', '1'), ('0', False), ('', False), ('aaa', False)
])
def test_check_pk(value_pk, expected_result):
    assert Note.check_pk(value_pk) == expected_result