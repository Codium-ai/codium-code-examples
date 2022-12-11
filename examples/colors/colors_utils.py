from __future__ import absolute_import, print_function
import re
import sys
from .csscolors import parse_rgb, css_colors

_PY2 = sys.version_info[0] == 2
string_types = basestring if _PY2 else str

from functools import partial


NAMES_OF_COLORS = ('black', 'red', 'green', 'yellow', 'blue',
          'magenta', 'cyan', 'white')



def join(*values):
    """
    Join values with semicolons.
    """
    return ';'.join(str(v) for v in values)

def is_string(object):
    return isinstance(object, string_types)

def encode_color(spec, base):
    """
    :param str|int|tuple|list spec: Unparsed color specification
    :param int base: Either 30 or 40, signifying the base value
        for color encoding (foreground and background respectively).
        Low values are added directly to the base. Higher values use `
        base + 8` (i.e. 38 or 48) then extended codes.
    :returns: Discovered ANSI color encoding.
    :rtype: str
    :raises: ValueError if cannot parse the color spec.
    """
    if is_string(spec):
        spec = spec.strip().lower()

    if spec == 'default':
        return join(base + 9)
    elif spec in NAMES_OF_COLORS:
        return join(base + NAMES_OF_COLORS.index(spec))
    elif isinstance(spec, int) and 0 <= spec <= 255:
        return join(base + 8, 5, spec)
    elif isinstance(spec, (tuple, list)):
        return join(base + 8, 2, join(*spec))
    else:
        rgb = parse_rgb(spec)
        # parse_rgb raises ValueError if cannot parse spec
        # or returns an rgb tuple if it can
        return join(base + 8, 2, join(*rgb))

def remove_ansi_color(s):
    return re.sub('\x1b\\[(K|.*?m)', '', s)


def len_without_color_codes(s):
    """
    Given a string with embedded ANSI codes, what would its
    length be without those codes?
    """
    return len(remove_ansi_color(s))
