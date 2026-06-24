# How To: Extension Array Cross Section Converts

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test extension array cross section converts

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
df = DataFrame({'A': pd.array([1, 2], dtype='Int64'), 'B': np.array([1, 2], dtype='int64')}, index=['a', 'b'])
```

### Step 2: Assign result = value

```python
result = df.loc['a']
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([1, 1], dtype='Int64', index=['A', 'B'], name='a')
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

### Step 7: Assign df = DataFrame(...)

```python
df = DataFrame({'A': pd.array([1, 2], dtype='Int64'), 'B': np.array(['a', 'b'])}, index=['a', 'b'])
```

### Step 8: Assign result = value

```python
result = df.loc['a']
```

### Step 9: Assign expected = Series(...)

```python
expected = Series([1, 'a'], dtype=object, index=['A', 'B'], name='a')
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 11: Assign result = value

```python
result = df.iloc[0]
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': pd.array([1, 2], dtype='Int64'), 'B': np.array([1, 2], dtype='int64')}, index=['a', 'b'])
result = df.loc['a']
expected = Series([1, 1], dtype='Int64', index=['A', 'B'], name='a')
tm.assert_series_equal(result, expected)
result = df.iloc[0]
tm.assert_series_equal(result, expected)
df = DataFrame({'A': pd.array([1, 2], dtype='Int64'), 'B': np.array(['a', 'b'])}, index=['a', 'b'])
result = df.loc['a']
expected = Series([1, 'a'], dtype=object, index=['A', 'B'], name='a')
tm.assert_series_equal(result, expected)
result = df.iloc[0]
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:995 | Complexity: Advanced | Last updated: 2026-06-02*