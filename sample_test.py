import pytest
from sample import sample_script


def test_sample_script_yes_should_return_false():
    assert not sample_script('yes')


def test_sample_script_not_yes_should_return_true():
    assert sample_script('not yes')