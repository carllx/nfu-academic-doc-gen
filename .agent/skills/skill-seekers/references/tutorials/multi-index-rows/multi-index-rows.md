# How To: Multi Index Rows

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate DataFrame: test multi index rows

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'A': pd.Series([0, 1, 2, np.nan, np.nan, 3, 4], index=pd.MultiIndex.from_tuples([('a', 1), ('a', 1), ('a', 1), ('a', 2), ('b', 1), ('b', 2), ('b', 2)]), dtype=object), 'B': 1})
```


## Complete Example

```python
# Workflow
expected = pd.DataFrame({'A': pd.Series([0, 1, 2, np.nan, np.nan, 3, 4], index=pd.MultiIndex.from_tuples([('a', 1), ('a', 1), ('a', 1), ('a', 2), ('b', 1), ('b', 2), ('b', 2)]), dtype=object), 'B': 1})
```

## Next Steps


---

*Source: test_explode.py:88 | Complexity: Beginner | Last updated: 2026-06-02*