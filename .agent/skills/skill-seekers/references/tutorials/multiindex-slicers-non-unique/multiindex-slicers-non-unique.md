# How To: Multiindex Slicers Non Unique

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiindex slicers non unique

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.indexing.common`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame.set_index.sort_index(...)

```python
df = DataFrame({'A': ['foo', 'foo', 'foo', 'foo'], 'B': ['a', 'a', 'a', 'a'], 'C': [1, 2, 1, 3], 'D': [1, 2, 3, 4]}).set_index(['A', 'B', 'C']).sort_index()
```

**Verification:**
```python
assert not df.index.is_unique
```

### Step 2: Assign expected = DataFrame.set_index.sort_index(...)

```python
expected = DataFrame({'A': ['foo', 'foo'], 'B': ['a', 'a'], 'C': [1, 1], 'D': [1, 3]}).set_index(['A', 'B', 'C']).sort_index()
```

**Verification:**
```python
assert not df.index.is_unique
```

### Step 3: Assign result = value

```python
result = df.loc[(slice(None), slice(None), 1), :]
```

**Verification:**
```python
assert not result.index.is_unique
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = df.xs(...)

```python
result = df.xs(1, level=2, drop_level=False)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign df = DataFrame.set_index.sort_index(...)

```python
df = DataFrame({'A': ['foo', 'foo', 'foo', 'foo'], 'B': ['a', 'a', 'a', 'a'], 'C': [1, 2, 1, 2], 'D': [1, 2, 3, 4]}).set_index(['A', 'B', 'C']).sort_index()
```

**Verification:**
```python
assert not df.index.is_unique
```

### Step 8: Assign expected = DataFrame.set_index.sort_index(...)

```python
expected = DataFrame({'A': ['foo', 'foo'], 'B': ['a', 'a'], 'C': [1, 1], 'D': [1, 3]}).set_index(['A', 'B', 'C']).sort_index()
```

### Step 9: Assign result = value

```python
result = df.loc[(slice(None), slice(None), 1), :]
```

**Verification:**
```python
assert not result.index.is_unique
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 11: Assign ints = value

```python
ints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 13, 14, 14, 16, 17, 18, 19, 200000, 200000]
```

### Step 12: Assign n = len(...)

```python
n = len(ints)
```

### Step 13: Assign idx = MultiIndex.from_arrays(...)

```python
idx = MultiIndex.from_arrays([['a'] * n, ints])
```

### Step 14: Assign result = Series(...)

```python
result = Series([1] * n, index=idx)
```

### Step 15: Assign result = result.sort_index(...)

```python
result = result.sort_index()
```

### Step 16: Assign result = value

```python
result = result.loc[slice(None), slice(100000)]
```

### Step 17: Assign expected = Series.sort_index(...)

```python
expected = Series([1] * (n - 2), index=idx[:-2]).sort_index()
```

### Step 18: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': ['foo', 'foo', 'foo', 'foo'], 'B': ['a', 'a', 'a', 'a'], 'C': [1, 2, 1, 3], 'D': [1, 2, 3, 4]}).set_index(['A', 'B', 'C']).sort_index()
assert not df.index.is_unique
expected = DataFrame({'A': ['foo', 'foo'], 'B': ['a', 'a'], 'C': [1, 1], 'D': [1, 3]}).set_index(['A', 'B', 'C']).sort_index()
result = df.loc[(slice(None), slice(None), 1), :]
tm.assert_frame_equal(result, expected)
result = df.xs(1, level=2, drop_level=False)
tm.assert_frame_equal(result, expected)
df = DataFrame({'A': ['foo', 'foo', 'foo', 'foo'], 'B': ['a', 'a', 'a', 'a'], 'C': [1, 2, 1, 2], 'D': [1, 2, 3, 4]}).set_index(['A', 'B', 'C']).sort_index()
assert not df.index.is_unique
expected = DataFrame({'A': ['foo', 'foo'], 'B': ['a', 'a'], 'C': [1, 1], 'D': [1, 3]}).set_index(['A', 'B', 'C']).sort_index()
result = df.loc[(slice(None), slice(None), 1), :]
assert not result.index.is_unique
tm.assert_frame_equal(result, expected)
ints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 13, 14, 14, 16, 17, 18, 19, 200000, 200000]
n = len(ints)
idx = MultiIndex.from_arrays([['a'] * n, ints])
result = Series([1] * n, index=idx)
result = result.sort_index()
result = result.loc[slice(None), slice(100000)]
expected = Series([1] * (n - 2), index=idx[:-2]).sort_index()
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_slice.py:166 | Complexity: Advanced | Last updated: 2026-06-02*