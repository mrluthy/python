import pytest

from andrew_practice import did_I_return_home


def test_did_I_return_home_mixed_case():
    assert did_I_return_home(['n', 'w', 'w', 'S', 's', 's', 'e', 'E', 'n', 'n'])


def test_did_I_return_home_numbers():
    assert not did_I_return_home(['n', 'w', 'w', '1', 's', '-1', 'e', '9', 'n', 'n'])


def test_did_I_return_home_special_char():
    assert not did_I_return_home(['n', '#', 'w', 's', ')', 's', 'e', '\\', 'n', 'n'])


def test_did_I_return_home_too_short():
    assert not did_I_return_home(['n', 'w', 'w', 's', 's', 'e', 'e', 'n',"n"])