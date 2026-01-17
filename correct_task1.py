# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.
from __future__ import annotations
from typing import Any, Iterable
def calculate_average_order_value(orders: Iterable[dict[str, Any]]) -> float:
    """
    Calculate average order value for non-cancelled orders.
    - Includes orders where status != "cancelled"
    - Ignores orders with missing/invalid amount
    - Returns 0.0 if there are no valid non-cancelled orders
    """
    total = 0.0
    valid_count = 0

    for order in orders:
        if not isinstance(order, dict):
            continue

        if order.get("status") == "cancelled":
            continue

        amount = order.get("amount")
        try:
            amount_f = float(amount)
        except (TypeError, ValueError):
            continue

        total += amount_f
        valid_count += 1

    return total / valid_count if valid_count > 0 else 0.0    