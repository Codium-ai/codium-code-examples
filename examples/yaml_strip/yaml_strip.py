import re
from typing import Optional
import yaml

def yaml_safe_load(s):
    try:
        return yaml.safe_load(strip_yaml(s))
    except Exception:
        return None

def strip_yaml(yaml_str: Optional[str]) -> Optional[str]:
    if yaml_str is None:
        return None
    return re.sub(r'^```yaml', '', yaml_str).rstrip('`')
