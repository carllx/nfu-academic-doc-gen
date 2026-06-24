# How To: Setitem Ndarray 1D

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setitem ndarray 1d

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
df = DataFrame(index=Index(np.arange(1, 11), dtype=np.int64))
```

### Step 2: Assign unknown = np.zeros(...)

```python
df['foo'] = np.zeros(10, dtype=np.float64)
```

### Step 3: Assign unknown = np.zeros(...)

```python
df['bar'] = np.zeros(10, dtype=complex)
```

### Step 4: Assign msg = 'Must have equal len keys and value when setting with an iterable'

```python
msg = 'Must have equal len keys and value when setting with an iterable'
```

### Step 5: Assign unknown = np.array(...)

```python
df.loc[df.index[2:6], 'bar'] = np.array([2.33j, 1.23 + 0.1j, 2.2, 1.0])
```

### Step 6: Assign result = value

```python
result = df.loc[df.index[2:6], 'bar']
```

### Step 7: Assign expected = Series(...)

```python
expected = Series([2.33j, 1.23 + 0.1j, 2.2, 1.0], index=[3, 4, 5, 6], name='bar')
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 9: Assign unknown = np.array(...)

```python
df.loc[df.index[2:5], 'bar'] = np.array([2.33j, 1.23 + 0.1j, 2.2, 1.0])
```


## Complete Example

```python
# Workflow
df = DataFrame(index=Index(np.arange(1, 11), dtype=np.int64))
df['foo'] = np.zeros(10, dtype=np.float64)
df['bar'] = np.zeros(10, dtype=complex)
msg = 'Must have equal len keys and value when setting with an iterable'
with pytest.raises(ValueError, match=msg):
    df.loc[df.index[2:5], 'bar'] = np.array([2.33j, 1.23 + 0.1j, 2.2, 1.0])
df.loc[df.index[2:6], 'bar'] = np.array([2.33j, 1.23 + 0.1j, 2.2, 1.0])
result = df.loc[df.index[2:6], 'bar']
expected = Series([2.33j, 1.23 + 0.1j, 2.2, 1.0], index=[3, 4, 5, 6], name='bar')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:40 | Complexity: Advanced | Last updated: 2026-06-02*