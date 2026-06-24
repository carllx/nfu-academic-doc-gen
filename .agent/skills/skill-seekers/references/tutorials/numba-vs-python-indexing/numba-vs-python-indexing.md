# How To: Numba Vs Python Indexing

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate DataFrame: test numba vs python indexing

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.util.version`


## Step-by-Step Guide

### Step 1: Assign frame = DataFrame(...)

```python
frame = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7.0, 8.0, 9.0]}, index=Index(['A', 'B', 'C']))
```


## Complete Example

```python
# Workflow
frame = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7.0, 8.0, 9.0]}, index=Index(['A', 'B', 'C']))
```

## Next Steps


---

*Source: test_numba.py:54 | Complexity: Beginner | Last updated: 2026-06-02*