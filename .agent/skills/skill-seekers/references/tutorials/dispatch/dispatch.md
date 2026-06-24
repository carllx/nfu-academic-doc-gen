# How To: Dispatch

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test dispatch

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign xy = value

```python
xy = [1, 2]
```

**Verification:**
```python
assert_(r == ((ShouldDispatch,), (s_d, xy), {}))
```

### Step 2: Assign s_d = ShouldDispatch(...)

```python
s_d = ShouldDispatch()
```

**Verification:**
```python
assert_(r == ((ShouldDispatch,), (xy, s_d), {}))
```

### Step 3: Assign r = histogram2d(...)

```python
r = histogram2d(s_d, xy)
```

**Verification:**
```python
assert_(r, ((ShouldDispatch,), (xy, xy), {'bins': s_d}))
```

### Step 4: Call assert_()

```python
assert_(r == ((ShouldDispatch,), (s_d, xy), {}))
```

**Verification:**
```python
assert_(r, ((ShouldDispatch,), (xy, xy), {'bins': [s_d, 5]}))
```

### Step 5: Assign r = histogram2d(...)

```python
r = histogram2d(xy, s_d)
```

**Verification:**
```python
assert_raises(Exception, histogram2d, xy, xy, bins=[s_d])
```

### Step 6: Call assert_()

```python
assert_(r == ((ShouldDispatch,), (xy, s_d), {}))
```

**Verification:**
```python
assert_(r, ((ShouldDispatch,), (xy, xy), {'weights': s_d}))
```

### Step 7: Assign r = histogram2d(...)

```python
r = histogram2d(xy, xy, bins=s_d)
```

### Step 8: Call assert_()

```python
assert_(r, ((ShouldDispatch,), (xy, xy), {'bins': s_d}))
```

### Step 9: Assign r = histogram2d(...)

```python
r = histogram2d(xy, xy, bins=[s_d, 5])
```

### Step 10: Call assert_()

```python
assert_(r, ((ShouldDispatch,), (xy, xy), {'bins': [s_d, 5]}))
```

### Step 11: Call assert_raises()

```python
assert_raises(Exception, histogram2d, xy, xy, bins=[s_d])
```

### Step 12: Assign r = histogram2d(...)

```python
r = histogram2d(xy, xy, weights=s_d)
```

### Step 13: Call assert_()

```python
assert_(r, ((ShouldDispatch,), (xy, xy), {'weights': s_d}))
```


## Complete Example

```python
# Workflow
class ShouldDispatch:

    def __array_function__(self, function, types, args, kwargs):
        return (types, args, kwargs)
xy = [1, 2]
s_d = ShouldDispatch()
r = histogram2d(s_d, xy)
assert_(r == ((ShouldDispatch,), (s_d, xy), {}))
r = histogram2d(xy, s_d)
assert_(r == ((ShouldDispatch,), (xy, s_d), {}))
r = histogram2d(xy, xy, bins=s_d)
assert_(r, ((ShouldDispatch,), (xy, xy), {'bins': s_d}))
r = histogram2d(xy, xy, bins=[s_d, 5])
assert_(r, ((ShouldDispatch,), (xy, xy), {'bins': [s_d, 5]}))
assert_raises(Exception, histogram2d, xy, xy, bins=[s_d])
r = histogram2d(xy, xy, weights=s_d)
assert_(r, ((ShouldDispatch,), (xy, xy), {'weights': s_d}))
```

## Next Steps


---

*Source: test_twodim_base.py:298 | Complexity: Advanced | Last updated: 2026-06-02*