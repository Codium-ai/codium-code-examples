import pytest
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
