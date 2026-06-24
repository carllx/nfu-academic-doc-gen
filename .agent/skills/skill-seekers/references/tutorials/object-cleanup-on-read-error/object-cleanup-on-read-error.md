# How To: Object Cleanup On Read Error

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test object cleanup on read error

## Prerequisites

**Required Modules:**
- `os`
- `sys`
- `io`
- `tempfile`
- `pytest`
- `numpy`
- `numpy.ma.testutils`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign sentinel = object(...)

```python
sentinel = object()
```

**Verification:**
```python
assert sys.getrefcount(sentinel) == 2
```

### Step 2: Assign already_read = 0

```python
already_read = 0
```

### Step 3: Assign txt = StringIO(...)

```python
txt = StringIO('x\n' * 10000)
```

**Verification:**
```python
assert sys.getrefcount(sentinel) == 2
```

### Step 4: Call np.loadtxt()

```python
np.loadtxt(txt, dtype=object, converters={0: conv})
```


## Complete Example

```python
# Workflow
sentinel = object()
already_read = 0

def conv(x):
    nonlocal already_read
    if already_read > 4999:
        raise ValueError('failed half-way through!')
    already_read += 1
    return sentinel
txt = StringIO('x\n' * 10000)
with pytest.raises(ValueError, match='at row 5000, column 1'):
    np.loadtxt(txt, dtype=object, converters={0: conv})
assert sys.getrefcount(sentinel) == 2
```

## Next Steps


---

*Source: test_loadtxt.py:467 | Complexity: Intermediate | Last updated: 2026-06-02*