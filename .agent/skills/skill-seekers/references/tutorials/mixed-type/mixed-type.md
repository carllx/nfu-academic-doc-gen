# How To: Mixed Type

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate Series: test mixed type

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign expected = pd.Series(...)

```python
expected = pd.Series([0, 1, 2, np.nan, None, np.nan, 'a', 'b'], index=[0, 0, 0, 1, 2, 3, 4, 4], dtype=object, name='foo')
```


## Complete Example

```python
# Workflow
expected = pd.Series([0, 1, 2, np.nan, None, np.nan, 'a', 'b'], index=[0, 0, 0, 1, 2, 3, 4, 4], dtype=object, name='foo')
```

## Next Steps


---

*Source: test_explode.py:22 | Complexity: Beginner | Last updated: 2026-06-02*