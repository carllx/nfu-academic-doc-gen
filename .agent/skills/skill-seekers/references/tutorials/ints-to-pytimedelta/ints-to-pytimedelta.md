# How To: Ints To Pytimedelta

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test ints to pytimedelta

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.timedeltas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: unit
```

## Step-by-Step Guide

### Step 1: Assign arr = np.arange.view(...)

```python
arr = np.arange(6, dtype=np.int64).view(f'm8[{unit}]')
```

### Step 2: Assign res = ints_to_pytimedelta(...)

```python
res = ints_to_pytimedelta(arr, box=False)
```

### Step 3: Assign expected = arr.astype(...)

```python
expected = arr.astype(object)
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, expected)
```

### Step 5: Assign res = ints_to_pytimedelta(...)

```python
res = ints_to_pytimedelta(arr, box=True)
```

### Step 6: Assign expected = np.array(...)

```python
expected = np.array([Timedelta(x) for x in arr], dtype=object)
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, expected)
```


## Complete Example

```python
# Setup
# Fixtures: unit

# Workflow
arr = np.arange(6, dtype=np.int64).view(f'm8[{unit}]')
res = ints_to_pytimedelta(arr, box=False)
expected = arr.astype(object)
tm.assert_numpy_array_equal(res, expected)
res = ints_to_pytimedelta(arr, box=True)
expected = np.array([Timedelta(x) for x in arr], dtype=object)
tm.assert_numpy_array_equal(res, expected)
```

## Next Steps


---

*Source: test_timedeltas.py:126 | Complexity: Intermediate | Last updated: 2026-06-02*