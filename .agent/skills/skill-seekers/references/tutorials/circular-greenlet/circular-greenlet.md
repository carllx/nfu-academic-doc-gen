# How To: Circular Greenlet

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test circular greenlet

## Prerequisites

**Required Modules:**
- `gc`
- `weakref`
- `greenlet`
- `leakcheck`
- `sys`


## Step-by-Step Guide

### Step 1: Assign o = circular_greenlet(...)

```python
o = circular_greenlet()
```

### Step 2: Assign o.self = o

```python
o.self = o
```

### Step 3: Assign o = weakref.ref(...)

```python
o = weakref.ref(o)
```

### Step 4: Call gc.collect()

```python
gc.collect()
```

### Step 5: Call self.assertIsNone()

```python
self.assertIsNone(o())
```

### Step 6: Call self.assertFalse()

```python
self.assertFalse(gc.garbage, gc.garbage)
```

### Step 7: Assign self = None

```python
self = None
```


## Complete Example

```python
# Workflow
class circular_greenlet(greenlet.greenlet):
    self = None
o = circular_greenlet()
o.self = o
o = weakref.ref(o)
gc.collect()
self.assertIsNone(o())
self.assertFalse(gc.garbage, gc.garbage)
```

## Next Steps


---

*Source: test_gc.py:24 | Complexity: Intermediate | Last updated: 2026-06-02*