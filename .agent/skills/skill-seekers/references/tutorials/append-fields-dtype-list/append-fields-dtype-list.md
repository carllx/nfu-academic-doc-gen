# How To: Append Fields Dtype List

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test append fields dtype list

## Prerequisites

**Required Modules:**
- `os`
- `numpy`
- `numpy.testing`
- `numpy.lib.recfunctions`
- `io`


## Step-by-Step Guide

### Step 1: Assign base = np.array(...)

```python
base = np.array([1, 2, 3], dtype=np.int32)
```

### Step 2: Assign names = value

```python
names = ['a', 'b', 'c']
```

### Step 3: Assign data = np.eye.astype(...)

```python
data = np.eye(3).astype(np.int32)
```

### Step 4: Assign dlist = value

```python
dlist = [np.float64, np.int32, np.int32]
```

### Step 5: Call append_fields()

```python
append_fields(base, names, data, dlist)
```


## Complete Example

```python
# Workflow
from numpy.lib.recfunctions import append_fields
base = np.array([1, 2, 3], dtype=np.int32)
names = ['a', 'b', 'c']
data = np.eye(3).astype(np.int32)
dlist = [np.float64, np.int32, np.int32]
try:
    append_fields(base, names, data, dlist)
except Exception:
    raise AssertionError
```

## Next Steps


---

*Source: test_regression.py:176 | Complexity: Advanced | Last updated: 2026-06-02*