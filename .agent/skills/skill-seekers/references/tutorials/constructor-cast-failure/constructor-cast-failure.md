# How To: Constructor Cast Failure

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor cast failure

## Prerequisites

**Required Modules:**
- `array`
- `collections`
- `collections.abc`
- `dataclasses`
- `datetime`
- `functools`
- `re`
- `numpy`
- `numpy`
- `numpy.ma`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas.compat.numpy`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.arrays`
- `numpy.dtypes`


## Step-by-Step Guide

### Step 1: Assign msg = 'could not convert string to float'

```python
msg = 'could not convert string to float'
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.ones((4, 2)))
```

### Step 3: Assign unknown = np.ones.tolist(...)

```python
df['foo'] = np.ones((4, 2)).tolist()
```

### Step 4: Assign msg = 'Expected a 1D array, got an array with shape \\(4, 2\\)'

```python
msg = 'Expected a 1D array, got an array with shape \\(4, 2\\)'
```

### Step 5: Assign unknown = np.ones.tolist(...)

```python
df['foo2'] = np.ones((4, 2)).tolist()
```

### Step 6: Call DataFrame()

```python
DataFrame({'a': ['a', 'b', 'c']}, dtype=np.float64)
```

### Step 7: Assign unknown = np.ones(...)

```python
df['test'] = np.ones((4, 2))
```


## Complete Example

```python
# Workflow
msg = 'could not convert string to float'
with pytest.raises(ValueError, match=msg):
    DataFrame({'a': ['a', 'b', 'c']}, dtype=np.float64)
df = DataFrame(np.ones((4, 2)))
df['foo'] = np.ones((4, 2)).tolist()
msg = 'Expected a 1D array, got an array with shape \\(4, 2\\)'
with pytest.raises(ValueError, match=msg):
    df['test'] = np.ones((4, 2))
df['foo2'] = np.ones((4, 2)).tolist()
```

## Next Steps


---

*Source: test_constructors.py:269 | Complexity: Intermediate | Last updated: 2026-06-02*