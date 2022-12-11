from .colors import to_terminal_color

def test_to_terminal_color():
    """
    This is a sanity test to make sure that imports and paths work.
    """
    assert to_terminal_color("foo", fg="red") == "\x1b[31mfoo\x1b[0m"
