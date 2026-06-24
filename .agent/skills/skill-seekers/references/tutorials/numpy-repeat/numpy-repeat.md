# How To: Numpy Repeat

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test numpy repeat

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

### Step 2: Assign idx = simple_index

```python
idx = simple_index
```

### Step 3: Assign expected = idx.repeat(...)

```python
expected = idx.repeat(rep)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(np.repeat(idx, rep), expected)
```

### Step 5: Assign msg = "the 'axis' parameter is not supported"

```python
msg = "the 'axis' parameter is not supported"
```

### Step 6: Call np.repeat()

```python
np.repeat(idx, rep, axis=0)
```


## Complete Example

```python
# Setup
# Fixtures: simple_index

# Workflow
rep = 2
idx = simple_index
expected = idx.repeat(rep)
tm.assert_index_equal(np.repeat(idx, rep), expected)
msg = "the 'axis' parameter is not supported"
with pytest.raises(ValueError, match=msg):
    np.repeat(idx, rep, axis=0)
```

## Next Steps


---

*Source: test_old_base.py:384 | Complexity: Intermediate | Last updated: 2026-06-02*