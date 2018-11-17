"""
Do not edit manually! Generated from
https://github.com/mr-mixas/Nested-Diff/tree/master/tests/json/hashes_with_one_different_value_noO.json
"""

from __future__ import unicode_literals
import nested_diff


def test_hashes_with_one_different_value_noO():
    a = {'one': 1}
    b = {'one': 2}
    diff = {'D': {'one': {'N': 2}}}
    opts = {'O': False}
    assert diff == nested_diff.diff(a, b, **opts)
