# How To: Get Numeric Data Extension Dtype

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate DataFrame: test get numeric data extension dtype

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
df = DataFrame({'A': pd.array([-10, np.nan, 0, 10, 20, 30], dtype='Int64'), 'B': Categorical(list('abcabc')), 'C': pd.array([0, 1, 2, 3, np.nan, 5], dtype='UInt8'), 'D': IntervalArray.from_breaks(range(7))})
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': pd.array([-10, np.nan, 0, 10, 20, 30], dtype='Int64'), 'B': Categorical(list('abcabc')), 'C': pd.array([0, 1, 2, 3, np.nan, 5], dtype='UInt8'), 'D': IntervalArray.from_breaks(range(7))})
```

## Next Steps


---

*Source: test_get_numeric_data.py:94 | Complexity: Beginner | Last updated: 2026-06-02*