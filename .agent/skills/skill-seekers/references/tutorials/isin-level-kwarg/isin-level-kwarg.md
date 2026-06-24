# How To: Isin Level Kwarg

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test isin level kwarg

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = MultiIndex.from_arrays(...)

```python
idx = MultiIndex.from_arrays([['qux', 'baz', 'foo', 'bar'], np.arange(4)])
```

### Step 2: Assign vals_0 = value

```python
vals_0 = ['foo', 'bar', 'quux']
```

### Step 3: Assign vals_1 = value

```python
vals_1 = [2, 3, 10]
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([False, False, True, True])
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(expected, idx.isin(vals_0, level=0))
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(expected, idx.isin(vals_0, level=-2))
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(expected, idx.isin(vals_1, level=1))
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(expected, idx.isin(vals_1, level=-1))
```

### Step 9: Assign msg = 'Too many levels: Index has only 2 levels, not 6'

```python
msg = 'Too many levels: Index has only 2 levels, not 6'
```

### Step 10: Assign msg = 'Too many levels: Index has only 2 levels, -5 is not a valid level number'

```python
msg = 'Too many levels: Index has only 2 levels, -5 is not a valid level number'
```

### Step 11: Assign idx.names = value

```python
idx.names = ['A', 'B']
```

### Step 12: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(expected, idx.isin(vals_0, level='A'))
```

### Step 13: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(expected, idx.isin(vals_1, level='B'))
```

### Step 14: Call idx.isin()

```python
idx.isin(vals_0, level=5)
```

### Step 15: Call idx.isin()

```python
idx.isin(vals_0, level=-5)
```

### Step 16: Call idx.isin()

```python
idx.isin(vals_0, level=1.0)
```

### Step 17: Call idx.isin()

```python
idx.isin(vals_1, level=-1.0)
```

### Step 18: Call idx.isin()

```python
idx.isin(vals_1, level='A')
```

### Step 19: Call idx.isin()

```python
idx.isin(vals_1, level='C')
```


## Complete Example

```python
# Workflow
idx = MultiIndex.from_arrays([['qux', 'baz', 'foo', 'bar'], np.arange(4)])
vals_0 = ['foo', 'bar', 'quux']
vals_1 = [2, 3, 10]
expected = np.array([False, False, True, True])
tm.assert_numpy_array_equal(expected, idx.isin(vals_0, level=0))
tm.assert_numpy_array_equal(expected, idx.isin(vals_0, level=-2))
tm.assert_numpy_array_equal(expected, idx.isin(vals_1, level=1))
tm.assert_numpy_array_equal(expected, idx.isin(vals_1, level=-1))
msg = 'Too many levels: Index has only 2 levels, not 6'
with pytest.raises(IndexError, match=msg):
    idx.isin(vals_0, level=5)
msg = 'Too many levels: Index has only 2 levels, -5 is not a valid level number'
with pytest.raises(IndexError, match=msg):
    idx.isin(vals_0, level=-5)
with pytest.raises(KeyError, match="'Level 1\\.0 not found'"):
    idx.isin(vals_0, level=1.0)
with pytest.raises(KeyError, match="'Level -1\\.0 not found'"):
    idx.isin(vals_1, level=-1.0)
with pytest.raises(KeyError, match="'Level A not found'"):
    idx.isin(vals_1, level='A')
idx.names = ['A', 'B']
tm.assert_numpy_array_equal(expected, idx.isin(vals_0, level='A'))
tm.assert_numpy_array_equal(expected, idx.isin(vals_1, level='B'))
with pytest.raises(KeyError, match="'Level C not found'"):
    idx.isin(vals_1, level='C')
```

## Next Steps


---

*Source: test_isin.py:40 | Complexity: Advanced | Last updated: 2026-06-02*