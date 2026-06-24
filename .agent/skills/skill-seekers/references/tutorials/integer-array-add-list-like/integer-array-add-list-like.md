# How To: Integer Array Add List Like

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test integer array add list like

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `collections`
- `datetime`
- `decimal`
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.computation`
- `pandas.tests.arithmetic.common`

**Setup Required:**
```python
# Fixtures: box_pandas_1d_array, box_1d_array, data, expected_data
```

## Step-by-Step Guide

### Step 1: Assign arr = array(...)

```python
arr = array(data, dtype='Int64')
```

### Step 2: Assign container = box_pandas_1d_array(...)

```python
container = box_pandas_1d_array(arr)
```

### Step 3: Assign left = value

```python
left = container + box_1d_array(data)
```

### Step 4: Assign right = value

```python
right = box_1d_array(data) + container
```

### Step 5: Assign expected = cls(...)

```python
expected = cls(expected_data, dtype='Int64')
```

### Step 6: Call tm.assert_equal()

```python
tm.assert_equal(left, expected)
```

### Step 7: Call tm.assert_equal()

```python
tm.assert_equal(right, expected)
```

### Step 8: Assign cls = Series

```python
cls = Series
```

### Step 9: Assign cls = Index

```python
cls = Index
```

### Step 10: Assign cls = array

```python
cls = array
```


## Complete Example

```python
# Setup
# Fixtures: box_pandas_1d_array, box_1d_array, data, expected_data

# Workflow
arr = array(data, dtype='Int64')
container = box_pandas_1d_array(arr)
left = container + box_1d_array(data)
right = box_1d_array(data) + container
if Series in [box_1d_array, box_pandas_1d_array]:
    cls = Series
elif Index in [box_1d_array, box_pandas_1d_array]:
    cls = Index
else:
    cls = array
expected = cls(expected_data, dtype='Int64')
tm.assert_equal(left, expected)
tm.assert_equal(right, expected)
```

## Next Steps


---

*Source: test_numeric.py:1506 | Complexity: Advanced | Last updated: 2026-06-02*