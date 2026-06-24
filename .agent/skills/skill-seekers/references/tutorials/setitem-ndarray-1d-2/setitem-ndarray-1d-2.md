# How To: Setitem Ndarray 1D 2

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setitem ndarray 1d 2

## Prerequisites

**Required Modules:**
- `array`
- `datetime`
- `re`
- `weakref`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.indexing.common`
- `pandas.tests.indexing.test_floats`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(index=Index(np.arange(1, 11)))
```

### Step 2: Assign unknown = np.zeros(...)

```python
df['foo'] = np.zeros(10, dtype=np.float64)
```

### Step 3: Assign unknown = np.zeros(...)

```python
df['bar'] = np.zeros(10, dtype=complex)
```

### Step 4: Assign msg = 'Must have equal len keys and value when setting with an iterable'

```python
msg = 'Must have equal len keys and value when setting with an iterable'
```

### Step 5: Assign unknown = value

```python
df[2:5] = np.arange(1, 4) * 1j
```


## Complete Example

```python
# Workflow
df = DataFrame(index=Index(np.arange(1, 11)))
df['foo'] = np.zeros(10, dtype=np.float64)
df['bar'] = np.zeros(10, dtype=complex)
msg = 'Must have equal len keys and value when setting with an iterable'
with pytest.raises(ValueError, match=msg):
    df[2:5] = np.arange(1, 4) * 1j
```

## Next Steps


---

*Source: test_indexing.py:62 | Complexity: Intermediate | Last updated: 2026-06-02*