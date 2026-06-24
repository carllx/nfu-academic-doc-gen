# How To: Index From Index

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test index from index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tests.copy_view.util`

**Setup Required:**
```python
# Fixtures: using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([1, 2])
```

### Step 2: Assign idx = Index(...)

```python
idx = Index(ser)
```

### Step 3: Assign idx = Index(...)

```python
idx = Index(idx)
```

### Step 4: Assign expected = idx.copy(...)

```python
expected = idx.copy(deep=True)
```

### Step 5: Assign unknown = 100

```python
ser.iloc[0] = 100
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, expected)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, Index([100, 2]))
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, warn_copy_on_write

# Workflow
ser = Series([1, 2])
idx = Index(ser)
idx = Index(idx)
expected = idx.copy(deep=True)
with tm.assert_cow_warning(warn_copy_on_write):
    ser.iloc[0] = 100
if using_copy_on_write:
    tm.assert_index_equal(idx, expected)
else:
    tm.assert_index_equal(idx, Index([100, 2]))
```

## Next Steps


---

*Source: test_index.py:104 | Complexity: Intermediate | Last updated: 2026-06-02*