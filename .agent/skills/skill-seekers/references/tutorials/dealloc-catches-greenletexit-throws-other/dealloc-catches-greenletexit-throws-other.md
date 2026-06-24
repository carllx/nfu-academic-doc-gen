# How To: Dealloc Catches Greenletexit Throws Other

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test dealloc catches GreenletExit throws other

## Prerequisites

**Required Modules:**
- `gc`
- `sys`
- `time`
- `threading`
- `unittest`
- `abc`
- `abc`
- `greenlet`
- `greenlet`
- `leakcheck`
- `io`
- `copy`
- `greenlet`
- `greenlet`
- `threading`
- `threading`
- `greenlet`
- `functools`


## Step-by-Step Guide

### Step 1: Assign g = RawGreenlet(...)

```python
g = RawGreenlet(run)
```

### Step 2: Call g.switch()

```python
g.switch()
```

### Step 3: Assign oldstderr = value

```python
oldstderr = sys.stderr
```

### Step 4: Assign stderr, sys.stderr = StringIO(...)

```python
stderr = sys.stderr = StringIO()
```

### Step 5: Assign v = stderr.getvalue(...)

```python
v = stderr.getvalue()
```

### Step 6: Call self.assertIn()

```python
self.assertIn('Exception', v)
```

### Step 7: Call self.assertIn()

```python
self.assertIn('ignored', v)
```

### Step 8: Call self.assertIn()

```python
self.assertIn('SomeError', v)
```

### Step 9: Assign sys.stderr = oldstderr

```python
sys.stderr = oldstderr
```

### Step 10: Call greenlet.getcurrent.parent.switch()

```python
greenlet.getcurrent().parent.switch()
```


## Complete Example

```python
# Workflow
def run():
    try:
        greenlet.getcurrent().parent.switch()
    except greenlet.GreenletExit:
        raise SomeError from None
g = RawGreenlet(run)
g.switch()
oldstderr = sys.stderr
from io import StringIO
stderr = sys.stderr = StringIO()
try:
    del g
finally:
    sys.stderr = oldstderr
v = stderr.getvalue()
self.assertIn('Exception', v)
self.assertIn('ignored', v)
self.assertIn('SomeError', v)
```

## Next Steps


---

*Source: test_greenlet.py:200 | Complexity: Advanced | Last updated: 2026-06-02*