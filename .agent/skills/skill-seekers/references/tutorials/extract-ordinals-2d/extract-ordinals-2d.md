# How To: Extract Ordinals 2D

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test extract ordinals 2d

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.period`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign freq = to_offset(...)

```python
freq = to_offset('D')
```

### Step 2: Assign arr = np.empty(...)

```python
arr = np.empty(10, dtype=object)
```

### Step 3: Assign unknown = iNaT

```python
arr[:] = iNaT
```

### Step 4: Assign res = extract_ordinals(...)

```python
res = extract_ordinals(arr, freq)
```

### Step 5: Assign res2 = extract_ordinals(...)

```python
res2 = extract_ordinals(arr.reshape(5, 2), freq)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, res2.reshape(-1))
```


## Complete Example

```python
# Workflow
freq = to_offset('D')
arr = np.empty(10, dtype=object)
arr[:] = iNaT
res = extract_ordinals(arr, freq)
res2 = extract_ordinals(arr.reshape(5, 2), freq)
tm.assert_numpy_array_equal(res, res2.reshape(-1))
```

## Next Steps


---

*Source: test_period.py:110 | Complexity: Intermediate | Last updated: 2026-06-02*