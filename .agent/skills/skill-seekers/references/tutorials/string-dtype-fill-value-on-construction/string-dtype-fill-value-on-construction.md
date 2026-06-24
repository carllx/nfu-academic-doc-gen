# How To: String Dtype Fill Value On Construction

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test string dtype fill value on construction

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
assert isinstance(arr.fill_value, str)
```

### Step 2: Assign data = np.array(...)

```python
data = np.array(['A', 'test', 'variable', ''], dtype=dt)
```

**Verification:**
```python
assert arr.fill_value == 'FILL'
```

### Step 3: Assign mask = value

```python
mask = [True, False, True, True]
```

**Verification:**
```python
assert filled.tolist() == ['FILL', 'test', 'FILL', 'FILL']
```

### Step 4: Assign arr = np.ma.MaskedArray(...)

```python
arr = np.ma.MaskedArray(data, mask=mask, fill_value='FILL', dtype=dt)
```

**Verification:**
```python
assert isinstance(arr.fill_value, str)
```

### Step 5: Assign filled = arr.filled(...)

```python
filled = arr.filled()
```

**Verification:**
```python
assert filled.tolist() == ['FILL', 'test', 'FILL', 'FILL']
```


## Complete Example

```python
# Workflow
dt = np.dtypes.StringDType()
data = np.array(['A', 'test', 'variable', ''], dtype=dt)
mask = [True, False, True, True]
arr = np.ma.MaskedArray(data, mask=mask, fill_value='FILL', dtype=dt)
assert isinstance(arr.fill_value, str)
assert arr.fill_value == 'FILL'
filled = arr.filled()
assert filled.tolist() == ['FILL', 'test', 'FILL', 'FILL']
```

## Next Steps


---

*Source: test_core.py:5717 | Complexity: Intermediate | Last updated: 2026-06-02*