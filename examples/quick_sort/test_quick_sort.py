import pytest
from hypothesis import given
import hypothesis.strategies as some

from examples.quick_sort.quick_sort import qsort

class TestQuickSort:
    @pytest.mark.parametrize(
            "l,expected",
            [
                ([], []),
                ([1], [1]),
            ]
            )
    def test_sort_simple_lists(self, l, expected):
        expected_copy = expected[:]
        assert qsort(l) == expected_copy

class TestQuickSortPBT:
    @given(some.lists(some.integers()))
    def test_sort_is_idempotent(self, lst):
        assert qsort(qsort(lst)) == qsort(lst)
