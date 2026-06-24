# How To: Dealloc Switch Args Not Lost

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test dealloc switch args not lost

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

### Step 1: Assign seen = value

```python
seen = []
```

### Step 2: Assign worker = value

```python
worker = [RawGreenlet(worker)]
```

### Step 3: Call unknown.switch()

```python
worker[0].switch()
```

### Step 4: Assign initiator = RawGreenlet(...)

```python
initiator = RawGreenlet(initiator, worker[0])
```

### Step 5: Assign value = initiator.switch(...)

```python
value = initiator.switch()
```

### Step 6: Call self.assertTrue()

```python
self.assertTrue(seen)
```

### Step 7: Call self.assertEqual()

```python
self.assertEqual(value, 42)
```

### Step 8: Assign value = greenlet.getcurrent.parent.switch(...)

```python
value = greenlet.getcurrent().parent.switch()
```

### Step 9: Assign initiator.parent = value

```python
initiator.parent = greenlet.getcurrent().parent
```

### Step 10: Call greenlet.getcurrent.parent.switch()

```python
greenlet.getcurrent().parent.switch(value)
```

### Step 11: Call seen.append()

```python
seen.append(greenlet.getcurrent())
```


## Complete Example

```python
# Workflow
seen = []

def worker():
    value = greenlet.getcurrent().parent.switch()
    del worker[0]
    initiator.parent = greenlet.getcurrent().parent
    try:
        greenlet.getcurrent().parent.switch(value)
    finally:
        seen.append(greenlet.getcurrent())

def initiator():
    return 42
worker = [RawGreenlet(worker)]
worker[0].switch()
initiator = RawGreenlet(initiator, worker[0])
value = initiator.switch()
self.assertTrue(seen)
self.assertEqual(value, 42)
```

## Next Steps


---

*Source: test_greenlet.py:581 | Complexity: Advanced | Last updated: 2026-06-02*