# How To: Offset Mul Ndarray

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test offset mul ndarray

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.offsets`
- `pandas._libs.tslibs.offsets`
- `pandas._libs.tslibs.period`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.tests.tseries.offsets.common`
- `pandas.tseries`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: offset_types
```

## Step-by-Step Guide

### Step 1: Assign off = _create_offset(...)

```python
off = _create_offset(offset_types)
```

### Step 2: Assign expected = np.array(...)

```python
expected = np.array([[off, off * 2], [off * 3, off * 4]])
```

### Step 3: Assign result = value

```python
result = np.array([[1, 2], [3, 4]]) * off
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 5: Assign result = value

```python
result = off * np.array([[1, 2], [3, 4]])
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: offset_types

# Workflow
off = _create_offset(offset_types)
expected = np.array([[off, off * 2], [off * 3, off * 4]])
result = np.array([[1, 2], [3, 4]]) * off
tm.assert_numpy_array_equal(result, expected)
result = off * np.array([[1, 2], [3, 4]])
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_offsets.py:223 | Complexity: Intermediate | Last updated: 2026-06-02*