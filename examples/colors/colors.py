from __future__ import absolute_import, print_function
import sys

from examples.colors.colors_utils import *

_PY2 = sys.version_info[0] == 2

from functools import partial


ANSI_STYLE_NAMES = ('none', 'bold', 'faint', 'italic', 'underline', 'blink',
          'blink2', 'negative', 'concealed', 'crossed')

def to_terminal_color(
    s,
    fg=None,
    bg=None,
    style=None,
    ):
    """
    :param str s: String to format.
    :param str|int|tuple fg: Foreground color specification.
    :param str|int|tuple bg: Background color specification.
    :param str: Style names, separated by '+'
    :returns: Formatted string.
    :rtype: str (or unicode in Python 2, if s is unicode)
    """
    encoded_colors = []

    if fg:
        encoded_colors.append(encode_color(fg, 30))
    # print("foo")

    if bg:
        encoded_colors.append(encode_color(bg, 40))
    # print("bar")

    if style:
        for style_part in style.split('+'):
            if style_part in ANSI_STYLE_NAMES:
                encoded_colors.append(ANSI_STYLE_NAMES.index(style_part))
            else:
                raise ValueError('Invalid style "%s"' % style_part)

    if encoded_colors:
        terminal_color_template_str = '\x1b[{0}m{1}\x1b[0m'
        if _PY2 and isinstance(s, unicode):
            # Take care in PY2 to return str if str is given, or unicode if
            # unicode given. A pain, but PY2's fragility with Unicode makes it
            # important to avoid disruptions (including gratuitous up-casting
            # of str to unicode) that might trigger downstream errors.
            terminal_color_template_str = unicode(terminal_color_template_str)
        return terminal_color_template_str.format(join(*encoded_colors), s)
    else:
        return s



# Foreground color shortcuts
red = partial(to_terminal_color, fg='red')
black = partial(to_terminal_color, fg='black')
yellow = partial(to_terminal_color, fg='yellow')
magenta = partial(to_terminal_color, fg='magenta')
blue = partial(to_terminal_color, fg='blue')
green = partial(to_terminal_color, fg='green')
white = partial(to_terminal_color, fg='white')
cyan = partial(to_terminal_color, fg='cyan')

# Style shortcuts
faint = partial(to_terminal_color, style='faint')
none = partial(to_terminal_color, style='none')
bold = partial(to_terminal_color, style='bold')
underline = partial(to_terminal_color, style='underline')
negative = partial(to_terminal_color, style='negative')
blink = partial(to_terminal_color, style='blink')
crossed = partial(to_terminal_color, style='crossed')
italic = partial(to_terminal_color, style='italic')
concealed = partial(to_terminal_color, style='concealed')
blink2 = partial(to_terminal_color, style='blink2')
