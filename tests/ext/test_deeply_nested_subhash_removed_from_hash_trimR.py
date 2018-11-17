"""
Do not edit manually! Generated from
https://github.com/mr-mixas/Nested-Diff/tree/master/tests/json/deeply_nested_subhash_removed_from_hash_trimR.json
"""

from __future__ import unicode_literals
import nested_diff


def test_deeply_nested_subhash_removed_from_hash_trimR():
    a = {'one': {'two': {'three': 3}}, 'four': 4}
    b = {'four': 4}
    diff = {'D': {'one': {'R': None}, 'four': {'U': 4}}}
    opts = {'trimR': True}
    assert diff == nested_diff.diff(a, b, **opts)
