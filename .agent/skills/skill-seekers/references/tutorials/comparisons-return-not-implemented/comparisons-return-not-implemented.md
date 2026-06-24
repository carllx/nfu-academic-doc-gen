# How To: Comparisons Return Not Implemented

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test comparisons return not implemented

## Prerequisites

**Required Modules:**
- `datetime`
- `pickle`
- `warnings`
- `zoneinfo`
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign obj = custom(...)

```python
obj = custom()
```

**Verification:**
```python
assert item.__eq__(obj) is NotImplemented
```

### Step 2: Assign dt = np.datetime64(...)

```python
dt = np.datetime64('2000', 'ns')
```

**Verification:**
```python
assert item.__ne__(obj) is NotImplemented
```

### Step 3: Assign td = value

```python
td = dt - dt
```

**Verification:**
```python
assert item.__le__(obj) is NotImplemented
```

### Step 4: Assign __array_priority__ = 10000

```python
__array_priority__ = 10000
```

**Verification:**
```python
assert item.__lt__(obj) is NotImplemented
```


## Complete Example

```python
# Workflow
class custom:
    __array_priority__ = 10000
obj = custom()
dt = np.datetime64('2000', 'ns')
td = dt - dt
for item in [dt, td]:
    assert item.__eq__(obj) is NotImplemented
    assert item.__ne__(obj) is NotImplemented
    assert item.__le__(obj) is NotImplemented
    assert item.__lt__(obj) is NotImplemented
    assert item.__ge__(obj) is NotImplemented
    assert item.__gt__(obj) is NotImplemented
```

## Next Steps


---

*Source: test_datetime.py:2775 | Complexity: Intermediate | Last updated: 2026-06-02*