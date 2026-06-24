# How To: Repeat

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test repeat

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
# Fixtures: simple_index
```

## Step-by-Step Guide

### Step 1: Assign rep = 2

```python
rep = 2
```

### Step 2: Assign idx = simple_index.copy(...)

```python
idx = simple_index.copy()
```

### Step 3: Assign new_index_cls = value

```python
new_index_cls = idx._constructor
```

### Step 4: Assign expected = new_index_cls(...)

```python
expected = new_index_cls(idx.values.repeat(rep), name=idx.name)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.repeat(rep), expected)
```

### Step 6: Assign idx = simple_index

```python
idx = simple_index
```

### Step 7: Assign rep = np.arange(...)

```python
rep = np.arange(len(idx))
```

### Step 8: Assign expected = new_index_cls(...)

```python
expected = new_index_cls(idx.values.repeat(rep), name=idx.name)
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.repeat(rep), expected)
```


## Complete Example

```python
# Setup
# Fixtures: simple_index

# Workflow
rep = 2
idx = simple_index.copy()
new_index_cls = idx._constructor
expected = new_index_cls(idx.values.repeat(rep), name=idx.name)
tm.assert_index_equal(idx.repeat(rep), expected)
idx = simple_index
rep = np.arange(len(idx))
expected = new_index_cls(idx.values.repeat(rep), name=idx.name)
tm.assert_index_equal(idx.repeat(rep), expected)
```

## Next Steps


---

*Source: test_old_base.py:372 | Complexity: Advanced | Last updated: 2026-06-02*