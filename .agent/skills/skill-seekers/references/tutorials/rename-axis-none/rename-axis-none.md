# How To: Rename Axis None

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test rename axis none

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: kwargs
```

## Step-by-Step Guide

### Step 1: Assign index = Index(...)

```python
index = Index(list('abc'), name='foo')
```

### Step 2: Assign ser = Series(...)

```python
ser = Series([1, 2, 3], index=index)
```

### Step 3: Assign result = ser.rename_axis(...)

```python
result = ser.rename_axis(**kwargs)
```

### Step 4: Assign expected_index = value

```python
expected_index = index.rename(None) if kwargs else index
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([1, 2, 3], index=expected_index)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: kwargs

# Workflow
index = Index(list('abc'), name='foo')
ser = Series([1, 2, 3], index=index)
result = ser.rename_axis(**kwargs)
expected_index = index.rename(None) if kwargs else index
expected = Series([1, 2, 3], index=expected_index)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_rename_axis.py:39 | Complexity: Intermediate | Last updated: 2026-06-02*