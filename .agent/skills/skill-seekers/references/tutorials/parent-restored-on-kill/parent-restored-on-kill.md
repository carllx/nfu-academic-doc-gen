# How To: Parent Restored On Kill

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test parent restored on kill

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

### Step 1: Assign hub = RawGreenlet(...)

```python
hub = RawGreenlet(lambda: None)
```

### Step 2: Assign main = greenlet.getcurrent(...)

```python
main = greenlet.getcurrent()
```

### Step 3: Assign result = value

```python
result = []
```

### Step 4: Assign g = RawGreenlet(...)

```python
g = RawGreenlet(worker, parent=hub)
```

### Step 5: Call g.switch()

```python
g.switch()
```

### Step 6: Call self.assertTrue()

```python
self.assertTrue(result)
```

### Step 7: Call self.assertIs()

```python
self.assertIs(result[0], main)
```

### Step 8: Call self.assertIs()

```python
self.assertIs(result[1].parent, hub)
```

### Step 9: Assign hub = None

```python
hub = None
```

### Step 10: Assign main = None

```python
main = None
```

### Step 11: Call main.switch()

```python
main.switch()
```

### Step 12: Call result.append()

```python
result.append(greenlet.getcurrent().parent)
```

### Step 13: Call result.append()

```python
result.append(greenlet.getcurrent())
```

### Step 14: Call hub.switch()

```python
hub.switch()
```


## Complete Example

```python
# Workflow
hub = RawGreenlet(lambda: None)
main = greenlet.getcurrent()
result = []

def worker():
    try:
        main.switch()
    except greenlet.GreenletExit:
        result.append(greenlet.getcurrent().parent)
        result.append(greenlet.getcurrent())
        hub.switch()
g = RawGreenlet(worker, parent=hub)
g.switch()
del g
self.assertTrue(result)
self.assertIs(result[0], main)
self.assertIs(result[1].parent, hub)
del result[:]
hub = None
main = None
```

## Next Steps


---

*Source: test_greenlet.py:400 | Complexity: Advanced | Last updated: 2026-06-02*