# How To: Get Numeric Data Mixed Dtype

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate DataFrame: test get numeric data mixed dtype

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3], 'b': [True, False, True], 'c': ['foo', 'bar', 'baz'], 'd': [None, None, None], 'e': [3.14, 0.577, 2.773]})
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': [1, 2, 3], 'b': [True, False, True], 'c': ['foo', 'bar', 'baz'], 'd': [None, None, None], 'e': [3.14, 0.577, 2.773]})
```

## Next Steps


---

*Source: test_get_numeric_data.py:80 | Complexity: Beginner | Last updated: 2026-06-02*