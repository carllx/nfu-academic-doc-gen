# How To: Ufunc Reduce Raises

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test ufunc reduce raises

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: values
```

## Step-by-Step Guide

### Step 1: Assign arr = pd.array(...)

```python
arr = pd.array(values, dtype='boolean')
```

### Step 2: Assign res = np.add.reduce(...)

```python
res = np.add.reduce(arr)
```

### Step 3: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(res, expected)
```

### Step 4: Assign expected = value

```python
expected = pd.NA
```

### Step 5: Assign expected = arr._data.sum(...)

```python
expected = arr._data.sum()
```


## Complete Example

```python
# Setup
# Fixtures: values

# Workflow
arr = pd.array(values, dtype='boolean')
res = np.add.reduce(arr)
if arr[-1] is pd.NA:
    expected = pd.NA
else:
    expected = arr._data.sum()
tm.assert_almost_equal(res, expected)
```

## Next Steps


---

*Source: test_function.py:81 | Complexity: Intermediate | Last updated: 2026-06-02*