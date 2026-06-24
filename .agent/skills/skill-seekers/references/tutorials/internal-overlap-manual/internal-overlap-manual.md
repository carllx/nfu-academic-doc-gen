# How To: Internal Overlap Manual

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test internal overlap manual

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `numpy`
- `numpy._core`
- `numpy._core._multiarray_tests`
- `numpy.lib.stride_tricks`
- `numpy.testing`
- `numpy.lib._stride_tricks_impl`


## Step-by-Step Guide

### Step 1: Assign x = np.arange.astype(...)

```python
x = np.arange(1).astype(np.int8)
```

### Step 2: Call check_internal_overlap()

```python
check_internal_overlap(x, False)
```

### Step 3: Call check_internal_overlap()

```python
check_internal_overlap(x.reshape([]), False)
```

### Step 4: Assign a = as_strided(...)

```python
a = as_strided(x, strides=(3, 4), shape=(4, 4))
```

### Step 5: Call check_internal_overlap()

```python
check_internal_overlap(a, False)
```

### Step 6: Assign a = as_strided(...)

```python
a = as_strided(x, strides=(3, 4), shape=(5, 4))
```

### Step 7: Call check_internal_overlap()

```python
check_internal_overlap(a, True)
```

### Step 8: Assign a = as_strided(...)

```python
a = as_strided(x, strides=(0,), shape=(0,))
```

### Step 9: Call check_internal_overlap()

```python
check_internal_overlap(a, False)
```

### Step 10: Assign a = as_strided(...)

```python
a = as_strided(x, strides=(0,), shape=(1,))
```

### Step 11: Call check_internal_overlap()

```python
check_internal_overlap(a, False)
```

### Step 12: Assign a = as_strided(...)

```python
a = as_strided(x, strides=(0,), shape=(2,))
```

### Step 13: Call check_internal_overlap()

```python
check_internal_overlap(a, True)
```

### Step 14: Assign a = as_strided(...)

```python
a = as_strided(x, strides=(0, -9993), shape=(87, 22))
```

### Step 15: Call check_internal_overlap()

```python
check_internal_overlap(a, True)
```

### Step 16: Assign a = as_strided(...)

```python
a = as_strided(x, strides=(0, -9993), shape=(1, 22))
```

### Step 17: Call check_internal_overlap()

```python
check_internal_overlap(a, False)
```

### Step 18: Assign a = as_strided(...)

```python
a = as_strided(x, strides=(0, -9993), shape=(0, 22))
```

### Step 19: Call check_internal_overlap()

```python
check_internal_overlap(a, False)
```


## Complete Example

```python
# Workflow
x = np.arange(1).astype(np.int8)
check_internal_overlap(x, False)
check_internal_overlap(x.reshape([]), False)
a = as_strided(x, strides=(3, 4), shape=(4, 4))
check_internal_overlap(a, False)
a = as_strided(x, strides=(3, 4), shape=(5, 4))
check_internal_overlap(a, True)
a = as_strided(x, strides=(0,), shape=(0,))
check_internal_overlap(a, False)
a = as_strided(x, strides=(0,), shape=(1,))
check_internal_overlap(a, False)
a = as_strided(x, strides=(0,), shape=(2,))
check_internal_overlap(a, True)
a = as_strided(x, strides=(0, -9993), shape=(87, 22))
check_internal_overlap(a, True)
a = as_strided(x, strides=(0, -9993), shape=(1, 22))
check_internal_overlap(a, False)
a = as_strided(x, strides=(0, -9993), shape=(0, 22))
check_internal_overlap(a, False)
```

## Next Steps


---

*Source: test_mem_overlap.py:477 | Complexity: Advanced | Last updated: 2026-06-02*