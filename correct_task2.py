# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.
from __future__ import annotations
from typing import Any, Iterable
def is_basic_valid_email(email: Any) -> bool:
    """
    Basic email validation suitable for general application logic.
    This is not RFC-complete, but avoids obvious invalid cases.
    """
    if not isinstance(email, str):
        return False
    
    email = email.strip()
    if not email or " " in email:
        return False
    
    if email.count("@") != 1:
        return False
    
    local, domain = email.split("@")
    if not local or not domain:
        return False
    
    if domain.startswith(".") or domain.endswith("."):
        return False
    
    if "." not in domain:
        return False
    
    return True

def count_valid_emails(emails: Iterable[Any]) -> int:
    count = 0
    for email in emails:
        if is_basic_valid_email(email):
            count += 1
    return count