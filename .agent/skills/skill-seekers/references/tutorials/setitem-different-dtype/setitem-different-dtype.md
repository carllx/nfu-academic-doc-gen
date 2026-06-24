# How To: Setitem Different Dtype

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setitem different dtype

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.base`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((5, 3)), index=np.arange(5), columns=['c', 'b', 'a'])
```

### Step 2: Call df.insert()

```python
df.insert(0, 'foo', df['a'])
```

### Step 3: Call df.insert()

```python
df.insert(2, 'bar', df['c'])
```

### Step 4: Assign unknown = unknown.astype(...)

```python
df['x'] = df['a'].astype('float32')
```

### Step 5: Assign result = value

```python
result = df.dtypes
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([np.dtype('float64')] * 5 + [np.dtype('float32')], index=['foo', 'c', 'bar', 'b', 'a', 'x'])
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign unknown = unknown.astype(...)

```python
df['a'] = df['a'].astype('float32')
```

### Step 9: Assign result = value

```python
result = df.dtypes
```

### Step 10: Assign expected = Series(...)

```python
expected = Series([np.dtype('float64')] * 4 + [np.dtype('float32')] * 2, index=['foo', 'c', 'bar', 'b', 'a', 'x'])
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 12: Assign unknown = unknown.astype(...)

```python
df['y'] = df['a'].astype('int32')
```

### Step 13: Assign result = value

```python
result = df.dtypes
```

### Step 14: Assign expected = Series(...)

```python
expected = Series([np.dtype('float64')] * 4 + [np.dtype('float32')] * 2 + [np.dtype('int32')], index=['foo', 'c', 'bar', 'b', 'a', 'x', 'y'])
```

### Step 15: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((5, 3)), index=np.arange(5), columns=['c', 'b', 'a'])
df.insert(0, 'foo', df['a'])
df.insert(2, 'bar', df['c'])
df['x'] = df['a'].astype('float32')
result = df.dtypes
expected = Series([np.dtype('float64')] * 5 + [np.dtype('float32')], index=['foo', 'c', 'bar', 'b', 'a', 'x'])
tm.assert_series_equal(result, expected)
df['a'] = df['a'].astype('float32')
result = df.dtypes
expected = Series([np.dtype('float64')] * 4 + [np.dtype('float32')] * 2, index=['foo', 'c', 'bar', 'b', 'a', 'x'])
tm.assert_series_equal(result, expected)
df['y'] = df['a'].astype('int32')
result = df.dtypes
expected = Series([np.dtype('float64')] * 4 + [np.dtype('float32')] * 2 + [np.dtype('int32')], index=['foo', 'c', 'bar', 'b', 'a', 'x', 'y'])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_setitem.py:113 | Complexity: Advanced | Last updated: 2026-06-02*