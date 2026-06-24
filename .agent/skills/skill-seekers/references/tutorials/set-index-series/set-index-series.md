# How To: Set Index Series

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set index series

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

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2], 'b': 1.5})
```

### Step 2: Assign ser = Series(...)

```python
ser = Series([10, 11])
```

### Step 3: Assign df = df.set_index(...)

```python
df = df.set_index(ser)
```

### Step 4: Assign expected = df.index.copy(...)

```python
expected = df.index.copy(deep=True)
```

### Step 5: Assign unknown = 100

```python
ser.iloc[0] = 100
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(df.index, expected)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(df.index, Index([100, 11]))
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, warn_copy_on_write

# Workflow
df = DataFrame({'a': [1, 2], 'b': 1.5})
ser = Series([10, 11])
df = df.set_index(ser)
expected = df.index.copy(deep=True)
with tm.assert_cow_warning(warn_copy_on_write):
    ser.iloc[0] = 100
if using_copy_on_write:
    tm.assert_index_equal(df.index, expected)
else:
    tm.assert_index_equal(df.index, Index([100, 11]))
```

## Next Steps


---

*Source: test_index.py:43 | Complexity: Intermediate | Last updated: 2026-06-02*