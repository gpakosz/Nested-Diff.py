"""
Do not edit manually! Generated from
https://github.com/mr-mixas/Nested-Diff/tree/master/tests/json/lists_LCS_changed_items_noOU.json
"""

from __future__ import unicode_literals
import nested_diff


def test_lists_LCS_changed_items_noOU():
    a = [0, 1, 2, 3, 4, 5, 6, 7]
    b = [0, 1, 9, 9, 4, 9, 6, 7]
    diff = {'D': [{'N': 9, 'I': 2}, {'N': 9}, {'N': 9, 'I': 5}]}
    opts = {'U': False, 'O': False}
    assert diff == nested_diff.diff(a, b, **opts)
