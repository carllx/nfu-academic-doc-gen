# How To: Nditer Multi Index Set Refcount

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test nditer multi index set refcount

## Prerequisites

**Required Modules:**
- `inspect`
- `subprocess`
- `sys`
- `textwrap`
- `warnings`
- `pytest`
- `numpy`
- `numpy._core._multiarray_tests`
- `numpy._core.umath`
- `numpy`
- `numpy.testing`
- `numpy.testing._private.utils`


## Step-by-Step Guide

### Step 1: Assign index = 0

```python
index = 0
```

**Verification:**
```python
assert_equal(start_count, end_count)
```

### Step 2: Assign i = np.nditer(...)

```python
i = np.nditer(np.array([111, 222, 333, 444]), flags=['multi_index'])
```

### Step 3: Assign start_count = sys.getrefcount(...)

```python
start_count = sys.getrefcount(index)
```

### Step 4: Assign i.multi_index = value

```python
i.multi_index = (index,)
```

### Step 5: Assign end_count = sys.getrefcount(...)

```python
end_count = sys.getrefcount(index)
```

### Step 6: Call assert_equal()

```python
assert_equal(start_count, end_count)
```


## Complete Example

```python
# Workflow
index = 0
i = np.nditer(np.array([111, 222, 333, 444]), flags=['multi_index'])
start_count = sys.getrefcount(index)
i.multi_index = (index,)
end_count = sys.getrefcount(index)
assert_equal(start_count, end_count)
```

## Next Steps


---

*Source: test_nditer.py:209 | Complexity: Intermediate | Last updated: 2026-06-02*