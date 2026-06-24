# How To: Astype Category

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test astype category

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
# Fixtures: copy, name, ordered, simple_index
```

## Step-by-Step Guide

### Step 1: Assign idx = simple_index

```python
idx = simple_index
```

### Step 2: Assign dtype = CategoricalDtype(...)

```python
dtype = CategoricalDtype(ordered=ordered)
```

### Step 3: Assign result = idx.astype(...)

```python
result = idx.astype(dtype, copy=copy)
```

### Step 4: Assign expected = CategoricalIndex(...)

```python
expected = CategoricalIndex(idx, name=name, ordered=ordered)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```

### Step 6: Assign dtype = CategoricalDtype(...)

```python
dtype = CategoricalDtype(idx.unique().tolist()[:-1], ordered)
```

### Step 7: Assign result = idx.astype(...)

```python
result = idx.astype(dtype, copy=copy)
```

### Step 8: Assign expected = CategoricalIndex(...)

```python
expected = CategoricalIndex(idx, name=name, dtype=dtype)
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```

### Step 10: Assign idx = idx.rename(...)

```python
idx = idx.rename(name)
```

### Step 11: Assign result = idx.astype(...)

```python
result = idx.astype('category', copy=copy)
```

### Step 12: Assign expected = CategoricalIndex(...)

```python
expected = CategoricalIndex(idx, name=name)
```

### Step 13: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```


## Complete Example

```python
# Setup
# Fixtures: copy, name, ordered, simple_index

# Workflow
idx = simple_index
if name:
    idx = idx.rename(name)
dtype = CategoricalDtype(ordered=ordered)
result = idx.astype(dtype, copy=copy)
expected = CategoricalIndex(idx, name=name, ordered=ordered)
tm.assert_index_equal(result, expected, exact=True)
dtype = CategoricalDtype(idx.unique().tolist()[:-1], ordered)
result = idx.astype(dtype, copy=copy)
expected = CategoricalIndex(idx, name=name, dtype=dtype)
tm.assert_index_equal(result, expected, exact=True)
if ordered is False:
    result = idx.astype('category', copy=copy)
    expected = CategoricalIndex(idx, name=name)
    tm.assert_index_equal(result, expected, exact=True)
```

## Next Steps


---

*Source: test_old_base.py:727 | Complexity: Advanced | Last updated: 2026-06-02*