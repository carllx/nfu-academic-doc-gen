# How To: Where Setitem Invalid

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test where setitem invalid

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign msg = value

```python
msg = lambda x: f'cannot set using a {x} indexer with a different length than the value'
```

### Step 2: Assign s = Series(...)

```python
s = Series(list('abc'), dtype=object)
```

### Step 3: Assign unknown = list(...)

```python
s[0:3] = list(range(3))
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([0, 1, 2])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s.astype(np.int64), expected)
```

### Step 6: Assign s = Series(...)

```python
s = Series(list('abcdef'), dtype=object)
```

### Step 7: Assign s = Series(...)

```python
s = Series(list('abcdef'), dtype=object)
```

### Step 8: Assign unknown = list(...)

```python
s[0:4:2] = list(range(2))
```

### Step 9: Assign expected = Series(...)

```python
expected = Series([0, 'b', 1, 'd', 'e', 'f'])
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s, expected)
```

### Step 11: Assign s = Series(...)

```python
s = Series(list('abcdef'), dtype=object)
```

### Step 12: Assign unknown = list(...)

```python
s[-3:-1] = list(range(2))
```

### Step 13: Assign expected = Series(...)

```python
expected = Series(['a', 'b', 'c', 0, 1, 'f'])
```

### Step 14: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s, expected)
```

### Step 15: Assign s = Series(...)

```python
s = Series(list('abc'), dtype=object)
```

### Step 16: Assign s = Series(...)

```python
s = Series(list('abc'), dtype=object)
```

### Step 17: Assign s = Series(...)

```python
s = Series(list('abc'), dtype=object)
```

### Step 18: Assign unknown = list(...)

```python
s[0] = list(range(10))
```

### Step 19: Assign expected = Series(...)

```python
expected = Series([list(range(10)), 'b', 'c'])
```

### Step 20: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s, expected)
```

### Step 21: Assign unknown = list(...)

```python
s[0:3] = list(range(27))
```

### Step 22: Assign unknown = list(...)

```python
s[0:4:2] = list(range(27))
```

### Step 23: Assign unknown = list(...)

```python
s[:-1] = list(range(27))
```

### Step 24: Assign unknown = list(...)

```python
s[[0, 1, 2]] = list(range(27))
```

### Step 25: Assign unknown = list(...)

```python
s[[0, 1, 2]] = list(range(2))
```


## Complete Example

```python
# Workflow
msg = lambda x: f'cannot set using a {x} indexer with a different length than the value'
s = Series(list('abc'), dtype=object)
with pytest.raises(ValueError, match=msg('slice')):
    s[0:3] = list(range(27))
s[0:3] = list(range(3))
expected = Series([0, 1, 2])
tm.assert_series_equal(s.astype(np.int64), expected)
s = Series(list('abcdef'), dtype=object)
with pytest.raises(ValueError, match=msg('slice')):
    s[0:4:2] = list(range(27))
s = Series(list('abcdef'), dtype=object)
s[0:4:2] = list(range(2))
expected = Series([0, 'b', 1, 'd', 'e', 'f'])
tm.assert_series_equal(s, expected)
s = Series(list('abcdef'), dtype=object)
with pytest.raises(ValueError, match=msg('slice')):
    s[:-1] = list(range(27))
s[-3:-1] = list(range(2))
expected = Series(['a', 'b', 'c', 0, 1, 'f'])
tm.assert_series_equal(s, expected)
s = Series(list('abc'), dtype=object)
with pytest.raises(ValueError, match=msg('list-like')):
    s[[0, 1, 2]] = list(range(27))
s = Series(list('abc'), dtype=object)
with pytest.raises(ValueError, match=msg('list-like')):
    s[[0, 1, 2]] = list(range(2))
s = Series(list('abc'), dtype=object)
s[0] = list(range(10))
expected = Series([list(range(10)), 'b', 'c'])
tm.assert_series_equal(s, expected)
```

## Next Steps


---

*Source: test_where.py:233 | Complexity: Advanced | Last updated: 2026-06-02*