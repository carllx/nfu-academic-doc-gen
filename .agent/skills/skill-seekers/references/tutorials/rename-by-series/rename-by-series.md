# How To: Rename By Series

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rename by series

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(range(5), name='foo')
```

### Step 2: Assign renamer = Series(...)

```python
renamer = Series({1: 10, 2: 20})
```

### Step 3: Assign result = ser.rename(...)

```python
result = ser.rename(renamer)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series(range(5), index=[0, 10, 20, 3, 4], name='foo')
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
ser = Series(range(5), name='foo')
renamer = Series({1: 10, 2: 20})
result = ser.rename(renamer)
expected = Series(range(5), index=[0, 10, 20, 3, 4], name='foo')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_rename.py:42 | Complexity: Intermediate | Last updated: 2026-06-02*