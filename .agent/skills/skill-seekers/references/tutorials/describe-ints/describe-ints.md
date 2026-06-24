# How To: Describe Ints

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate Series: test describe ints

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign expected = Series(...)

```python
expected = Series([5, 2, ser.std(), 0, 1, 2, 3, 4], name='int_data', index=['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'])
```


## Complete Example

```python
# Workflow
expected = Series([5, 2, ser.std(), 0, 1, 2, 3, 4], name='int_data', index=['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'])
```

## Next Steps


---

*Source: test_describe.py:26 | Complexity: Beginner | Last updated: 2026-06-02*