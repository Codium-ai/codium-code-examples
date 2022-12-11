from .colors import to_terminal_color

def test_to_terminal_color_env_setup_correct():
    """
    This is a sanity test to make sure that imports and paths work.
    Just run the function.
    """
    to_terminal_color("foo", fg="red")
