# How To: Refcounting

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test refcounting

## Prerequisites

**Required Modules:**
- `sys`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign objects = value

```python
objects = [object() for i in range(10)]
```

**Verification:**
```python
assert_(all((sys.getrefcount(o) == rc + 1 for o, rc in zip(objects, orig_rcs))))
```

### Step 2: Assign orig_rcs = value

```python
orig_rcs = [sys.getrefcount(o) for o in objects]
```

**Verification:**
```python
assert_(all((sys.getrefcount(o) == rc + 1 for o, rc in zip(objects, orig_rcs))))
```

### Step 3: Assign a = np.array(...)

```python
a = np.array(objects)
```

### Step 4: Assign b = np.array(...)

```python
b = np.array([2, 2, 4, 5, 3, 5])
```

### Step 5: Call a.take()

```python
a.take(b, out=a[:6], mode=mode)
```

### Step 6: Assign a = value

```python
a = np.array(objects * 2)[::2]
```

### Step 7: Call a.take()

```python
a.take(b, out=a[:6], mode=mode)
```

### Step 8: Call assert_()

```python
assert_(all((sys.getrefcount(o) == rc + 1 for o, rc in zip(objects, orig_rcs))))
```

### Step 9: Call assert_()

```python
assert_(all((sys.getrefcount(o) == rc + 1 for o, rc in zip(objects, orig_rcs))))
```


## Complete Example

```python
# Workflow
objects = [object() for i in range(10)]
if HAS_REFCOUNT:
    orig_rcs = [sys.getrefcount(o) for o in objects]
for mode in ('raise', 'clip', 'wrap'):
    a = np.array(objects)
    b = np.array([2, 2, 4, 5, 3, 5])
    a.take(b, out=a[:6], mode=mode)
    del a
    if HAS_REFCOUNT:
        assert_(all((sys.getrefcount(o) == rc + 1 for o, rc in zip(objects, orig_rcs))))
    a = np.array(objects * 2)[::2]
    a.take(b, out=a[:6], mode=mode)
    del a
    if HAS_REFCOUNT:
        assert_(all((sys.getrefcount(o) == rc + 1 for o, rc in zip(objects, orig_rcs))))
```

## Next Steps


---

*Source: test_item_selection.py:49 | Complexity: Advanced | Last updated: 2026-06-02*