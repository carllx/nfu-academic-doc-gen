# How To: String Dtype Fill Value Persists Through Slice

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test string dtype fill value persists through slice

## Prerequisites

**Required Modules:**
- `copy`
- `inspect`
- `itertools`
- `operator`
- `pickle`
- `sys`
- `textwrap`
- `warnings`
- `functools`
- `pytest`
- `numpy`
- `numpy._core.fromnumeric`
- `numpy._core.umath`
- `numpy.ma.core`
- `numpy`
- `numpy._utils`
- `numpy.exceptions`
- `numpy.ma.core`
- `numpy.ma.testutils`
- `numpy.testing`
- `numpy.testing._private.utils`
- `datetime`
- `copy`
- `io`
- `copy`
- `copy`


## Step-by-Step Guide

### Step 1: Assign dt = np.dtypes.StringDType(...)

```python
dt = np.dtypes.StringDType()
```

**Verification:**
```python
assert isinstance(sub.fill_value, str)
```

### Step 2: Assign arr = np.ma.MaskedArray(...)

```python
arr = np.ma.MaskedArray(['a', 'b', 'c'], mask=[True, False, True], dtype=dt)
```

**Verification:**
```python
assert sub.fill_value == 'Z'
```

### Step 3: Assign arr.fill_value = 'Z'

```python
arr.fill_value = 'Z'
```

**Verification:**
```python
assert sub.filled().tolist() == ['b', 'Z']
```

### Step 4: Assign sub = value

```python
sub = arr[1:]
```

**Verification:**
```python
assert isinstance(sub.fill_value, str)
```


## Complete Example

```python
# Workflow
dt = np.dtypes.StringDType()
arr = np.ma.MaskedArray(['a', 'b', 'c'], mask=[True, False, True], dtype=dt)
arr.fill_value = 'Z'
sub = arr[1:]
assert isinstance(sub.fill_value, str)
assert sub.fill_value == 'Z'
assert sub.filled().tolist() == ['b', 'Z']
```

## Next Steps


---

*Source: test_core.py:5744 | Complexity: Intermediate | Last updated: 2026-06-02*