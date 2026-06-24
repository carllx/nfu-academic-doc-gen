# How To: Frames Always Exposed

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test frames always exposed

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

### Step 1: Assign main = greenlet.getcurrent(...)

```python
main = greenlet.getcurrent()
```

### Step 2: Assign gr = RawGreenlet(...)

```python
gr = RawGreenlet(outer)
```

### Step 3: Assign frame = gr.switch(...)

```python
frame = gr.switch()
```

### Step 4: Assign unrelated = RawGreenlet(...)

```python
unrelated = RawGreenlet(lambda: None)
```

### Step 5: Call unrelated.switch()

```python
unrelated.switch()
```

### Step 6: Call self.assertEqual()

```python
self.assertEqual(frame.f_code.co_name, 'outer')
```

### Step 7: Call self.assertIsNone()

```python
self.assertIsNone(frame.f_back)
```

### Step 8: Call inner()

```python
inner(sys._getframe(0))
```

### Step 9: Call main.switch()

```python
main.switch(frame)
```


## Complete Example

```python
# Workflow
main = greenlet.getcurrent()

def outer():
    inner(sys._getframe(0))

def inner(frame):
    main.switch(frame)
gr = RawGreenlet(outer)
frame = gr.switch()
unrelated = RawGreenlet(lambda: None)
unrelated.switch()
self.assertEqual(frame.f_code.co_name, 'outer')
self.assertIsNone(frame.f_back)
```

## Next Steps


---

*Source: test_greenlet.py:937 | Complexity: Advanced | Last updated: 2026-06-02*