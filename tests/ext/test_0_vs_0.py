"""
Do not edit manually! Generated from
https://github.com/mr-mixas/Nested-Diff/tree/master/tests/json/0_vs_0.json
"""

from __future__ import unicode_literals
import nested_diff


def test_0_vs_0():
    a = 0
    b = 0
    diff = {'U': 0}
    opts = {}
    assert diff == nested_diff.diff(a, b, **opts)
