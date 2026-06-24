# How To: Arrays For Binary Ufunc

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: A pair of random, length-100 integer-dtype arrays, that are mostly 0.

## Prerequisites

**Required Modules:**
- `collections`
- `re`
- `string`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.arrays`


## Step-by-Step Guide

### Step 1: '\n    A pair of random, length-100 integer-dtype arrays, that are mostly 0.\n    '

```python
'\n    A pair of random, length-100 integer-dtype arrays, that are mostly 0.\n    '
```

### Step 2: Assign a1 = np.random.default_rng.integers(...)

```python
a1 = np.random.default_rng(2).integers(0, 10, 100, dtype='int64')
```

### Step 3: Assign a2 = np.random.default_rng.integers(...)

```python
a2 = np.random.default_rng(2).integers(0, 10, 100, dtype='int64')
```

### Step 4: Assign unknown = 0

```python
a1[::3] = 0
```

### Step 5: Assign unknown = 0

```python
a2[::4] = 0
```


## Complete Example

```python
# Workflow
'\n    A pair of random, length-100 integer-dtype arrays, that are mostly 0.\n    '
a1 = np.random.default_rng(2).integers(0, 10, 100, dtype='int64')
a2 = np.random.default_rng(2).integers(0, 10, 100, dtype='int64')
a1[::3] = 0
a2[::4] = 0
return (a1, a2)
```

## Next Steps


---

*Source: test_ufunc.py:30 | Complexity: Intermediate | Last updated: 2026-06-02*