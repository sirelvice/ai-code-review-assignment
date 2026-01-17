# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py'.
from __future__ import annotations
from typing import Any, Iterable
import math

def average_valid_measurements(values: Iterable[Any]) -> float:
    """
    Average only valid numeric measurements.
     - Ignores None
     - Ignores values that can't be converted to float
     - Ignores non-finite values (NaN/inf)
     - Returns 0.0 if no valid values exist
    """
    total = 0.0
    valid_count = 0

    for v in values:
        if v is None:
            continue

        try:
            x = float(v)
        except (TypeError, ValueError): 
            continue

        if not math.isfinite(x):
            continue

        total += x
        valid_count += 1

    return total / valid_count if valid_count > 0 else 0.0