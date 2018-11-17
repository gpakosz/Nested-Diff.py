"""
Do not edit manually! Generated from
https://github.com/mr-mixas/Nested-Diff/tree/master/tests/json/one_item_removed_from_the_middle_of_list_noR.json
"""

from __future__ import unicode_literals
import nested_diff


def test_one_item_removed_from_the_middle_of_list_noR():
    a = [0, 1, 2]
    b = [0, 2]
    diff = {'D': [{'U': 0}, {'U': 2, 'I': 2}]}
    opts = {'R': False}
    assert diff == nested_diff.diff(a, b, **opts)
