# How To: Select Dtypes Duplicate Columns

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test select dtypes duplicate columns

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': ['a', 'b', 'c'], 'b': [1, 2, 3], 'c': np.arange(3, 6).astype('u1'), 'd': np.arange(4.0, 7.0, dtype='float64'), 'e': [True, False, True], 'f': pd.date_range('now', periods=3).values})
```

### Step 2: Assign df.columns = value

```python
df.columns = ['a', 'a', 'b', 'b', 'b', 'c']
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': list(range(1, 4)), 'b': np.arange(3, 6).astype('u1')})
```

### Step 4: Assign result = df.select_dtypes(...)

```python
result = df.select_dtypes(include=[np.number], exclude=['floating'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': ['a', 'b', 'c'], 'b': [1, 2, 3], 'c': np.arange(3, 6).astype('u1'), 'd': np.arange(4.0, 7.0, dtype='float64'), 'e': [True, False, True], 'f': pd.date_range('now', periods=3).values})
df.columns = ['a', 'a', 'b', 'b', 'b', 'c']
expected = DataFrame({'a': list(range(1, 4)), 'b': np.arange(3, 6).astype('u1')})
result = df.select_dtypes(include=[np.number], exclude=['floating'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_select_dtypes.py:281 | Complexity: Intermediate | Last updated: 2026-06-02*