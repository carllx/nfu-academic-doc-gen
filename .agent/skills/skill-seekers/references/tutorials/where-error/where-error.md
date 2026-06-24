# How To: Where Error

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test where error

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(np.random.default_rng(2).standard_normal(5))
```

### Step 2: Assign cond = value

```python
cond = s > 0
```

### Step 3: Assign msg = 'Array conditional must be same shape as self'

```python
msg = 'Array conditional must be same shape as self'
```

### Step 4: Assign s = Series(...)

```python
s = Series([1, 2])
```

### Step 5: Assign unknown = value

```python
s[[True, False]] = [0, 1]
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([0, 2])
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s, expected)
```

### Step 8: Assign msg = 'cannot set using a list-like indexer with a different length than the value'

```python
msg = 'cannot set using a list-like indexer with a different length than the value'
```

### Step 9: Call s.where()

```python
s.where(1)
```

### Step 10: Call s.where()

```python
s.where(cond[:3].values, -s)
```

### Step 11: Assign unknown = value

```python
s[[True, False]] = [0, 2, 3]
```

### Step 12: Assign unknown = value

```python
s[[True, False]] = []
```


## Complete Example

```python
# Workflow
s = Series(np.random.default_rng(2).standard_normal(5))
cond = s > 0
msg = 'Array conditional must be same shape as self'
with pytest.raises(ValueError, match=msg):
    s.where(1)
with pytest.raises(ValueError, match=msg):
    s.where(cond[:3].values, -s)
s = Series([1, 2])
s[[True, False]] = [0, 1]
expected = Series([0, 2])
tm.assert_series_equal(s, expected)
msg = 'cannot set using a list-like indexer with a different length than the value'
with pytest.raises(ValueError, match=msg):
    s[[True, False]] = [0, 2, 3]
with pytest.raises(ValueError, match=msg):
    s[[True, False]] = []
```

## Next Steps


---

*Source: test_where.py:152 | Complexity: Advanced | Last updated: 2026-06-02*