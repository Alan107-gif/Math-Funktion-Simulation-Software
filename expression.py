import re
import keyword
import builtins
import math


def detect_variables(expr: str):
    """Detect variable names in the expression that are not keywords or math/builtins."""
    tokens = re.findall(r"[A-Za-z_][A-Za-z0-9_]*", expr)
    exclude = set(keyword.kwlist) | set(dir(math)) | set(dir(builtins))
    return sorted({t for t in tokens if t not in exclude})
