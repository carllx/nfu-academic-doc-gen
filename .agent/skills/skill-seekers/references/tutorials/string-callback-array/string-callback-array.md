# How To: String Callback Array

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test string callback array

## Prerequisites

**Required Modules:**
- `math`
- `platform`
- `sys`
- `textwrap`
- `threading`
- `time`
- `traceback`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign cu1 = np.zeros(...)

```python
cu1 = np.zeros((1,), 'S8')
```

**Verification:**
```python
assert res == 0
```

### Step 2: Assign cu2 = np.zeros(...)

```python
cu2 = np.zeros((1, 8), 'c')
```

### Step 3: Assign cu3 = np.array(...)

```python
cu3 = np.array([''], 'S8')
```

### Step 4: Assign f = value

```python
f = self.module.string_callback_array
```

### Step 5: Assign res = f(...)

```python
res = f(callback, cu, cu.size)
```

**Verification:**
```python
assert res == 0
```


## Complete Example

```python
# Workflow
cu1 = np.zeros((1,), 'S8')
cu2 = np.zeros((1, 8), 'c')
cu3 = np.array([''], 'S8')

def callback(cu, lencu):
    if cu.shape != (lencu,):
        return 1
    if cu.dtype != 'S8':
        return 2
    if not np.all(cu == b''):
        return 3
    return 0
f = self.module.string_callback_array
for cu in [cu1, cu2, cu3]:
    res = f(callback, cu, cu.size)
    assert res == 0
```

## Next Steps


---

*Source: test_callback.py:106 | Complexity: Intermediate | Last updated: 2026-06-02*