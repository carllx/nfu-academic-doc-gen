# How To: Dealloc Weakref

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dealloc weakref

## Prerequisites

**Required Modules:**
- `gc`
- `weakref`
- `greenlet`


## Step-by-Step Guide

### Step 1: Assign seen = value

```python
seen = []
```

### Step 2: Assign g = greenlet.greenlet(...)

```python
g = greenlet.greenlet(worker)
```

### Step 3: Call g.switch()

```python
g.switch()
```

### Step 4: Assign g2 = greenlet.greenlet(...)

```python
g2 = greenlet.greenlet(lambda: None, g)
```

### Step 5: Assign g = weakref.ref(...)

```python
g = weakref.ref(g2)
```

### Step 6: Assign g2 = None

```python
g2 = None
```

### Step 7: Call self.assertEqual()

```python
self.assertEqual(seen, [None])
```

### Step 8: Call greenlet.getcurrent.parent.switch()

```python
greenlet.getcurrent().parent.switch()
```

### Step 9: Call seen.append()

```python
seen.append(g())
```


## Complete Example

```python
# Workflow
seen = []

def worker():
    try:
        greenlet.getcurrent().parent.switch()
    finally:
        seen.append(g())
g = greenlet.greenlet(worker)
g.switch()
g2 = greenlet.greenlet(lambda: None, g)
g = weakref.ref(g2)
g2 = None
self.assertEqual(seen, [None])
```

## Next Steps


---

*Source: test_weakref.py:23 | Complexity: Advanced | Last updated: 2026-06-02*