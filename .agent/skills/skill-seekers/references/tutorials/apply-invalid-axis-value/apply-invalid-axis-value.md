# How To: Apply Invalid Axis Value

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate DataFrame: test apply invalid axis value

## Prerequisites

**Required Modules:**
- `itertools`
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['a', 'a', 'c'])
```


## Complete Example

```python
# Workflow
df = DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['a', 'a', 'c'])
```

## Next Steps


---

*Source: test_invalid_arg.py:42 | Complexity: Beginner | Last updated: 2026-06-02*