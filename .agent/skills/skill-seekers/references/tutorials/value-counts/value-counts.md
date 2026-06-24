# How To: Value Counts

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test value counts

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.base.common`

**Setup Required:**
```python
# Fixtures: index_or_series_obj
```

## Step-by-Step Guide

### Step 1: Assign obj = index_or_series_obj

```python
obj = index_or_series_obj
```

### Step 2: Assign obj = np.repeat(...)

```python
obj = np.repeat(obj, range(1, len(obj) + 1))
```

### Step 3: Assign result = obj.value_counts(...)

```python
result = obj.value_counts()
```

### Step 4: Assign counter = collections.Counter(...)

```python
counter = collections.Counter(obj)
```

### Step 5: Assign expected = Series(...)

```python
expected = Series(dict(counter.most_common()), dtype=np.int64, name='count')
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign expected.index = expected.index.astype(...)

```python
expected.index = expected.index.astype(obj.dtype)
```

### Step 8: Assign expected.index.names = value

```python
expected.index.names = obj.names
```

### Step 9: Assign expected.index.name = value

```python
expected.index.name = obj.name
```

### Step 10: Assign result = result.sort_index(...)

```python
result = result.sort_index()
```

### Step 11: Assign expected = expected.sort_index(...)

```python
expected = expected.sort_index()
```

### Step 12: Call expected.index.astype()

```python
expected.index.astype(obj.dtype)
```

### Step 13: Assign expected = expected.astype(...)

```python
expected = expected.astype('int64[pyarrow]')
```

### Step 14: Assign expected = expected.astype(...)

```python
expected = expected.astype('Int64')
```


## Complete Example

```python
# Setup
# Fixtures: index_or_series_obj

# Workflow
obj = index_or_series_obj
obj = np.repeat(obj, range(1, len(obj) + 1))
result = obj.value_counts()
counter = collections.Counter(obj)
expected = Series(dict(counter.most_common()), dtype=np.int64, name='count')
if obj.dtype != np.float16:
    expected.index = expected.index.astype(obj.dtype)
else:
    with pytest.raises(NotImplementedError, match='float16 indexes are not '):
        expected.index.astype(obj.dtype)
    return
if isinstance(expected.index, MultiIndex):
    expected.index.names = obj.names
else:
    expected.index.name = obj.name
if not isinstance(result.dtype, np.dtype):
    if getattr(obj.dtype, 'storage', '') == 'pyarrow':
        expected = expected.astype('int64[pyarrow]')
    else:
        expected = expected.astype('Int64')
if obj.duplicated().any():
    result = result.sort_index()
    expected = expected.sort_index()
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_value_counts.py:24 | Complexity: Advanced | Last updated: 2026-06-02*