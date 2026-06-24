# How To: Pyarrow Dtype Backend

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate DataFrame: test pyarrow dtype backend

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'a': pd.Series([1, 2, 3], dtype=np.dtype('int32')), 'b': pd.Series(['x', 'y', None], dtype=np.dtype('O')), 'c': pd.Series([True, False, None], dtype=np.dtype('O')), 'd': pd.Series([np.nan, 100.5, 200], dtype=np.dtype('float')), 'e': pd.Series(pd.date_range('2022', periods=3)), 'f': pd.Series(pd.date_range('2022', periods=3, tz='UTC').as_unit('s')), 'g': pd.Series(pd.timedelta_range('1D', periods=3))})
```


## Complete Example

```python
# Workflow
df = pd.DataFrame({'a': pd.Series([1, 2, 3], dtype=np.dtype('int32')), 'b': pd.Series(['x', 'y', None], dtype=np.dtype('O')), 'c': pd.Series([True, False, None], dtype=np.dtype('O')), 'd': pd.Series([np.nan, 100.5, 200], dtype=np.dtype('float')), 'e': pd.Series(pd.date_range('2022', periods=3)), 'f': pd.Series(pd.date_range('2022', periods=3, tz='UTC').as_unit('s')), 'g': pd.Series(pd.timedelta_range('1D', periods=3))})
```

## Next Steps


---

*Source: test_convert_dtypes.py:49 | Complexity: Beginner | Last updated: 2026-06-02*