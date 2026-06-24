# How To: Correct Function Signature

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate DataFrame: test correct function signature

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.util.version`
- `numba`
- `numba`


## Step-by-Step Guide

### Step 1: Assign data = DataFrame(...)

```python
data = DataFrame({'key': ['a', 'a', 'b', 'b', 'a'], 'data': [1.0, 2.0, 3.0, 4.0, 5.0]}, columns=['key', 'data'])
```


## Complete Example

```python
# Workflow
data = DataFrame({'key': ['a', 'a', 'b', 'b', 'a'], 'data': [1.0, 2.0, 3.0, 4.0, 5.0]}, columns=['key', 'data'])
```

## Next Steps


---

*Source: test_numba.py:32 | Complexity: Beginner | Last updated: 2026-06-02*