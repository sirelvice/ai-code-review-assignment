# AI Code Review Assignment (Python)

## Candidate
- Name: Elvis Oduor
- Approximate time spent: 78 minutes

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- The function adds only non-cancelled orders but still divides by the total number of orders. This makes the average incorrect.
- If the input list is empty, the function will crash due to division by zero.

### Edge cases & risks
- The code assumes every order has "status" and "amount" keys, which can cause errors if they are missing.
- The amount value may not always be numeric, which can lead to incorrect results or runtime errors.
- If all orders are cancelled, the function still divides by the full list size, which does not make sense for an average of valid orders.

### Code quality / design issues
- The function assumes well-formed input without any validation.
- It does not clearly separate which orders are included in the average versus excluded.
- There is no defined behavior for cases where no valid orders exist.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Count only non-cancelled orders with valid numeric amounts.
- Divide the total amount by the number of included orders instead of all orders.
- Return 0.0 when there are no valid non-cancelled orders to avoid errors.
- Safely read dictionary values and skip invalid entries instead of crashing.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- An empty list, to confirm the function does not crash.
- A mix of cancelled and non-cancelled orders, to verify the average is calculated correctly.
- A case where all orders are cancelled.
- Orders with missing fields or invalid amount values, to ensure the function behaves safely.
- Different numeric formats for amounts (integers, floats, numeric strings).

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- The explanation says cancelled orders are excluded, but the denominator still includes them, so the average is wrong.
- It does not explain what happens when the input is empty or when order data is invalid.

### Rewritten explanation
- This function calculates the average order value for non-cancelled orders by summing their numeric amounts and dividing by the number of valid included orders. Cancelled orders are excluded from both the total and the count. Orders with missing or invalid amounts are ignored. If there are no valid non-cancelled orders, the function returns 0.0.

## 4) Final Judgment
- Decision: Request Changes
- Justification: The original code gives incorrect results because it divides by the wrong count and can crash on empty input. It also assumes perfect input data.
- Confidence & unknowns: I am confident in the identified issues and the proposed fix. One open question is how the product would prefer invalid amounts to be handled, but skipping them is a safe and reasonable default.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- The check "@" in email is too weak to determine whether an email is valid.
- Strings like "@", "user@", "@domain.com" and "a@b" are counted as valid even though they should not be.
- If an item in the list is not a string (e.g. None or a number), the code may fail or behave unexpectedly.

### Edge cases & risks
- Emails with multiple @ characters (e.g. "a@@b.com").
- Emails with leading or trailing spaces.
- Emails without a proper domain (missing .).
- Mixed input types (strings, numbers, None).
- Empty input list (works, but explanation overstates correctness).

### Code quality / design issues
- No clear definition of what “valid email” means.
- No input type checking.
- The explanation promises correct validation, but the implementation does not support that claim.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Added a small helper function to perform basic email validation.
- Ensured the value is a string before processing.
- Required exactly one @ character.
- Ensured both local and domain parts are present.
- Checked that the domain contains at least one dot and no spaces.
- Skipped invalid entries safely instead of counting them.

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- Empty list input, to confirm it returns 0.
- Clearly valid emails (e.g. "user@example.com").
- Clearly invalid emails ("@", "user@", "a@b", "a@@b.com").
- Inputs with leading/trailing spaces.
- Mixed input types such as None, numbers, and strings.
- Large input lists to ensure consistent behavior.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- The explanation claims the function counts “valid email addresses,” but the code only checks for the presence of "@".
- It incorrectly suggests invalid entries are safely handled, which is not always true for non-string inputs.

### Rewritten explanation
- This function counts how many items in the input list are valid email strings based on simple, practical rules. A valid email must be a string, contain exactly one @, have non-empty local and domain parts, contain no spaces, and include a dot in the domain. Invalid or non-string entries are ignored, and an empty input returns 0.

## 4) Final Judgment
- Decision: Request Changes
- Justification: The original implementation is too permissive and does not actually validate email addresses as described. It can also fail with non-string inputs.
- Confidence & unknowns: High confidence in the identified issues and the fix. Exact validation rules may vary by product, but the implemented approach is a reasonable and safe baseline.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- The function ignores None values in the sum but still divides by the total length of the input list, which produces an incorrect average.
- If the input list is empty, the function will raise a division by zero error.
- The function assumes all non-None values can be safely converted to floats, which is not always true.

### Edge cases & risks
- All values are None, which should not result in a division by the full list size.
- Mixed input types such as strings, invalid numeric values, or objects can cause runtime errors.
- Special float values like NaN or infinity can silently corrupt the final average.

### Code quality / design issues
- The logic does not clearly separate valid and invalid measurements.
- There is no explicit definition of what qualifies as a “valid” measurement.
- Error handling is missing around numeric conversion.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Count only values that are valid, finite numbers.
- Skip None values and values that cannot be converted to floats.
- Ignore non-finite float values such as NaN and infinity.
- Return 0.0 when no valid measurements exist to avoid division errors.

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- Empty input list, to ensure the function does not crash.
- Lists containing only None values.
- Mixed inputs (numbers, numeric strings, invalid strings).
- Inputs containing NaN or infinity values.
- Typical valid numeric inputs to confirm correct averaging.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- The explanation claims the function “safely handles mixed input types,” which is not true for invalid strings or non-numeric values.
- It does not mention the incorrect denominator or the division-by-zero risk.
- The behavior when no valid values exist is not defined.

### Rewritten explanation
- This function calculates the average of valid numeric measurements by ignoring missing values (None) and any values that cannot be converted into finite numbers. Only valid numeric inputs are included in both the total and the count. If no valid measurements are found, the function returns 0.0.

## 4) Final Judgment
- Decision: Request Changes
- Justification: The original implementation produces incorrect averages, can crash on empty input, and does not safely handle mixed or invalid values.
- Confidence & unknowns: High confidence in the identified issues and fixes. One open question is whether special float values like NaN or infinity should be handled differently depending on product requirements.
