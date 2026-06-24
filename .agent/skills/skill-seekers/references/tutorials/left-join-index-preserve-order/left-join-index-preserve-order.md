# How To: Left Join Index Preserve Order

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test left join index preserve order

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.concat`
- `pandas.core.reshape.merge`


## Step-by-Step Guide

### Step 1: Assign on_cols = value

```python
on_cols = ['k1', 'k2']
```

### Step 2: Assign left = DataFrame(...)

```python
left = DataFrame({'k1': [0, 1, 2] * 8, 'k2': ['foo', 'bar'] * 12, 'v': np.array(np.arange(24), dtype=np.int64)})
```

### Step 3: Assign index = MultiIndex.from_tuples(...)

```python
index = MultiIndex.from_tuples([(2, 'bar'), (1, 'foo')])
```

### Step 4: Assign right = DataFrame(...)

```python
right = DataFrame({'v2': [5, 7]}, index=index)
```

### Step 5: Assign result = left.join(...)

```python
result = left.join(right, on=on_cols)
```

### Step 6: Assign expected = left.copy(...)

```python
expected = left.copy()
```

### Step 7: Assign unknown = value

```python
expected['v2'] = np.nan
```

### Step 8: Assign unknown = 5

```python
expected.loc[(expected.k1 == 2) & (expected.k2 == 'bar'), 'v2'] = 5
```

### Step 9: Assign unknown = 7

```python
expected.loc[(expected.k1 == 1) & (expected.k2 == 'foo'), 'v2'] = 7
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 11: Call result.sort_values()

```python
result.sort_values(on_cols, kind='mergesort', inplace=True)
```

### Step 12: Assign expected = left.join(...)

```python
expected = left.join(right, on=on_cols, sort=True)
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 14: Assign left = DataFrame(...)

```python
left = DataFrame({'k1': [0, 1, 2] * 8, 'k2': ['foo', 'bar'] * 12, 'k3': np.array([0, 1, 2] * 8, dtype=np.float32), 'v': np.array(np.arange(24), dtype=np.int32)})
```

### Step 15: Assign index = MultiIndex.from_tuples(...)

```python
index = MultiIndex.from_tuples([(2, 'bar'), (1, 'foo')])
```

### Step 16: Assign right = DataFrame(...)

```python
right = DataFrame({'v2': [5, 7]}, index=index)
```

### Step 17: Assign result = left.join(...)

```python
result = left.join(right, on=on_cols)
```

### Step 18: Assign expected = left.copy(...)

```python
expected = left.copy()
```

### Step 19: Assign unknown = value

```python
expected['v2'] = np.nan
```

### Step 20: Assign unknown = 5

```python
expected.loc[(expected.k1 == 2) & (expected.k2 == 'bar'), 'v2'] = 5
```

### Step 21: Assign unknown = 7

```python
expected.loc[(expected.k1 == 1) & (expected.k2 == 'foo'), 'v2'] = 7
```

### Step 22: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 23: Assign result = result.sort_values(...)

```python
result = result.sort_values(on_cols, kind='mergesort')
```

### Step 24: Assign expected = left.join(...)

```python
expected = left.join(right, on=on_cols, sort=True)
```

### Step 25: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
on_cols = ['k1', 'k2']
left = DataFrame({'k1': [0, 1, 2] * 8, 'k2': ['foo', 'bar'] * 12, 'v': np.array(np.arange(24), dtype=np.int64)})
index = MultiIndex.from_tuples([(2, 'bar'), (1, 'foo')])
right = DataFrame({'v2': [5, 7]}, index=index)
result = left.join(right, on=on_cols)
expected = left.copy()
expected['v2'] = np.nan
expected.loc[(expected.k1 == 2) & (expected.k2 == 'bar'), 'v2'] = 5
expected.loc[(expected.k1 == 1) & (expected.k2 == 'foo'), 'v2'] = 7
tm.assert_frame_equal(result, expected)
result.sort_values(on_cols, kind='mergesort', inplace=True)
expected = left.join(right, on=on_cols, sort=True)
tm.assert_frame_equal(result, expected)
left = DataFrame({'k1': [0, 1, 2] * 8, 'k2': ['foo', 'bar'] * 12, 'k3': np.array([0, 1, 2] * 8, dtype=np.float32), 'v': np.array(np.arange(24), dtype=np.int32)})
index = MultiIndex.from_tuples([(2, 'bar'), (1, 'foo')])
right = DataFrame({'v2': [5, 7]}, index=index)
result = left.join(right, on=on_cols)
expected = left.copy()
expected['v2'] = np.nan
expected.loc[(expected.k1 == 2) & (expected.k2 == 'bar'), 'v2'] = 5
expected.loc[(expected.k1 == 1) & (expected.k2 == 'foo'), 'v2'] = 7
tm.assert_frame_equal(result, expected)
result = result.sort_values(on_cols, kind='mergesort')
expected = left.join(right, on=on_cols, sort=True)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_multi.py:221 | Complexity: Advanced | Last updated: 2026-06-02*