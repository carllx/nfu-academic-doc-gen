# How To: Assign Index As Index

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test assign index as index

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

### Step 3: Assign rhs_index = Index(...)

```python
rhs_index = Index(ser)
```

### Step 4: Assign df.index = rhs_index

```python
df.index = rhs_index
```

### Step 5: Assign rhs_index = None

```python
rhs_index = None
```

### Step 6: Assign expected = df.index.copy(...)

```python
expected = df.index.copy(deep=True)
```

### Step 7: Assign unknown = 100

```python
ser.iloc[0] = 100
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(df.index, expected)
```

### Step 9: Call tm.assert_index_equal()

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
rhs_index = Index(ser)
df.index = rhs_index
rhs_index = None
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

*Source: test_index.py:69 | Complexity: Advanced | Last updated: 2026-06-02*