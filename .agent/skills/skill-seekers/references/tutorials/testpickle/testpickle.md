# How To: Testpickle

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test testPickle

## Prerequisites

**Required Modules:**
- `pickle`
- `functools`
- `pytest`
- `numpy`
- `numpy._core.fromnumeric`
- `numpy._core.umath`
- `numpy.ma`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign x = arange(...)

```python
x = arange(12)
```

**Verification:**
```python
assert_(eq(x, y))
```

### Step 2: Assign unknown = masked

```python
x[4:10:2] = masked
```

### Step 3: Assign x = x.reshape(...)

```python
x = x.reshape(4, 3)
```

### Step 4: Assign s = pickle.dumps(...)

```python
s = pickle.dumps(x, protocol=proto)
```

### Step 5: Assign y = pickle.loads(...)

```python
y = pickle.loads(s)
```

### Step 6: Call assert_()

```python
assert_(eq(x, y))
```


## Complete Example

```python
# Workflow
x = arange(12)
x[4:10:2] = masked
x = x.reshape(4, 3)
for proto in range(2, pickle.HIGHEST_PROTOCOL + 1):
    s = pickle.dumps(x, protocol=proto)
    y = pickle.loads(s)
    assert_(eq(x, y))
```

## Next Steps


---

*Source: test_old_ma.py:610 | Complexity: Intermediate | Last updated: 2026-06-02*