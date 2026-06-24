# How To: Extension Array Cross Section

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test extension array cross section

## Prerequisites

**Required Modules:**
- `array`
- `datetime`
- `re`
- `weakref`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.indexing.common`
- `pandas.tests.indexing.test_floats`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': pd.array([1, 2], dtype='Int64'), 'B': pd.array([3, 4], dtype='Int64')}, index=['a', 'b'])
```

### Step 2: Assign expected = Series(...)

```python
expected = Series(pd.array([1, 3], dtype='Int64'), index=['A', 'B'], name='a')
```

### Step 3: Assign result = value

```python
result = df.loc['a']
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = value

```python
result = df.iloc[0]
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': pd.array([1, 2], dtype='Int64'), 'B': pd.array([3, 4], dtype='Int64')}, index=['a', 'b'])
expected = Series(pd.array([1, 3], dtype='Int64'), index=['A', 'B'], name='a')
result = df.loc['a']
tm.assert_series_equal(result, expected)
result = df.iloc[0]
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:978 | Complexity: Intermediate | Last updated: 2026-06-02*