"""
Do not edit manually! Generated from
https://github.com/mr-mixas/Nested-Diff/tree/master/tests/json/one_item_changed_in_the_middle_of_list_noU.json
"""

from __future__ import unicode_literals
import nested_diff


def test_one_item_changed_in_the_middle_of_list_noU():
    a = [0, 1, 2]
    b = [0, 9, 2]
    diff = {'D': [{'N': 9, 'O': 1, 'I': 1}]}
    opts = {'U': False}
    assert diff == nested_diff.diff(a, b, **opts)
