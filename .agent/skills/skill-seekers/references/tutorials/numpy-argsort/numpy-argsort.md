# How To: Numpy Argsort

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test numpy argsort

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `weakref`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: index
```

## Step-by-Step Guide

### Step 1: Assign result = np.argsort(...)

```python
result = np.argsort(index)
```

### Step 2: Assign expected = index.argsort(...)

```python
expected = index.argsort()
```

### Step 3: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 4: Assign result = np.argsort(...)

```python
result = np.argsort(index, kind='mergesort')
```

### Step 5: Assign expected = index.argsort(...)

```python
expected = index.argsort(kind='mergesort')
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 7: Assign msg = "the 'axis' parameter is not supported"

```python
msg = "the 'axis' parameter is not supported"
```

### Step 8: Assign msg = "the 'order' parameter is not supported"

```python
msg = "the 'order' parameter is not supported"
```

### Step 9: Call np.argsort()

```python
np.argsort(index, axis=1)
```

### Step 10: Call np.argsort()

```python
np.argsort(index, order=('a', 'b'))
```


## Complete Example

```python
# Setup
# Fixtures: index

# Workflow
result = np.argsort(index)
expected = index.argsort()
tm.assert_numpy_array_equal(result, expected)
result = np.argsort(index, kind='mergesort')
expected = index.argsort(kind='mergesort')
tm.assert_numpy_array_equal(result, expected)
if isinstance(index, (CategoricalIndex, RangeIndex)):
    msg = "the 'axis' parameter is not supported"
    with pytest.raises(ValueError, match=msg):
        np.argsort(index, axis=1)
    msg = "the 'order' parameter is not supported"
    with pytest.raises(ValueError, match=msg):
        np.argsort(index, order=('a', 'b'))
```

## Next Steps


---

*Source: test_old_base.py:347 | Complexity: Advanced | Last updated: 2026-06-02*