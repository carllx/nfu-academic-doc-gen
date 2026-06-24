# How To: Fast Unique Multiple List Gen Sort

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fast unique multiple list gen sort

## Prerequisites

**Required Modules:**
- `pickle`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.compat`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign keys = value

```python
keys = [['p', 'a'], ['n', 'd'], ['a', 's']]
```

### Step 2: Assign gen = value

```python
gen = (key for key in keys)
```

### Step 3: Assign expected = np.array(...)

```python
expected = np.array(['a', 'd', 'n', 'p', 's'])
```

### Step 4: Assign out = lib.fast_unique_multiple_list_gen(...)

```python
out = lib.fast_unique_multiple_list_gen(gen, sort=True)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(np.array(out), expected)
```

### Step 6: Assign gen = value

```python
gen = (key for key in keys)
```

### Step 7: Assign expected = np.array(...)

```python
expected = np.array(['p', 'a', 'n', 'd', 's'])
```

### Step 8: Assign out = lib.fast_unique_multiple_list_gen(...)

```python
out = lib.fast_unique_multiple_list_gen(gen, sort=False)
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(np.array(out), expected)
```


## Complete Example

```python
# Workflow
keys = [['p', 'a'], ['n', 'd'], ['a', 's']]
gen = (key for key in keys)
expected = np.array(['a', 'd', 'n', 'p', 's'])
out = lib.fast_unique_multiple_list_gen(gen, sort=True)
tm.assert_numpy_array_equal(np.array(out), expected)
gen = (key for key in keys)
expected = np.array(['p', 'a', 'n', 'd', 's'])
out = lib.fast_unique_multiple_list_gen(gen, sort=False)
tm.assert_numpy_array_equal(np.array(out), expected)
```

## Next Steps


---

*Source: test_lib.py:35 | Complexity: Advanced | Last updated: 2026-06-02*